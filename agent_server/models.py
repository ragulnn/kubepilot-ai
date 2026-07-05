from pydantic import BaseModel


class InvestigationRequest(BaseModel):

    question: str


class InvestigationResponse(BaseModel):

    root_cause: str

    confidence: float

    evidence: list

    recommended_fix: list

    requires_manual_review: bool
