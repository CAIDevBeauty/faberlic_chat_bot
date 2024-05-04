from collections import defaultdict

from dff.pipeline import Pipeline
from dff.script import Context

from api import faq, intents, search, slots

from . import consts


def extract_intents():
    """
    Extract intents .
    """

    def extract_intents_inner(ctx: Context, _: Pipeline) -> Context:
        ctx.misc[consts.INTENTS].append(intents.get_intents(ctx.last_request))
        return ctx

    return extract_intents_inner


def clear_intents():
    """
    Clear intents container.
    """

    def clear_intents_inner(ctx: Context, _: Pipeline) -> Context:
        ctx.misc[consts.INTENTS] = []
        return ctx

    return clear_intents_inner


def search_product():
    def search_product_inner(ctx: Context, _: Pipeline) -> Context:
        search_params = ctx.misc[consts.SLOTS]
        ctx.misc[consts.SEARCH_RESULT] = search.search_products(ctx.last_request, search_params)
        return ctx

    return search_product_inner


def search_faq():
    def search_faq_inner(ctx: Context, _: Pipeline) -> Context:
        ctx.misc[consts.FAQ_RESULT] = faq.get_faq_answer(ctx.last_request)
        return ctx

    return search_faq_inner


def extract_slots():
    def extract_slots_inner(ctx: Context, _: Pipeline) -> Context:
        recognized_slots = slots.get_slots(ctx.last_request)
        if not ctx.misc.get(consts.SLOTS):
            ctx.misc[consts.SLOTS] = defaultdict()
        if recognized_slots:
            for slot_key, slot_value in recognized_slots.items():
                if ctx.misc[consts.SLOTS].get(slot_key) is None:
                    ctx.misc[consts.SLOTS][slot_key] = slot_value
        return ctx

    return extract_slots_inner


def clear_faq():
    """
    Clear intents container.
    """

    def clear_faq_inner(ctx: Context, _: Pipeline) -> Context:
        ctx.misc[consts.FAQ_RESULT] = []
        return ctx

    return clear_faq_inner


def clear_search():
    def search_product_inner(ctx: Context, _: Pipeline) -> Context:
        ctx.misc[consts.SEARCH_RESULT] = []
        return ctx

    return search_product_inner


def clear_slots():
    """
    Clear slots container.
    """

    def clear_slots_inner(ctx: Context, _: Pipeline) -> Context:
        ctx.misc[consts.SLOTS] = {
            "hair_type": None,
            "product_type": None,
            "is_cheap": None,
            "action": None,
            "sex": None,
        }
        return ctx

    return clear_slots_inner
