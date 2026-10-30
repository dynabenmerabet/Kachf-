# 🧭 Kachf AI (كشف)
> **Agentic Career Guidance & Hidden Pathway Discovery Engine for Algerian Youth**

Kachf is an AI-powered multi-agent system designed to dismantle societal and psychological barriers in higher education orientation across Algeria and emerging markets. By coupling standardized psychometric frameworks (**Holland’s RIASEC** & **Five-Factor Model / Big Five**) with real-time local market data via **Model Context Protocol (MCP)**, Kachf uncovers non-obvious, high-fit career trajectories for young adults (ages 17–25).

---

## 🔬 Research & Psychological Methodology

Traditional orientation in Algeria often forces students into high-prestige majors (e.g., Medicine, Computer Science) without aligning with their cognitive or personality profiles. Kachf bridges this gap using a dual-framework methodology:

1. **Holland Code (RIASEC):** Evaluates vocational personality across six operational dimensions:
   - *Realistic (R), Investigative (I), Artistic (A), Social (S), Enterprising (E), Conventional (C).*
2. **Big Five Personality Inventory (OCEAN):** Assesses core behavioral traits:
   - *Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism.*

These psychometric vectors are mapped against a specialized matrix to identify cross-disciplinary "hidden careers" (e.g., mapping a CS background with high Investigative + Conventional scores to **IT Auditing** or **Health-Tech Data Governance**).

---

## 🛠️ System Architecture & Multi-Agent Design

Built in **Cursor IDE** using Python and structured for LLM orchestration:

* **`EvaluatorAgent`:** Executes dynamic, multi-turn psychometric interviews to generate structured JSON profiles containing RIASEC scores and OCEAN confidence metrics.
* **`MarketMapperAgent`:** Communicates via **MCP (Model Context Protocol)** to query contextual databases of Algerian university curricula, emerging remote roles, and industry sectors.
* **`CareerSimulatorAgent`:** Synthesizes the user's personality vector and local market data to generate realistic "Day-in-the-Life" simulations and custom growth roadmaps.

---

## 📁 Repository Structure

```text
.
├── README.md                # System documentation & research foundation
├── mcp_config.json          # MCP Server configuration for local dataset context
├── requirements.txt         # Core Python dependencies & LLM SDKs
├── app.py                   # System entry point & orchestration loop
├── src/
│   ├── agents/              # Multi-agent implementations
│   │   ├── evaluator.py     # RIASEC & Big Five psychometric engine
│   │   ├── mapper.py        # MCP-connected market mapping agent
│   │   └── simulator.py     # Interactive career scenario generator
│   ├── mcp/
│   │   └── market_server.py # MCP server delivering Algerian educational & job market data
│   └── schemas/
│       └── models.py        # Pydantic JSON schemas for strict type safety
└── ai_prompts/
    └── system_prompts.py    # Prompt-as-Code definitions for all agents
