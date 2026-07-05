from agents.memory_agent import MemoryAgent

state = {

    "question": "Why is nginx restarting?",

    "resources": [

        {

            "name": "nginx",

            "namespace": "default",

        }

    ],

    "analysis": {

        "root_cause": "Memory Exhaustion",

        "confidence": 0.95,

        "critical_evidence": [

            "OOMKilled",

            "Restart Count 8",

        ],

        "recommended_fix": [

            "Increase memory",

        ],

    },

}

agent = MemoryAgent()

agent.run(state)

print()

print(state["memory"])
