from remediation_engine.registry import SUPPORTED_ACTIONS
from remediation_engine.rules import (
    SUPPORTED_RESOURCES,
    REQUIRED_FIELDS,
)
from remediation_engine.result import ValidationResult


class ActionValidator:

    def validate(self, action):

        errors = []

        warnings = []

        # -------------------------
        # Required fields
        # -------------------------

        for field in REQUIRED_FIELDS:

            if not getattr(action, field, None):

                errors.append(

                    f"Missing field: {field}"

                )

        # -------------------------
        # Action
        # -------------------------

        if action.action not in SUPPORTED_ACTIONS:

            errors.append(

                f"Unsupported action: {action.action}"

            )

        # -------------------------
        # Resource Type
        # -------------------------

        if action.resource_type not in SUPPORTED_RESOURCES:

            errors.append(

                f"Unsupported resource: {action.resource_type}"

            )

        # -------------------------
        # Confidence
        # -------------------------

        if action.confidence < 0.70:

            warnings.append(

                "Low confidence remediation"

            )

        return ValidationResult(

            valid=len(errors) == 0,

            errors=errors,

            warnings=warnings,

        )
