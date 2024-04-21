from typing import Callable

from dff.script import Context
from dff.pipeline import Pipeline

from . import consts


def has_intent(labels: list) -> Callable:
    def has_intent_inner(ctx: Context, _: Pipeline) -> bool:
        if ctx.validation:
            return False
        return any([label in ctx.misc.get(consts.INTENTS, []) for label in labels])

    return has_intent_inner

def is_slots_full(slots) -> Callable:
    def is_slots_full_inner(ctx: Context, _: Pipeline) -> bool:
        if ctx.validation:
            return False
        return all([slot in ctx.misc[consts.SLOTS] for slot in slots])
    return  is_slots_full_inner


