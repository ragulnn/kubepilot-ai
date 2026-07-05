from models.specialist_result import SpecialistResult


class SpecialistAggregator:

    def aggregate(self, results):

        aggregated = {

            "sources": [],
            "summaries": [],
            "root_causes": [],
            "recommendations": [],
            "findings": [],
            "confidence": 0.0,

        }

        total_confidence = 0.0
        count = 0

        for result in results:

            if not isinstance(result, SpecialistResult):
                continue

            aggregated["sources"].append(result.source)

            aggregated["summaries"].append(result.summary)

            aggregated["root_causes"].append(result.root_cause)

            aggregated["recommendations"].extend(
                result.recommendations
            )

            aggregated["findings"].extend(
                result.findings
            )

            total_confidence += result.confidence

            count += 1

        # ----------------------------------
        # Average confidence
        # ----------------------------------

        if count:

            aggregated["confidence"] = round(
                total_confidence / count,
                2,
            )

        # ----------------------------------
        # Remove duplicate recommendations
        # ----------------------------------

        aggregated["recommendations"] = list(
            dict.fromkeys(
                aggregated["recommendations"]
            )
        )

        # ----------------------------------
        # Remove duplicate findings
        # Works for dicts and strings
        # ----------------------------------

        unique = []
        seen = set()

        for finding in aggregated["findings"]:

            if isinstance(finding, dict):

                key = tuple(sorted(finding.items()))

            else:

                key = finding

            if key in seen:
                continue

            seen.add(key)

            unique.append(finding)

        aggregated["findings"] = unique

        # ----------------------------------
        # Remove duplicate sources
        # ----------------------------------

        aggregated["sources"] = list(
            dict.fromkeys(
                aggregated["sources"]
            )
        )

        return aggregated
