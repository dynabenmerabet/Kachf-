"""
Pydantic schemas for psychometric profiling and career matching in Kachf AI.
Integrates Holland's RIASEC model and Big Five (OCEAN) traits.
"""

from pydantic import BaseModel, Field
from typing import List, Dict

class RIASECScore(BaseModel):
    realistic: float = Field(..., ge=0.0, le=100.0, description="Realistic score")
    investigative: float = Field(..., ge=0.0, le=100.0, description="Investigative score")
    artistic: float = Field(..., ge=0.0, le=100.0, description="Artistic score")
    social: float = Field(..., ge=0.0, le=100.0, description="Social score")
    enterprising: float = Field(..., ge=0.0, le=100.0, description="Enterprising score")
    conventional: float = Field(..., ge=0.0, le=100.0, description="Conventional score")

class BigFiveScore(BaseModel):
    openness: float = Field(..., ge=0.0, le=100.0)
    conscientiousness: float = Field(..., ge=0.0, le=100.0)
    extraversion: float = Field(..., ge=0.0, le=100.0)
    agreeableness: float = Field(..., ge=0.0, le=100.0)
    neuroticism: float = Field(..., ge=0.0, le=100.0)

class UserPsychometricProfile(BaseModel):
    user_id: str
    age: int = Field(..., ge=17, le=25)
    academic_background: str
    riasec: RIASECScore
    big_five: BigFiveScore
    primary_code: str = Field(..., description="Top 2-3 RIASEC code, e.g. 'IC'")

class CareerRecommendation(BaseModel):
    title: str
    sector: str
    match_confidence: float
    description: str
    day_in_life_summary: str
    key_skills_required: List[str]
