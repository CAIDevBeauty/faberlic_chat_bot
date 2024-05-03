
from dff.messengers.telegram import TelegramMessage
from dff.script import PRE_TRANSITIONS_PROCESSING, RESPONSE, TRANSITIONS, Message
from dff.script import conditions as cnd

from . import conditions as loc_cnd
from . import processing as loc_prc
from .responses import get_welcome_text

script = {
    "general_flow": {
        "start_node": {
            TRANSITIONS: {
                ("general_flow", "welcome_node"): cnd.exact_match(TelegramMessage("/start")),
            }
        },
        "welcome_node": {
            RESPONSE: get_welcome_text,
            TRANSITIONS: {
                ("product_flow", "search_node"): loc_cnd.has_intent(["покупка товара"]),
                ("faq_flow", "question_node"): cnd.negation(loc_cnd.has_intent(["покупка товара"])),
            },
        },
        "fallback_node": {
            RESPONSE: Message("Не получается распознать запрос"),
        },
    },
    "product_flow": {
        "search_node": {
            RESPONSE: Message("Я что-то нашел"),
            TRANSITIONS: {
                ("product_flow", "search_node"): loc_cnd.has_intent(["покупка товара"]),
                ("faq_flow", "question_node"): cnd.negation(loc_cnd.has_intent(["покупка товара"])),
            },
        }
    },
    "faq_flow": {
        "question_node": {
            RESPONSE: Message("я отвечаю на faq"),
            TRANSITIONS: {
                ("product_flow", "search_node"): loc_cnd.has_intent(["покупка товара"]),
                ("faq_flow", "question_node"): cnd.negation(loc_cnd.has_intent(["покупка товара"])),
            },
        }
    },
}
