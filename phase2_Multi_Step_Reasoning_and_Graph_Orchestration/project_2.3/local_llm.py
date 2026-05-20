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
