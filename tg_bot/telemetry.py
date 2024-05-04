import os

from dff import Context
from dff.pipeline import ExtraHandlerRuntimeInfo
from dff.stats import (
    OtelInstrumentor,
    OTLPLogExporter,
    OTLPSpanExporter,
    default_extractors,
    set_logger_destination,
    set_tracer_destination,
)

set_logger_destination(OTLPLogExporter(os.getenv("OTEL_URI"), insecure=True))
set_tracer_destination(OTLPSpanExporter(os.getenv("OTEL_URI"), insecure=True))
dff_instrumentor = OtelInstrumentor()
dff_instrumentor.instrument()


@dff_instrumentor
async def get_service_state(ctx: Context, _, info: ExtraHandlerRuntimeInfo):
    data = {
        "execution_state": info.component.execution_state,
    }
    return data
