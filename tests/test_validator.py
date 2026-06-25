from agent.validator import Validator

validator = Validator()

action = {
    "tool": "logs"
}

valid, error = validator.validate(action)

print(valid)
print(error)
