from dff.messengers.telegram import TelegramMessage
from dff.script import (
    PRE_RESPONSE_PROCESSING,
    PRE_TRANSITIONS_PROCESSING,
    RESPONSE,
    TRANSITIONS,
    Message,
)
from dff.script import conditions as cnd

from . import conditions as loc_cnd
from . import processing as loc_prc
from . import responses as loc_rsp

script = {
    "general_flow": {
        "start_node": {
            TRANSITIONS: {
                ("general_flow", "welcome_node"): cnd.exact_match(TelegramMessage("/start")),
            }
        },
        "welcome_node": {
            PRE_TRANSITIONS_PROCESSING: {
                "1": loc_prc.clear_intents(),
                "2": loc_prc.extract_intents(),
                "3": loc_prc.clear_slots(),
                "4": loc_prc.extract_slots(),
            },
            RESPONSE: loc_rsp.get_welcome_text,
            TRANSITIONS: {
                ("product_flow", "search_node"): cnd.all(
                    [loc_cnd.has_intent(["покупка товара"]), loc_cnd.is_slots_full()]
                ),
                ("product_flow", "details_node"): cnd.all(
                    [loc_cnd.has_intent(["покупка товара"]), cnd.negation(loc_cnd.is_slots_full())]
                ),
                ("faq_flow", "question_node"): cnd.negation(loc_cnd.has_intent(["покупка товара"])),
            },
        },
        "fallback_node": {
            RESPONSE: Message("Не получается распознать запрос"),
            TRANSITIONS: {("product_flow", "search_node"): cnd.true()},
        },
    },
    "product_flow": {
        "search_node": {
            PRE_TRANSITIONS_PROCESSING: {
                "1": loc_prc.clear_intents(),
                "2": loc_prc.extract_intents(),
                "3": loc_prc.clear_slots(),
                "4": loc_prc.extract_slots(),
            },
            PRE_RESPONSE_PROCESSING: {"1": loc_prc.clear_search(), "2": loc_prc.search_product()},
            RESPONSE: loc_rsp.get_search_result,
            TRANSITIONS: {
                ("product_flow", "search_node"): cnd.all(
                    [loc_cnd.has_intent(["покупка товара"]), loc_cnd.is_slots_full()]
                ),
                ("product_flow", "details_node"): cnd.all(
                    [loc_cnd.has_intent(["покупка товара"]), cnd.negation(loc_cnd.is_slots_full())]
                ),
                ("product_flow", "buy_node"): cnd.exact_match(TelegramMessage(callback_query="buy")),
                ("faq_flow", "question_node"): cnd.negation(loc_cnd.has_intent(["покупка товара"])),
            },
        },
        "details_node": {
            PRE_TRANSITIONS_PROCESSING: {
                "1": loc_prc.clear_intents(),
                "2": loc_prc.extract_intents(),
                "3": loc_prc.extract_slots(),
            },
            RESPONSE: loc_rsp.get_cannot_extract_all_slots_text,
            TRANSITIONS: {
                ("product_flow", "search_node"): cnd.all(
                    [loc_cnd.has_intent(["покупка товара"]), loc_cnd.is_slots_full()]
                ),
                ("product_flow", "details_node"): cnd.all(
                    [loc_cnd.has_intent(["покупка товара"]), cnd.negation(loc_cnd.is_slots_full())]
                ),
                ("faq_flow", "question_node"): cnd.negation(loc_cnd.has_intent(["покупка товара"])),
            },
        },
        "buy_node": {
            PRE_TRANSITIONS_PROCESSING: {
                "1": loc_prc.clear_intents(),
                "2": loc_prc.extract_intents(),
                "3": loc_prc.clear_slots(),
                "4": loc_prc.extract_slots(),
            },
            RESPONSE: TelegramMessage("Товар добавлен в корзину"),
            TRANSITIONS: {
                ("product_flow", "search_node"): cnd.all(
                    [loc_cnd.has_intent(["покупка товара"]), loc_cnd.is_slots_full()]
                ),
                ("product_flow", "details_node"): cnd.all(
                    [loc_cnd.has_intent(["покупка товара"]), cnd.negation(loc_cnd.is_slots_full())]
                ),
                ("faq_flow", "question_node"): cnd.negation(loc_cnd.has_intent(["покупка товара"])),
            },
        },
    },
    "faq_flow": {
        "question_node": {
            PRE_TRANSITIONS_PROCESSING: {
                "1": loc_prc.clear_intents(),
                "2": loc_prc.extract_intents(),
                "3": loc_prc.clear_slots(),
                "4": loc_prc.extract_slots(),
            },
            PRE_RESPONSE_PROCESSING: {"1": loc_prc.clear_faq(), "2": loc_prc.search_faq()},
            RESPONSE: loc_rsp.get_faq_result,
            TRANSITIONS: {
                ("product_flow", "search_node"): cnd.all(
                    [loc_cnd.has_intent(["покупка товара"]), loc_cnd.is_slots_full()]
                ),
                ("product_flow", "details_node"): cnd.all(
                    [loc_cnd.has_intent(["покупка товара"]), cnd.negation(loc_cnd.is_slots_full())]
                ),
                ("faq_flow", "question_node"): cnd.negation(loc_cnd.has_intent(["покупка товара"])),
            },
        }
    },
}
