# STEP 7 — agent.py
# This is your first Retrieval-Augmented Agent
# Major milestone: it can decide to read a file, then answer using that context.

from logger import log_section
from prompts import ROUTER_SYSTEM_PROMPT, ANSWER_SYSTEM_PROMPT
from validators import validate_tool
import re  # moved up — used for extracting names in transfers

class FileReaderAgent:
    def __init__(self, llm, tools):
        # store the LLM client and the toolset (read_statement, filter_and_sum, etc.)
        self.llm = llm
        self.tools = tools

    # ---------- ROUTER ----------
    def decide_tool(self, user_query):
        """Ask the LLM which tool to use. Temperature 0.0 = deterministic routing."""
        response = self.llm.chat(
            system_prompt=ROUTER_SYSTEM_PROMPT,
            user_prompt=user_query,
            temperature=0.0
        )

        log_section("RAW ROUTER RESPONSE", response)

        # validate_tool checks if LLM output is valid JSON like {"tool": "read_statement"}
        validation = validate_tool(response)

        if validation["valid"]:
            return validation["tool"]

        # fallback if router fails
        return "normal_response"

    # ---------- ANSWERER ----------
    def answer_with_context(self, user_query, context):
        """Send the retrieved bank statement + question to the LLM."""
        final_prompt = f"""
BANK_STATEMENT:
{context}

USER_QUESTION: {user_query}
"""
        response = self.llm.chat(
            system_prompt=ANSWER_SYSTEM_PROMPT,
            user_prompt=final_prompt,
            temperature=0.2  # low temp for factual answers
        )
        return response

    # ---------- MAIN RUN LOOP ----------
    def run(self, user_query):
        log_section("USER QUERY", user_query)

        # 1. Decide which path to take
        tool_decided = self.decide_tool(user_query=user_query)
        log_section("SELECTED TOOL", tool_decided)

        # 2. If router chose to read the statement, do RAG
        if tool_decided == "read_statement":
            file_result = self.tools.read_statement()
            print(file_result)

            if not file_result["success"]:
                return file_result["error"]

            context = file_result["content"]
            log_section("RETRIEVED CONTEXT", context[:500] + "...")

            # --- Enhancement 1: quick math for gas/fuel ---
            if "gas" in user_query.lower() or "fuel" in user_query.lower():
                log_section("Enhancement", "Using keyword filter + sum")
                filtered = self.tools.filter_and_sum(context, "gas")

                if filtered["found"]:
                    response = f"💰 GAS SPENDING SUMMARY:\n"
                    response += f"   Total: ${filtered['total']:.2f}\n"
                    response += f"   Transactions: {filtered['count']}\n\n"
                    response += f"📋 First few transactions:\n"
                    for t in filtered["transactions"][:3]:
                        response += f"   {t['merchant'][:40]}... ${t['amount']:.2f}\n"
                else:
                    response = filtered["message"]

            # --- Enhancement 2: total transfers to a person ---
            elif "total" in user_query.lower() and "transfer" in user_query.lower():
                log_section("ENHANCEMENT", "Filtering for transfers")

                name_match = re.search(r'to (\w+ \w+)', user_query, re.IGNORECASE)
                if name_match:
                    name = name_match.group(1)
                    filtered = self.tools.filter_and_sum(context, f"Zelle payment to {name}")

                    if filtered["found"]:
                        response = f"💰 TRANSFERS TO {name.upper()}:\n"
                        response += f"   Total sent: ${abs(filtered['total']):.2f}\n"
                        response += f"   Number of transfers: {filtered['count']}"
                    else:
                        response = f"No transfers found to {name}"
                else:
                    # if no name found, fall back to LLM
                    response = self.answer_with_context(user_query, context)

            # --- Default RAG path ---
            else:
                response = self.answer_with_context(user_query, context)

        # 3. If router didn't choose a tool, just chat normally
        else:
            response = self.llm.chat(
                system_prompt="You are a helpful assistant",
                user_prompt=user_query,
                temperature=0.5
            )

        log_section("FINAL RESPONSE", response)
        return response