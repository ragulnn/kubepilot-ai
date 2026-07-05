from remediation_engine.rollback import RollbackEngine

engine = RollbackEngine()

result = engine.rollback(

    "payment-service"

)

print(result)
