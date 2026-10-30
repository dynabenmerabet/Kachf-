"""
Kachf AI Engine - Main Orchestration System
Author: Dyna Benmerabet
Description: Multi-agent system leveraging MCP (Model Context Protocol) 
and RIASEC/Big Five psychometrics to uncover hidden career pathways in Algeria.
"""

import json
from src.schemas.models import UserPsychometricProfile, RIASECScore, BigFiveScore
from src.agents.evaluator import EvaluatorAgent
from src.agents.mapper import MarketMapperAgent
from src.mcp.market_server import KachfMCPServer

def main():
    print("=" * 60)
    print("🚀 Initializing Kachf AI Multi-Agent & MCP Pipeline...")
    print("=" * 60)

    # 1. Initialize System Components
    evaluator = EvaluatorAgent()
    mapper = MarketMapperAgent()
    mcp_server = KachfMCPServer()

    # 2. Simulate User Assessment (Computer Science Student)
    user_input_responses = ["I like solving logical puzzles", "I enjoy structure and data validation"]
    raw_profile = evaluator.process_assessment(user_input_responses)
    
    print(f"\n[1] EvaluatorAgent generated profile for User ({raw_profile['academic_background']}):")
    print(f"    - Primary RIASEC Vector: {raw_profile['primary_code']}")
    print(f"    - Investigative Score: {raw_profile['riasec']['investigative']}/100")
    print(f"    - Conventional Score: {raw_profile['riasec']['conventional']}/100")

    # 3. Retrieve Context via MCP Server
    mcp_context = mcp_server.handle_mcp_query(raw_profile['academic_background'])
    print(f"\n[2] MCP Server injected local market context for sector: {raw_profile['academic_background']}")

    # 4. Map Profile to Hidden Career Paths
    recommendations = mapper.map_profile_to_careers(raw_profile, mcp_context)
    
    print("\n[3] MarketMapperAgent computed non-obvious career options:")
    for rec in recommendations:
        print(f"    ✦ Role: {rec['title']} ({rec['sector']}) | Match Confidence: {rec['match_confidence'] * 100}%")
        print(f"      Reasoning: {rec['fit_reason']}")

    print("\n" + "=" * 60)
    print("✅ Pipeline execution finished successfully.")
    print("=" * 60)

if __name__ == "__main__":
    main()
