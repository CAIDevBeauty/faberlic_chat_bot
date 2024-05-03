from typing import Callable

from dff.pipeline import Pipeline
from dff.script import Context

from . import consts


def has_intent(labels: list) -> Callable:
    def has_intent_inner(ctx: Context, _: Pipeline) -> bool:
        if ctx.validation:
            return False
        return any([label in ctx.misc.get(consts.INTENTS, []) for label in labels])

    return has_intent_inner


def is_slots_full() -> Callable:
    def is_slots_full_inner(ctx: Context, _: Pipeline) -> bool:
        expected_slots = ["sex", "product_type", "action", "hair_type", "is_cheap"]
        if ctx.validation:
            return False
        return all(
            [slot in ctx.misc[consts.SLOTS] and ctx.misc[consts.SLOTS].get(slot) is not None for slot in expected_slots]
        )

    return is_slots_full_inner
