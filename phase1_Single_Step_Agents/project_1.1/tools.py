# STEP 4 — tools.py

# These are your agent capabilities.

# IMPORTANT:
# The tools do the work.
# The agent only decides.

class AgentTools:

    def __init__(self, llm):
        self.llm = llm

    def summarize(self, text: str):
        print("\n[Tool Execution] summarize()\n")
        return self.llm.generate_summary(text)
    
    def breakdown(self, text: str):
        print("\n[Tool Execution] breakdown()\n")
        return self.llm.generate_structured_paper_breakdown(text)