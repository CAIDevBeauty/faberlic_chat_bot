import os

from dff import Context
from dff.context_storages import DBContextStorage, context_storage_factory
from dff.messengers.telegram import PollingTelegramInterface
from dff.pipeline import ACTOR, ExtraHandlerRuntimeInfo, Pipeline, Service
from dff.stats import (
    OtelInstrumentor,
    OTLPLogExporter,
    OTLPSpanExporter,
    default_extractors,
    set_logger_destination,
    set_tracer_destination,
)

from dialog_graph import script

# set_logger_destination(OTLPLogExporter(os.getenv("OTEL_URI"), insecure=True))
# set_tracer_destination(OTLPSpanExporter(os.getenv("OTEL_URI"), insecure=True))
# dff_instrumentor = OtelInstrumentor()
# dff_instrumentor.instrument()


# @dff_instrumentor
# async def get_service_state(ctx: Context, _, info: ExtraHandlerRuntimeInfo):
#     data = {
#         "execution_state": info.component.execution_state,
#     }
#     return data


def _get_db_storage_factory() -> DBContextStorage | None:
    postgres_user = os.getenv("POSTGRES_CONTEXT_USER")
    postgres_password = os.getenv("POSTGRES_CONTEXT_PASSWORD")
    postgres_host = os.getenv("POSTGRES_CONTEXT_HOST")
    postgres_port = os.getenv("POSTGRES_CONTEXT_PORT")
    postgres_db = os.getenv("POSTGRES_CONTEXT_DB")
    if not all([postgres_user, postgres_password, postgres_host, postgres_port, postgres_db]):
        return None
    db_uri = f"postgresql+asyncpg://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
    db = context_storage_factory(db_uri)
    return db


def get_pipeline(use_cli_interface: bool = False, use_context_storage=True) -> Pipeline:
    telegram_token = os.getenv("TG_BOT_TOKEN")
    if use_cli_interface:
        messenger_interface = None

    elif telegram_token:
        messenger_interface = PollingTelegramInterface(token=telegram_token)
    else:
        raise RuntimeError(
            "Telegram token (`TG_BOT_TOKEN`) is not set. `TG_BOT_TOKEN` can be set via `.env` file."
            " For more info see README.md."
        )

    pipeline = Pipeline.from_dict(
        {
            "script": script.script,
            "start_label": ("general_flow", "start_node"),
            "fallback_label": ("general_flow", "fallback_node"),
            "messenger_interface": messenger_interface,
            "context_storage": _get_db_storage_factory() if use_context_storage else {},
            "components": [
                ACTOR
                # Service(
                #     handler=ACTOR,
                #     before_handler=[
                #         default_extractors.get_timing_before,
                #     ],
                #     after_handler=[
                #         default_extractors.get_timing_after,
                #         default_extractors.get_current_label,
                #         default_extractors.get_last_request,
                #         default_extractors.get_last_response,
                #         get_service_state,
                #     ],
                # )
            ],
        },
    )
    return pipeline


if __name__ == "__main__":
    pipeline = get_pipeline(use_context_storage=False)
    pipeline.run()
