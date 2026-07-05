from analysis_engine.rule_loader import RuleLoader

loader = RuleLoader()

rules = loader.load()

print()

for rule in rules:

    print(rule["name"])

    print(rule["conditions"])

    print()
