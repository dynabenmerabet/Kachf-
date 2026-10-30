"""
Multi-Agent Orchestrator managing execution flow between specialized agents.
"""

from src.middleware.pipeline import KachfMiddleware
from src.agents.evaluator import EvaluatorAgent
from src.agents.mapper import MarketMapperAgent

class AgentOrchestrator:
    def __init__(self):
        self.middleware = KachfMiddleware()
        self.evaluator = EvaluatorAgent()
        self.mapper = MarketMapperAgent()

    def run_pipeline(self, user_data: dict, mcp_server) -> dict:
        # Step 1: Middleware Input Validation
        clean_input = self.middleware.process_input(user_data)
        
        # Step 2: Agent 1 - Psychometric Evaluation
        profile = self.evaluator.process_assessment(clean_input.get("responses", []))
        
        # Step 3: MCP Context Injection
        mcp_context = mcp_server.handle_mcp_query(profile["academic_background"])
        
        # Step 4: Agent 2 - Market Mapping
        raw_recommendations = self.mapper.map_profile_to_careers(profile, mcp_context)
        
        # Step 5: Middleware Output Formatting
        return self.middleware.process_output({
            "user_profile": profile,
            "recommendations": raw_recommendations
        })
