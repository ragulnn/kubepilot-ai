import json


class JSONSchemaParser:

    def parse(self, text):

        try:

            return json.loads(text)

        except Exception:

            return None
