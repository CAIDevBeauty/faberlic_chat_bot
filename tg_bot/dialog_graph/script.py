import re

from dff.messengers.telegram import TelegramMessage
from dff.script import PRE_TRANSITIONS_PROCESSING, RESPONSE, TRANSITIONS, Message
from dff.script import conditions as cnd

from . import conditions as loc_cnd
from . import processing as loc_prc
from .responses import get_cannot_extract_all_slots_text, get_welcome_text

script = {
    "general_flow": {
        "start_node": {TRANSITIONS: {("chat_flow", "intro_node"): cnd.exact_match(TelegramMessage("/start"))}},
        "fallback_node": {
            RESPONSE: Message("Не получается распознать запрос"),
            TRANSITIONS: {("general_flow", "start_node"): cnd.true()},
        },
    },
    "chat_flow": {
        "intro_node": {
            RESPONSE: get_welcome_text,
            PRE_TRANSITIONS_PROCESSING: {
                "1": loc_prc.clear_intents(),
                "2": loc_prc.clear_slots(),
                "3": loc_prc.extract_intents(),
                "4": loc_prc.extract_slots(),
            },
            TRANSITIONS: {
                ("chat_flow", "search_node"): cnd.all(
                    [
                        loc_cnd.has_intent(["purchase of goods"]),
                        loc_cnd.is_slots_full(["hair_type", "product_type", "price", "series"]),
                    ]
                ),
                ("chat_flow", "details_node"): cnd.all(
                    [
                        loc_cnd.has_intent(["purchase of goods"]),
                        cnd.negation(loc_cnd.is_slots_full(["hair_type", "product_type", "price", "series"])),
                    ]
                ),
                ("chat_flow", "faq_node"): cnd.negation(loc_cnd.has_intent(["purchase_of_goods"])),
                ("general_flow", "fallback_node"): cnd.true(),
            },
        },
        "details_node": {
            RESPONSE: get_cannot_extract_all_slots_text,
            PRE_TRANSITIONS_PROCESSING: {"1": loc_prc.extract_slots()},
            TRANSITIONS: {
                ("chat_flow", "search_node"): loc_cnd.is_slots_full(["hair_type", "product_type", "price", "series"]),
                ("chat_flow", "details_node"): cnd.true(),
            },
        },
        "search_node": {
            RESPONSE: Message("Мы тут что-то нашли, брать будете или еще поищете?"),
            TRANSITIONS: {
                ("chat_flow", "buy_node"): cnd.regexp(r"да", re.IGNORECASE),
                ("chat_flow", "intro_node"): cnd.regexp(r"нет", re.IGNORECASE),
            },
        },
        "buy_node": {
            RESPONSE: Message("Покупка совершена!"),
            TRANSITIONS: {("chat_flow", "intro_node"): cnd.true()},
        },
        "faq_node": {RESPONSE: Message("Ответ на все сущее - 42")},
    },
}
