import json


class RuleLoader:

    def __init__(self):

        with open(

            "knowledge_base/kubernetes_rules.json",

            "r",

        ) as f:

            self.rules = json.load(f)

    def load(self):

        return self.rules
