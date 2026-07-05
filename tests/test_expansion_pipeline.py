from expansion_engine.pipeline import ExpansionPipeline

pipeline = ExpansionPipeline()

responses = pipeline.collect(

    {

        "kind": "Pod",

        "name": "nginx-7f8fbb96d-pt7cq",

        "namespace": "default",

    }

)

print()

for response in responses:

    print()

    print(response.source)

    print(response.success)

    print(response.message)

    print(response.evidence)
