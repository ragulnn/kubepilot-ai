class IncidentRanking:

    def rank(self, incidents):

        incidents.sort(

            key=lambda x: (

                x["score"],

                x["incident"]["confidence"],

            ),

            reverse=True,

        )

        return incidents
