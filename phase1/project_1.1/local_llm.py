import ollama

class LocalLLM:
    """
    Thin wrapper around Ollama for local model inference.

   -Why this wrapper exists:
   - keeps Ollama-specific code in one place
   - gives the rest of the project a clean interfac
   - makes future model swapping easier
   """
    
    def __init__(self,
                 model_name: str = "qwen2.5:7b"):
        
        self.model_name = model_name
    
    def chat(self,
             system_prompt: str,
             user_prompt: str,
             temperature: float):
        
        try:

            response = ollama.chat(model=self.model_name,
                                   messages=[
                                       {"role":"system", "content": system_prompt},
                                       {"role":"user", "content": user_prompt}
                                   ],
                                   options={"temperature": temperature})
            
            message = response.get("message", {})
            content = message.get("content", "")

            if not content or not isinstance(content, str):
                raise RuntimeError("Ollama returned an empty or invalid response.")
            
            return content.strip()
        except Exception as e:
            raise RuntimeError(f"Ollama call failed: {e}")
        
    
    def generate_structured_paper_breakdown(self, text: str) -> str:

        """
        Create a detailed breakdown explanation of the documemnt.
        Used by tools.breakdown()"""

        system_prompt = """You are a technical analyst. Created DETAILED breakdown.
        Return EXACT sections:
        ## Problem
        ## Approach
        ## Key Contributions
        ## Limitations
        ## Beginner Explanation
        
        Be thorough. Use bullet points.
        """

        user_prompt = f"Text to analyze:\n{text}"

        return self.chat(system_prompt = system_prompt,
                         user_prompt = user_prompt,
                         temperature=0.3)
    
    def generate_summary(self, text: str) -> str:

        """
        Create concise summary of the document.
        Used by tools.summarize()
        """
        system_prompt = """
        You are a research assistant. Create a CONCISE summary.

Return ONLY:
## What it is
## Key points
## Why it matters

No extra text. No markdown except these headings.
"""
        user_prompt = f"Text to summarize:\n{text}"

        return self.chat(system_prompt=system_prompt,
                         user_prompt=user_prompt,
                         temperature=0.3)