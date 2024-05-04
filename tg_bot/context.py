import os

from dff.context_storages import DBContextStorage, context_storage_factory


def get_db_storage_factory() -> DBContextStorage | None:
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
