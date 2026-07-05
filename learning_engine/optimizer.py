class StrategyOptimizer:

    def optimize(self, statistics):

        ordered = sorted(

            statistics.items(),

            key=lambda x: x[1],

            reverse=True,

        )

        return [

            action

            for action, _ in ordered

        ]
