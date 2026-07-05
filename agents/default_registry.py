from agents.registry import AgentRegistry

from agents.planner_agent import PlannerAgent
from agents.discovery_agent import DiscoveryAgent
from agents.evidence_agent import EvidenceAgent

from agents.prometheus_agent import PrometheusAgent
from agents.loki_agent import LokiAgent
from agents.tempo_agent import TempoAgent
from agents.kubernetes_agent import KubernetesAgent

from agents.aggregator_agent import AggregatorAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.memory_agent import MemoryAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.remediation_agent import RemediationAgent
from agents.verification_agent import VerificationAgent
from agents.learning_agent import LearningAgent

registry = AgentRegistry()

# Core
registry.register(
    PlannerAgent()
)

registry.register(
    DiscoveryAgent()
)

registry.register(
    EvidenceAgent()
)

# Specialists
registry.register(
    PrometheusAgent()
)

registry.register(
    LokiAgent()
)

registry.register(
    TempoAgent()
)

registry.register(
    KubernetesAgent()
)

# AI
registry.register(
    AggregatorAgent()
)

registry.register(
    AnalyzerAgent()
)

registry.register(
    VerificationAgent()
)

registry.register(
    MemoryAgent()
)

registry.register(
    KnowledgeAgent()
)

registry.register(
    RemediationAgent()
)
 
registry.register(
    LearningAgent()
)
