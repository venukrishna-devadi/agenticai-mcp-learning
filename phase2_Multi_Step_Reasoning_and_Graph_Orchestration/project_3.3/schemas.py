# STEP 2 — schemas.py

# VERY IMPORTANT.

# We now force structured LLM outputs.
# This is exactly how:

# * OpenAI function calling
# * MCP
# * tool calling APIs

# work internally.

from pydantic import BaseModel

class ToolDecision(BaseModel):
    need_tool: bool
    tool_name: str
    tool_input: str

# Instead of parsing messy text: "maybe use calculator..."
# We force:
# structured reasoning
# This is industrial-grade agent design.