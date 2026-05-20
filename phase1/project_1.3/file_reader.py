def read_text_file(file_path: str):

    try:
        with open(file_path, "r") as f:
            content = f.read()
        
        return{
            "success": True,
            "content": content
        }
    
    except Exception as e:

        return{
            "succuess": False,
            "error": str(e)
        }


# IMPORTANT CONCEPT

# This tool:

# * accesses external world
# * retrieves knowledge
# * returns context

# This is exactly how:

# * RAG
# * MCP
# * enterprise AI

# work conceptually.