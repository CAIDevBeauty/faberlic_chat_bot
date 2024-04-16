import re
from string import punctuation
from dff.script import Context
from dff.pipeline import Pipeline
from api import intents, slots
from . import consts


def extract_intents():
    """
    Extract intents .
    """

    def extract_intents_inner(ctx: Context, _: Pipeline) -> Context:
        ctx.misc[consts.INTENTS] = intents.get_intents(ctx.last_request)
        return ctx

    return extract_intents_inner

# def extract_slots():
#     def extract_slots_inner(ctx: Context, _: Pipeline) -> Context:
#         recognized_slots =  slots.get_slots(ctx.last_request)
#         for slot in recognized_slots.items():
#             ctx.misc[consts.SLOTS][slot['name']] = slot['value']
#         return ctx
#     return extract_slots_inner


def clear_intents():
    """
    Clear intents container.
    """

    def clear_intents_inner(ctx: Context, _: Pipeline) -> Context:
        ctx.misc[consts.INTENTS] = []
        return ctx

    return clear_intents_inner


def clear_slots():
    """
    Clear slots container.
    """

    def clear_slots_inner(ctx: Context, _: Pipeline) -> Context:
        ctx.misc[consts.SLOTS] = {}
        return ctx

    return clear_slots_inner

