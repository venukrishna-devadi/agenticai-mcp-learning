# def search_tool(query: str):
#     return f"Mock result for: {query}"

import requests

def search_tool(query: str):
    """DuckDuckGo API - no CAPTCHA"""
    try:
        url = "https://api.duckduckgo.com/"
        params = {
            'q': query,
            'format': 'json',
            'no_html': 1,
            'skip_disambig': 1
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        if data.get('Abstract'):
            return data['Abstract']
        elif data.get('Definition'):
            return data['Definition']
        else:
            return f"Search results for: {query}"
    except Exception as e:
        return f"Search error: {e}"