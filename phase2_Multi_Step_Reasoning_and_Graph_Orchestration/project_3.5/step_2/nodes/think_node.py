from local_llm import LocalLLM
import json

llm = LocalLLM()

def think_node(state):

    """
    ReAct Think Node
    Responsibilies:
    1. Decide whether to use tool or ask human or finalize
    2. Use oBservation context properly
    3. Prevent repeated loops
    4. Manage retry strategy
    """

    print("\n============================================================")
    print("THINK NODE")
    print("============================================================")

    if state.step_count >= state.max_steps:
        print("Max steps reached. Forcing to quit.")
        state.need_tool = False
        state.need_human = False
        state.final_answer = f"Max steps reached. Last thought: {state.current_thought}"
        return state
    
    if getattr(state, "human_response_consumed", False):
        state.need_human = False

    
    if state.tool_output and not state.need_tool:
        print("Already have tool output. Finalizing")
        state.need_human = False
        state.need_tool= False
        state.final_answer = state.tool_output
        return state
    
    # retry failure handling
    if state.retry_count >= 3:
        print(f"Too many retries ({state.retry_count}). Escalating to human.")
        state.need_tool = False
        state.need_human = True
        state.human_question = (
            f"I tried multiple approaches but got stuck. "
            f"Could you help with: {state.user_query}"
        )
        state.current_thought = "Escalating to human due to repeated failures"
        return state
    
    # build context for llm
    last_observation = getattr(state, "last_observation", None)

    prompt = f"""

You are a ReAct reasoning agent.
User Query:
{state.user_query}

Step Count:
{state.step_count} / {state.max_steps}

Retry Count:
{getattr(state, 'retry_count', 0)}

Last Observation:
{state.last_observation}

Human Response:
{state.human_response if state.human_response else "None"}

Tool Output (if any):
{state.tool_output}

Rules:
1. Use tools only when necessary
2. Ask human ONLY when information is missing or unclear
3. If enough info exists, stop and finalize
4. Do NOT repeat previous failed actions
5. Be concise

IMPORTANT:
1. If human_response is present, treat it as FINAL missing input.
2. Do NOT ask for it again.
3. If human_response is present AND calculation is required, you MUST return: need_tool = true
and provide tool_name + tool_input.

Return STRICT JSON:
If action needed:
{{
  "thought": "...",
  "confidence": 0.0-1.0,
  "need_tool": true/false,
  "tool_name": "...",
  "tool_input": "...",
  "need_human": true/false,
  "human_question": "..."
}}

If finished:

{{
  "thought": "...",
  "confidence": 0.0-1.0,
  "need_tool": false,
  "need_human": false
}}
"""
    
    if state.human_response and not state.human_response_consumed:
        print("Consuming human response for reasoning")
        state.human_response_consumed = True
    
    response = llm.chat(
        system_prompt= ("You are a strict JSON-only ReAct agent. "
                        "Never return text outside JSON."),
        user_prompt= prompt,
        temperature= 0.2
    )

    print("\nRaw Think Response:\n")
    print(response)

    # parse data safely
    try:
        data = json.loads(response)
    except:
        print("JSON parse failed. Forcing human fallback.")
        state.need_tool = False
        state.need_human = True
        state.human_question = "I couldn't understand the response. Please rephrase."
        return state
    
    # update state from llm
    state.current_thought = data.get("thought", "")

    state.confidence = data.get("confidence", 0.5)

    state.need_tool = data.get("need_tool", False)

    state.selected_tool = data.get("tool_name", "")

    state.tool_input = data.get("tool_input", "")

    state.need_human = data.get("need_human", False)

    state.human_question = data.get("human_question", "")

    # step + history update
    state.step_count += 1
    state.history.append(
        {
            "step": state.step_count,
            "type": "thought",
            "content": state.current_thought,
            "confidence": state.confidence
        }
    )

    print("\nUpdated State:")
    print(state)

    # loop safety check
    if state.step_count >= state.max_steps:
        print("Forced stop due to max steps.")
        state.need_tool = False
        state.need_human = False
        state.final_answer = f"Stopped at max steps. Last thought: {state.current_thought}"
    
    return state