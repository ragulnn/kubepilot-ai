from fastapi import FastAPI
import time
import random

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

resource = Resource.create(
    {
        "service.name": "kubepilot-demo"
    }
)

provider = TracerProvider(resource=resource)

processor = BatchSpanProcessor(
    OTLPSpanExporter(
        endpoint="localhost:4317",
        insecure=True,
    )
)

provider.add_span_processor(processor)

trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

app = FastAPI()


@app.get("/")
def root():

    with tracer.start_as_current_span("homepage"):

        time.sleep(random.uniform(0.1, 0.5))

        return {"status": "ok"}


@app.get("/error")
def error():

    with tracer.start_as_current_span("error"):

        raise Exception("Demo failure")
