from report_engine.report import InvestigationReport


class ReportGenerator:

    def generate(

        self,

        analysis,

        evidence,

    ):

        sources = []

        for item in evidence:

            source = getattr(

                item,

                "source",

                "unknown",

            )

            if source not in sources:

                sources.append(source)

        return InvestigationReport(

            root_cause=analysis.get(

                "root_cause",

                "Unknown",

            ),

            confidence=analysis.get(

                "confidence",

                0.0,

            ),

            evidence=analysis.get(

                "evidence",

                [],

            ),

            recommended_fix=analysis.get(

                "recommended_fix",

                [],

            ),

            sources=sources,

        )
