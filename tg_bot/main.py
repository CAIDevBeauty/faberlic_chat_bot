import os

from dff.messengers.telegram import PollingTelegramInterface
from dff.pipeline import ACTOR, Pipeline, Service
from dff.stats import default_extractors

from context import get_db_storage_factory
from dialog_graph import script
from telemetry import get_service_state


def get_pipeline(use_cli_interface: bool = False, use_context_storage=True, use_telemetry=True) -> Pipeline:
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
    if not use_telemetry:
        components = [ACTOR]
    else:
        components = (
            [
                Service(
                    handler=ACTOR,
                    before_handler=[
                        default_extractors.get_timing_before,
                    ],
                    after_handler=[
                        default_extractors.get_timing_after,
                        default_extractors.get_current_label,
                        default_extractors.get_last_request,
                        default_extractors.get_last_response,
                        get_service_state,
                    ],
                )
            ],
        )

    pipeline = Pipeline.from_dict(
        {
            "script": script.script,
            "start_label": ("general_flow", "start_node"),
            "fallback_label": ("general_flow", "fallback_node"),
            "messenger_interface": messenger_interface,
            "context_storage": get_db_storage_factory() if use_context_storage else {},
            "components": [ACTOR],
        },
    )
    return pipeline


if __name__ == "__main__":
    pipeline = get_pipeline()
    pipeline.run()
