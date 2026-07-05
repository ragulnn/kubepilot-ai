from memory.search import IncidentSearch
from knowledge_base.engine import KnowledgeEngine

search = IncidentSearch()

current = {

    "question":"Why is nginx restarting?",

    "resource_name":"nginx",

    "namespace":"default",

    "root_cause":"Memory Exhaustion",

}

matches = search.find(

    current

)

knowledge = KnowledgeEngine().build(

    matches

)

print()

print(knowledge)
