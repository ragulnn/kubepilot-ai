from expansion_engine.expander import ExpansionEngine

engine = ExpansionEngine()

requests = engine.expand(

    {

        "kind": "Pod",

        "namespace": "default",

        "name": "nginx",

    }

)

print()

for request in requests:

    print(request)
