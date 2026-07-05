from memory.search import IncidentSearch

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

for match in matches:

    print(match)
