from analysis_engine.incremental_analyzer import IncrementalAnalyzer

print("=" * 60)
print("Incremental Analyzer")
print("=" * 60)

results = [

    {

        "summary":"Memory pressure",

        "root_cause":"Memory",

        "confidence":0.52,

    },

    {

        "summary":"OOMKilled",

        "root_cause":"Memory Exhaustion",

        "confidence":0.81,

    },

]

analysis = IncrementalAnalyzer().analyze(

    results

)

print()

print(analysis)
