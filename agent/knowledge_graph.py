class KnowledgeGraph:

    def __init__(self):

        self.nodes = {}

        self.edges = []

    def add_node(self, node_type, name, data=None):

        key = f"{node_type}:{name}"

        if key not in self.nodes:

            self.nodes[key] = {

                "type": node_type,

                "name": name,

                "data": data or {},

            }

        return key

    def add_edge(self, source, relation, target):

        self.edges.append({

            "source": source,

            "relation": relation,

            "target": target,

        })

    def get_node(self, node_type, name):

        return self.nodes.get(

            f"{node_type}:{name}"

        )



    def summary(self):

           node_types = {}

           for node in self.nodes.values():

               t = node["type"]

               node_types[t] = node_types.get(t, 0) + 1

           return {

                "nodes": len(self.nodes),

                "edges": len(self.edges),

                "types": node_types,

    }            


    def print_graph(self):

        print("\nKnowledge Graph")

        for edge in self.edges:

            print(

                f"{edge['source']}"

                f" --{edge['relation']}--> "

                f"{edge['target']}"

            )

