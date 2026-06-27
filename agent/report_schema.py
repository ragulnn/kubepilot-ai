REPORT_SCHEMA = """
Return ONLY valid JSON.

Format:

{
    "root_cause": "",
    "confidence": 0.0,
    "severity": "",
    "symptom": "",
    "affected_resource": "",
    "namespace": "",
    "evidence": [],
    "recommended_fix": [],

    "next_action": {
        "tool": "",
        "resource": "",
        "name": "",
        "namespace": ""
    },

    "requires_more_evidence": false,
    "requires_manual_review": false
}
"""
