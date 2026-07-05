class InvestigationContextBuilder:

    def build(

        self,

        question,

        evidence,

        diagnosis,

    ):

        lines = []

        lines.append(f"Question:\n{question}\n")

        lines.append("=" * 60)

        lines.append("Evidence")

        lines.append("=" * 60)

        for item in evidence:

            lines.append(

                f"""

Source : {item.source}

Category : {item.category}

Name : {item.name}

Value : {item.value}

"""
            )

        lines.append("=" * 60)

        lines.append("Rule Engine Diagnosis")

        lines.append("=" * 60)

        lines.append(

            str(diagnosis)

        )

        return "\n".join(lines)
