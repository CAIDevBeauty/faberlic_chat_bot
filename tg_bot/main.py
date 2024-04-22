import os

from dff.context_storages import context_storage_factory
from dff.messengers.telegram import PollingTelegramInterface
from dff.pipeline import Pipeline
from dialog_graph import script


def get_pipeline() -> Pipeline:
    telegram_token = os.getenv("TG_BOT_TOKEN")

    db_uri = "postgresql+asyncpg://{}:{}@0.0.0.0:5432/{}".format(
        os.environ["POSTGRES_USERNAME"],
        os.environ["POSTGRES_PASSWORD"],
        os.environ["POSTGRES_DB"],
    )
    db = context_storage_factory(db_uri)


    if telegram_token:
        messenger_interface = PollingTelegramInterface(token=telegram_token)

    else:
        raise RuntimeError(
            "Telegram token (`TG_BOT_TOKEN`) is not set. `TG_BOT_TOKEN` can be set via `.env` file."
            " For more info see README.md."
        )

    pipeline = Pipeline.from_script(
        script=script.script,
        start_label=("general_flow", "start_node"),
        fallback_label=("general_flow", "fallback_node"),
        messenger_interface=messenger_interface,
        context_storage=db
    )

    return pipeline


if __name__ == "__main__":
    pipeline = get_pipeline()
    pipeline.run()
