from agent.investigation_guard import InvestigationGuard

guard = InvestigationGuard()

report = {

    "confidence": 0.96,

    "requires_more_evidence": False,

    "next_action": None,
}

finished, reason = guard.should_finish(
    report,
    observations=[],
)

print("Finished :", finished)
print("Reason    :", reason)

