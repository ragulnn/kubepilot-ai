from adaptive_engine.controller import InvestigationController

from agents.default_registry import registry

from agent_bus.bus import AgentBus

from analysis_engine.incremental_analyzer import IncrementalAnalyzer


class AdaptivePipeline:

    def __init__(self):

        self.bus = AgentBus()

        self.controller = InvestigationController()

        self.incremental = IncrementalAnalyzer()

        for name in registry.list():

            agent = registry.get(name)

            if agent:

                agent.bus = self.bus

    def run(self, state):

        # ==========================================================
        # Publish Question
        # ==========================================================

        self.bus.publish(
            "question",
            state["question"],
        )

        # ==========================================================
        # Planner
        # ==========================================================

        planner = registry.get("planner")

        state = planner.run(state)

        # ==========================================================
        # Discovery
        # ==========================================================

        discovery = registry.get("discovery")

        state = discovery.run(state)

        workflow = state.get("workflow")

        if workflow:

            self.bus.publish(
                "workflow",
                workflow,
            )

        # ==========================================================
        # Investigation Loop
        # ==========================================================

        specialist_results = []

        while True:

            plan = self.controller.next(
                state["question"]
            )

            print()
            print("=" * 60)
            print("Adaptive Planner")
            print("=" * 60)
            print(plan)

            if plan.get("completed"):

                break

            capability = plan.get("next")

            if capability is None:

                break

            agents = registry.by_capability(
                capability
            )

            if not agents:

                print()
                print(f"No agent for {capability}")

                self.controller.feedback(
                    capability,
                    {
                        "confidence": 0.0,
                    },
                )

                continue

            specialist = agents[0]

            print()
            print(f"Running {specialist.name}")

            # ------------------------------------------
            # Execute Specialist
            # ------------------------------------------

            state = specialist.run(state)

            # ------------------------------------------
            # Collect Result
            # ------------------------------------------

            key = f"{specialist.name}_result"

            result = self.bus.get(key)

            if result:

                specialist_results.append(result)

            # ------------------------------------------
            # Planner Feedback Only
            # ------------------------------------------

            confidence = getattr(
                result,
                "confidence",
                0.0,
            ) if result else 0.0

            self.controller.feedback(

                capability,

                {
                    "confidence": confidence,
                },

            )

        # ==========================================================
        # Investigation Finished
        # ==========================================================

        print()
        print("=" * 60)
        print("Investigation Complete")
        print("=" * 60)

        state["specialist_results"] = specialist_results

        # ==========================================================
        # Aggregator
        # ==========================================================

        aggregator = registry.get("aggregator")

        if aggregator:

            state = aggregator.run(state)

        # ==========================================================
        # Incremental Analyzer
        # ==========================================================

        incremental = self.incremental.analyze(

            specialist_results

        )

        state["incremental"] = incremental

        self.bus.publish(

            "incremental",

            incremental,

        )

        # ==========================================================
        # AI Analyzer
        # ==========================================================

        analyzer = registry.get("analyzer")

        if analyzer:

            state = analyzer.run(state)

        # ==========================================================
        # Verification
        # ==========================================================

        verifier = registry.get("verification")

        if verifier:

            state = verifier.run(state)

        # ==========================================================
        # Memory
        # ==========================================================

        memory = registry.get("memory")

        if memory:

            state = memory.run(state)

        # ==========================================================
        # Knowledge
        # ==========================================================

        knowledge = registry.get("knowledge")

        if knowledge:

            state = knowledge.run(state)

        # ==========================================================
        # Remediation
        # ==========================================================

        remediation = registry.get("remediation")

        if remediation:

            state = remediation.run(state)

        # ==========================================================
        # Learning
        # ==========================================================

        learning = registry.get("learning")

        if learning:

            state = learning.run(state)

        # ==========================================================
        # Report
        # ==========================================================

        report = registry.get("report")

        if report:

            state = report.run(state)

        return state
