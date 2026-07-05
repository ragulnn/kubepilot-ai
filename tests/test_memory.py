from datetime import datetime

from memory.incident import Incident
from memory.repository import IncidentRepository

repo = IncidentRepository()

incident = Incident(

    question="Why is nginx restarting?",

    resource_name="nginx",

    namespace="default",

    root_cause="Memory Exhaustion",

    confidence=0.95,

    findings=[

        "OOMKilled",

        "Restart Count 8",

    ],

    recommendations=[

        "Increase memory",

    ],

    timestamp=str(

        datetime.now()

    ),

)

repo.save(

    incident

)

print(

    repo.load()

)
