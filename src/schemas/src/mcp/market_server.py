"""
MCP (Model Context Protocol) Server implementation for Kachf AI.
Provides structured context retrieval for Algerian university paths and hidden job markets.
"""

import json
from typing import Dict, Any

class KachfMCPServer:
    def __init__(self):
        self.server_name = "algerian-job-market-mcp"
        self._load_knowledge_base()

    def _load_knowledge_base(self):
        # Simulated local dataset connecting academic backgrounds to non-obvious careers
        self.knowledge_base = {
            "computer_science": {
                "traditional_paths": ["Software Developer", "IT Support"],
                "hidden_paths": [
                    {"title": "IT Auditor", "sector": "Finance / Compliance", "fit_reason": "Suits analytical and methodical (Conventional/Investigative) profiles."},
                    {"title": "Health-Tech Product Manager", "sector": "Healthcare", "fit_reason": "Bridges technical execution with systemic problem-solving."}
                ]
            },
            "sciences_experimentales": {
                "traditional_paths": ["Medical Doctor", "Biologist"],
                "hidden_paths": [
                    {"title": "Bioinformatics Analyst", "sector": "Tech / Biotech", "fit_reason": "Combines scientific rigor with computational logic."},
                    {"title": "Medical Science Liaison", "sector": "Pharmaceutical Industry", "fit_reason": "Leverages scientific background with strong interpersonal communication."}
                ]
            }
        }

    def handle_mcp_query(self, background: str) -> Dict[str, Any]:
        """
        Retrieves structured context based on the student's academic background.
        """
        normalized_key = background.lower().strip().replace(" ", "_")
        return self.knowledge_base.get(normalized_key, {
            "traditional_paths": ["General Graduate Tracks"],
            "hidden_paths": [{"title": "Cross-Disciplinary Consultant", "sector": "Consulting", "fit_reason": "Adaptable across emerging markets."}]
        })

if __name__ == "__main__":
    server = KachfMCPServer()
    print("MCP Server initialized and ready for context injection.")
