class AgentState:

    def __init__(self):
        self.abstract = ""
        self.claims = ""
        self.limitations = ""
        self.beginner_explanation = ""

    def show_state(self):

        return{
            "abstract": self.abstract,
            "claims": self.claims,
            "limitations": self.limitations,
            "beginner_explanation": self.beginner_explanation
        }
    
# HUGE CONCEPT HERE

# This object is:
# working memory

# The agent now stores:

# * intermediate reasoning
# * partial outputs
# * evolving knowledge

# This is foundational for:

# * LangGraph state
# * autonomous workflows
# * planning agents
# * memory systems

# VERY important.