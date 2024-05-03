from collections import defaultdict

from dff import Context, Pipeline
from loguru import logger

from api import intents, slots
from dialog_graph import consts


def get_nlu_info(ctx: Context, _: Pipeline):
    logger.info(ctx.last_request)
    if ctx.last_label != ('general_flow', 'start_node'):
        intent_class = intents.get_intents(ctx.last_request)
        logger.info(intent_class)
        ctx.misc[consts.INTENTS] = intent_class
        if intent_class == "покупка товара":
            recognized_slots = slots.get_slots(ctx.last_request)
            logger.info(recognized_slots)
            ctx.misc[consts.SLOTS] = defaultdict()
            for slot_key, slot_value in recognized_slots.items():
                if ctx.misc[consts.SLOTS].get(slot_key) is None:
                    ctx.misc[consts.SLOTS][slot_key] = slot_value
