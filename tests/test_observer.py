from remediation_engine.observer import ObservationEngine

engine = ObservationEngine()

metrics = {

    "ready": True,

    "restarts": 0,

    "oomkilled": False,

}

result = engine.observe(

    metrics

)

print(result)
