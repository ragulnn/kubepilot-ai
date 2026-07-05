class ReportFormatter:

    def format(

        self,

        report,

    ):

        lines = []

        lines.append("=" * 60)
        lines.append("KUBEPILOT AI INVESTIGATION REPORT")
        lines.append("=" * 60)

        lines.append("")
        lines.append("Root Cause")
        lines.append("-" * 20)
        lines.append(report.root_cause)

        lines.append("")
        lines.append("Confidence")
        lines.append("-" * 20)
        lines.append(f"{report.confidence:.2f}")

        lines.append("")
        lines.append("Evidence")
        lines.append("-" * 20)

        for item in report.evidence:

            lines.append(f"✓ {item}")

        lines.append("")
        lines.append("Recommended Fixes")
        lines.append("-" * 20)

        for item in report.recommended_fix:

            lines.append(f"• {item}")

        lines.append("")
        lines.append("Sources")
        lines.append("-" * 20)

        for source in report.sources:

            lines.append(f"• {source}")

        return "\n".join(lines)
