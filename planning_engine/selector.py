from planning_engine import strategies


class StrategySelector:

    def select(self, question):

        q = question.lower()

        if any(

            word in q

            for word in [

                "restart",

                "crash",

                "crashloop",

                "oom",

                "pod",

            ]

        ):

            return strategies.POD_CRASH

        if any(

            word in q

            for word in [

                "cpu",

                "throttle",

            ]

        ):

            return strategies.CPU

        if any(

            word in q

            for word in [

                "memory",

                "oomkilled",

            ]

        ):

            return strategies.MEMORY

        if any(

            word in q

            for word in [

                "network",

                "dns",

                "timeout",

                "connection",

            ]

        ):

            return strategies.NETWORK

        if any(

            word in q

            for word in [

                "imagepullbackoff",

                "image",

            ]

        ):

            return strategies.IMAGE

        return strategies.DEFAULT
