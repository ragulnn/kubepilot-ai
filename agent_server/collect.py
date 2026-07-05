from fastapi import APIRouter

from router.capability_router import CapabilityRouter

from evidence_engine.dispatcher import EvidenceDispatcher
from evidence_engine.response_builder import (
    EvidenceResponseBuilder,
)

router = APIRouter()

dispatcher = EvidenceDispatcher()

builder = EvidenceResponseBuilder()

capability = CapabilityRouter()


@router.post("/collect")
def collect(request: dict):

    question = request.get("question", "")

    requests = capability.route(question)

    responses = dispatcher.collect(requests)

    return builder.build(

        question,

        responses,

    )
