from agent.knowledge_graph import KnowledgeGraph


class GraphBuilder:

    def build(

        self,

        graph: KnowledgeGraph,

        evidence_list,

    ):

        for evidence in evidence_list:

            graph.add_node(

                evidence.type,

                evidence.resource,

                {

                    "status": evidence.value,

                    "namespace": evidence.namespace,

                },

            )

        return graph
