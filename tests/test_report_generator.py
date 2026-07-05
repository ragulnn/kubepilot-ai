from report_engine.generator import ReportGenerator
from report_engine.formatter import ReportFormatter

analysis = {

    "root_cause": "Memory Exhaustion",

    "confidence": 0.96,

    "evidence": [

        "Memory usage reached 98%",

        "Restart count is 8",

        "OOMKilled detected",

        "Tempo trace contains exception",

    ],

    "recommended_fix": [

        "Increase memory limit",

        "Check for memory leak",

        "Restart deployment",

    ],

}


class MockResponse:

    def __init__(self, source):

        self.source = source


responses = [

    MockResponse("kubernetes"),

    MockResponse("prometheus"),

    MockResponse("loki"),

    MockResponse("tempo"),

]

generator = ReportGenerator()

report = generator.generate(

    analysis,

    responses,

)

formatter = ReportFormatter()

print()

print(

    formatter.format(

        report

    )

)
