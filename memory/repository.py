import json
import os

from memory.incident import Incident


class IncidentRepository:

    def __init__(self):

        self.path = "memory/storage.json"

    def save(self, incident: Incident):

        incidents = self.load()

        incidents.append(incident.__dict__)

        with open(self.path, "w") as f:

            json.dump(

                incidents,

                f,

                indent=4,

            )

    def load(self):

        if not os.path.exists(

            self.path

        ):

            return []

        with open(self.path) as f:

            try:

                return json.load(f)

            except:

                return []
  
