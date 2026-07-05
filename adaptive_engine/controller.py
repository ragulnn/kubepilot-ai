from adaptive_engine.state import InvestigationState
from adaptive_engine.evaluator import ConfidenceEvaluator

from planning_engine.executor import InvestigationExecutor

from analysis_engine.incremental_analyzer import IncrementalAnalyzer


class InvestigationController:

    def __init__(self):

        self.state = InvestigationState()

        self.executor = InvestigationExecutor()

        self.evaluator = ConfidenceEvaluator()

        self.incremental = IncrementalAnalyzer()

    # --------------------------------------------------

    def next(
        self,
        question,
    ):

        return self.executor.execute(

            question,

            self.state.confidence,

            self.state.collected,

        )

    # --------------------------------------------------

    def feedback(
        self,
        evidence,
        state,
    ):

        # Record collected evidence
        self.state.add(
            evidence
        )

        specialists = []

        # -----------------------------
        # Prometheus
        # -----------------------------
        if "prometheus_ai" in state:

            result = state["prometheus_ai"]

            if hasattr(result, "__dict__"):
                specialists.append(result.__dict__)
            else:
                specialists.append(result)

        # -----------------------------
        # Loki
        # -----------------------------
        if "loki_ai" in state:

            result = state["loki_ai"]

            if hasattr(result, "__dict__"):
                specialists.append(result.__dict__)
            else:
                specialists.append(result)

        # -----------------------------
        # Tempo
        # -----------------------------
        if "tempo_ai" in state:

            result = state["tempo_ai"]

            if hasattr(result, "__dict__"):
                specialists.append(result.__dict__)
            else:
                specialists.append(result)

        # -----------------------------
        # Kubernetes
        # -----------------------------
        if "kubernetes_ai" in state:

            result = state["kubernetes_ai"]

            if hasattr(result, "__dict__"):
                specialists.append(result.__dict__)
            else:
                specialists.append(result)

        # -----------------------------
        # Incremental Analysis
        # -----------------------------
        analysis = self.incremental.analyze(
            specialists
        )

        self.state.confidence = analysis.get(
            "confidence",
            0.0,
        )

        self.state.completed = (

            self.state.confidence >= 0.90

        )

        return analysis
