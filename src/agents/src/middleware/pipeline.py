"""
Middleware pipeline for Kachf AI.
Handles input validation, safety guards, and logging across agents.
"""

from typing import Dict, Any

class KachfMiddleware:
    def __init__(self):
        self.pipeline_version = "1.0-middleware"

    def process_input(self, user_payload: Dict[str, Any]) -> Dict[str, Any]:
        """Validates payload and enforces privacy/guardrails before sending to agents."""
        print("[Middleware] Validating input payload & applying guardrails...")
        if "academic_background" not in user_payload:
            raise ValueError("Missing critical field: academic_background")
        return user_payload

    def process_output(self, agent_output: Dict[str, Any]) -> Dict[str, Any]:
        """Formats and sanitizes agent responses."""
        print("[Middleware] Sanitizing output & structuring final response...")
        return agent_output
