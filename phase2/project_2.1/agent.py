# multi-stage reasoning pipeline

from logger import log_section
from prompts import CLAIM_EXTRACTION_PROMPT, LIMITATION_ANALYSIS_PROMPT, BEGINNER_EXPLANATION_PROMPT

from state import AgentState

class ResearchAssistantAgent:

    def __init__(self, llm):
        self.llm = llm
        self.state = AgentState

    def load_abstract(self, text):

        self.state.abstract = text
    
    def extract_claims(self):

        log_section("STEP 1 - Claim Extraction",
                    "Analyzing abstract...")
        
        claims = self.llm.chat(
            system_prompt = CLAIM_EXTRACTION_PROMPT,
            user_prompt = self.state.abstract,
            temperature = 0.2
        )

        self.state.claims = claims

        log_section("Claims Extracted",
                    claims)
    
    def analyze_limitations(self):

        log_section("STEP 2 - LIMITATION EXTRACTION",
                    "Critiquing Extracted Claims ...")
        
        limitations = self.llm.chat(system_prompt = LIMITATION_ANALYSIS_PROMPT,
                                    user_prompt = self.state.claims,
                                    temperature = 0.3)
        
        self.state.limitations = limitations

        log_section("Limitations Extracted",
                    limitations)
        
    def generate_beginner_explanations(self):

        log_section("STEP 3 - BEGINNER EXPLANATION",
                    "Generation Beginner Explanations ...")
        
        beginner_explanation = self.llm.chat(system_prompt = BEGINNER_EXPLANATION_PROMPT,
                                             user_prompt = self.state.abstract,
                                             temperature = 0.5)
        
        self.state.beginner_explanation = beginner_explanation

        log_section("Beginner Explanation",
                    beginner_explanation)
        
    
    def generate_final_report(self):

        report = f"""
================ FINAL REPORT ================

RESEARCH ABSTRACT:
{self.state.abstract}

---------------------------------------------

KEY CLAIMS:

{self.state.claims}

---------------------------------------------

LIMITATIONS:

{self.state.limitations}

---------------------------------------------

BEGINNER EXPLANATION:

{self.state.beginner_explanation}

=============================================
"""
        
        return report
    
    def run(self):

        self.extract_claims()
        self.analyze_limitations()
        self.generate_beginner_explanations()
        
        return self.generate_final_report()
    



# Notice
# self.state.claims

# becomes input to:analyze_limitations()

# This means:

# later reasoning depends on earlier reasoning

# This is the birth of:

# * agent state flow
# * graph execution
# * planning systems

# Critical concept.