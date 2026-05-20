# 🚀 Agentic AI & MCP Learning Path

## From Zero to Production-Grade Agents

[![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)](https://python.org)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.6+-green.svg)](https://langchain-ai.github.io/langgraph/)
[![Ollama](https://img.shields.io/badge/Ollama-Qwen2.5_7B-orange.svg)](https://ollama.ai)

---

## 📖 What is This?

**A complete, project-based learning path to master Agentic AI and MCP (Model Context Protocol) from absolute scratch.**

This repository contains **15+ progressive projects** that teach you how to build AI agents layer by layer - starting with a simple LLM wrapper and evolving to production-ready governed agents with human-in-the-loop capabilities.

**No LangChain black magic. No copy-paste. Just pure understanding built from first principles.**

---

## 🎯 Why This Learning Path?

Most tutorials jump straight to LangChain or AutoGPT without explaining:
- Why agents need state?
- How tool calling actually works?
- What makes ReAct loops special?
- When to ask humans for help?
- Why audit trails matter?

**You will NOT have those gaps after this course.**

---

## 📊 What You'll Build

### ✅ PHASE 0: Foundation (Projects 0.1-0.2)
- Custom LLM wrapper for local models (Qwen2.5 via Ollama)
- Validation & retry logic with JSON schemas

### ✅ PHASE 1: Single-Step Agents (Projects 1.1-1.3)
- Intent routing agent (decides between tools)
- Calculator tool agent (delegates math to Python)
- File reader agent (RAG grounding on bank statements)

### ✅ PHASE 2: Multi-Step Reasoning (Projects 2.1-2.3)
- Research assistant (extract claims → limitations → explanations)
- Planning agent (decomposes goals into executable tasks)
- Reflection agent (self-critique + improvement loop)

### ✅ PHASE 3: Graph Orchestration (Projects 3.1-3.5)
- LangGraph basics (stateful nodes + edges)
- Conditional routing (math vs science vs history)
- Tool-calling agent (structured JSON decisions)
- **ReAct loop agent (iterative reasoning + acting)**
- **HITL Governed Agent (human-in-the-loop + audit trails)** ← CURRENT

### 🔜 PHASE 4: Multi-Agent Systems (Coming)
- Supervisor agents, agent handoffs, collaboration

### 🔜 PHASE 5: MCP Integration (Coming)
- Model Context Protocol servers, tool registries

---

## 🧠 Key Concepts You'll Master

| Concept | Project | What You Learn |
|---------|---------|----------------|
| **LLM Wrapper** | 0.1 | Clean abstraction for local models |
| **Validation** | 0.2 | Reliable JSON parsing + retries |
| **Intent Routing** | 1.1 | Agent decides actions, not just text |
| **Tool Delegation** | 1.2 | LLM reasons, tools compute |
| **RAG Grounding** | 1.3 | External knowledge + file I/O |
| **Stateful Agents** | 2.1 | Working memory across steps |
| **Planning** | 2.2 | Task decomposition + execution |
| **Reflection** | 2.3 | Self-critique + improvement |
| **LangGraph** | 3.1 | Graph-based orchestration |
| **ReAct Loop** | 3.2 | Think → Act → Observe → Repeat |
| **HITL Governance** | 3.3 | Human approval + audit trails |

---

## 🛠️ Tech Stack

- **Local LLM**: Qwen2.5 7B via Ollama (no API costs!)
- **Framework**: LangGraph for graph orchestration
- **State Management**: Pydantic BaseModel
- **Tools**: Calculator, Census API, File Reader
- **External APIs**: US Census Bureau (real data!)

---

## 🚀 Quick Start

#### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/AgenticAI_MCP_Learning_ChatGPT.git
cd AgenticAI_MCP_Learning_ChatGPT


#### 2. Install dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt


#### 3. Install Ollama and pull Qwen
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt


#### 4. Set up API keys (for Project 3.2+)
cp .env.example .env
Add your CENSUS_API_KEY (free from census.gov)


#### 5. Run any project
python3 phase3/project_3.5/main.py


## 🎓 Learning Progression

| Step | Project | Concept | Status |
|------|---------|---------|--------|
| 1 | 0.1-0.2 | Simple LLM Chat + Validation | ✅ |
| 2 | 1.1 | Intent Routing | ✅ |
| 3 | 1.2 | Tool Calling (Calculator) | ✅ |
| 4 | 1.3 | RAG (File Reader) | ✅ |
| 5 | 2.1 | Multi-Step Pipeline | ✅ |
| 6 | 2.2 | Planning Agent | ✅ |
| 7 | 2.3 | Reflection Agent | ✅ |
| 8 | 3.1 | LangGraph Basics | ✅ |
| 9 | 3.2 | Conditional Routing | ✅ |
| 10 | 3.3 | Tool Calling Agent | ✅ |
| 11 | 3.4 | ReAct Loop | ✅ |
| 12 | 3.5 | **HITL Governed Agent** | ✅ 
| 13 | 4.x | Multi-Agent Systems | 🔜 |
| 14 | 5.x | MCP Integration | 🔜 |



💡 Highlights from Project 3.5 (HITL Governed Agent)

What it does: An agent that knows when to ask humans for help, tracks every decision, and respects human override.

Key features:
- Confidence scoring (0.0 to 1.0)
- Automatic approval gates for high-risk actions
- Complete audit trail for compliance
- Human override (STOP, MODIFY, REVERSE)
- Pausable/resumable execution

Example flow:

User: "Transfer $15,000 to savings"

Agent: [Thinks] "Large amount detected. Confidence: 0.31"
Agent: "⚠️ Approve transfer of $15,000?"

Human: "Yes, approved"

Agent: ✅ "Transfer completed"

[Audit trail logged for compliance]


📸 Sample Outputs - ReAct Loop Agent

THINK NODE
Thought: "Need Texas and California populations"

TOOL NODE
Tool: census_population_tool("Texas")
Output: 29,527,941

[Cycles 2 more times...]

FINAL ANSWER
Texas population is approximately 75.3% of California

## 🗺️ Roadmap - What's Coming

### ✅ Phase 0-3: Complete (15+ projects)
- Foundation (LLM wrapper, validation)
- Single-Step Agents (routing, calculator, RAG)
- Multi-Step Reasoning (pipeline, planning, reflection)
- Graph Orchestration (LangGraph, routing, ReAct, HITL)

### 🔜 Phase 4: Multi-Agent Systems (In Progress)

| Project | Concept | Status |
|---------|---------|--------|
| 4.1 | Supervisor Agent - Coordinates multiple agents | 📝 Planning |
| 4.2 | Agent Handoff - Pass context between agents | 📝 Planning |
| 4.3 | Shared Memory - Agents remember across handoffs | 📝 Planning |
| 4.4 | Collaborative Agents - Debate & consensus | 📝 Planning |

### 🔜 Phase 5: MCP Integration (Model Context Protocol)

| Project | Concept | Status |
|---------|---------|--------|
| 5.1 | MCP Server - Build a tool server | 📋 Planned |
| 5.2 | Tool Registry - Dynamic tool discovery | 📋 Planned |
| 5.3 | MCP Client Agent - Discover + use tools | 📋 Planned |
| 5.4 | Cross-Agent MCP - Multi-agent tool sharing | 📋 Planned |

### 🔜 Phase 6: Production Readiness

| Project | Concept | Status |
|---------|---------|--------|
| 6.1 | Streaming Responses - Real-time thinking | 📋 Planned |
| 6.2 | Checkpointing - Pause/resume agents | 📋 Planned |
| 6.3 | Human Approval Dashboard - UI for HITL | 📋 Planned |
| 6.4 | Agent Observability - Metrics & logging | 📋 Planned |
| 6.5 | Multi-modal Agents - Image + audio inputs | 🔮 Vision |

---

## 📅 Update Frequency

- **Weekly updates** - New projects added every week
- **GitHub stars** ⭐ - Help me prioritize what to build next
- **Issues & PRs** - Your feedback shapes the roadmap

**Follow this repo to get notified about new projects!**

 🤝 Who Is This For?

| Concept | Project |
|---------|---------|
| **Aspiring AI Engineer** | Learn agentic AI from first principless |
| **Students** | Understand what happens under the hood |
| **Developers** | Build production-ready agents |
| **Self-learners** | Progressive, project-based curriculum |
| **Educators** | Basic Python knowledge. Everything else is taught. |



📈 Current Status

Phase	Projects	Status
Phase 0	0.1 - 0.2	✅ Complete
Phase 1	1.1 - 1.3	✅ Complete
Phase 2	2.1 - 2.3	✅ Complete
Phase 3	3.1 - 3.5	✅ Complete (HITL done!)
Phase 4	Multi-Agent	🔜 In Progress
Phase 5	MCP	📋 Planned

