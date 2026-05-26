import requests
from dotenv import load_dotenv
import os

load_dotenv()

def search_tool(query: str):
    """
    Simple Web search tool using DuckDuckGo HTML
    """
    try:
        url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url=url, headers=headers, timeout=10)
        
        print(f"\n🔍 DEBUG: Response status: {response.status_code}")
        print(f"🔍 DEBUG: Response length: {len(response.text)} chars")
        
        # Save to file for inspection
        with open("debug_search.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("🔍 DEBUG: Saved HTML to debug_search.html")
        
        # Simple fallback: extract any text between result classes
        text = response.text
        
        # Try different parsing approaches
        results = []
        
        # Approach 1: Look for result links
        if 'result__a' in text:
            print("🔍 Found result__a class")
            import re
            matches = re.findall(r'<a[^>]*class="result__a"[^>]*>([^<]+)</a>', text)
            results.extend(matches[:3])
        
        # Approach 2: Look for any links with relevant text
        if not results:
            print("🔍 Trying fallback parsing...")
            import re
            # Find any text between <a> tags that looks like a title
            matches = re.findall(r'<a[^>]*>([^<]{20,100})</a>', text)
            results.extend(matches[:3])
        
        # Approach 3: Just return first chunk of readable text
        if not results:
            print("🔍 Returning raw text preview...")
            # Remove HTML tags for readability
            import re
            clean_text = re.sub(r'<[^>]+>', ' ', text)
            clean_text = re.sub(r'\s+', ' ', clean_text)
            return f"Search results for '{query}':\n{clean_text[:500]}..."
        
        if results:
            return f"Search results for '{query}':\n" + "\n".join(results[:3])
        else:
            return f"No clear results found for '{query}'. Please provide the information directly."
            
    except Exception as e:
        print(f"❌ Search error: {e}")
        return f"Search tool error: {str(e)}. Please provide the information manually."