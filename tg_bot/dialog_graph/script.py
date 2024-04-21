
from dff.script import conditions as cnd, PRE_TRANSITIONS_PROCESSING, LOCAL
from dff.script import RESPONSE, TRANSITIONS, Message
from dff.messengers.telegram import TelegramMessage
from . import conditions as loc_cnd
from dff.script import labels as lbl
from . import processing as loc_prc

script = {
    "general_flow": {
        "start_node": {
            TRANSITIONS: {("chat_flow", "greeting_node"): cnd.exact_match(TelegramMessage(text="/start"))},
        },
        "fallback_node": {
            RESPONSE: Message("Не получается распознать запрос"),
        },
    },
    "chat_flow": {
        "greeting_node": {
            RESPONSE: TelegramMessage(text="Вас приветствует бот-консультант Фаберлик! Я отвечу на любой ваш вопрос или помогу сделать заказ"),
            PRE_TRANSITIONS_PROCESSING: {"1": loc_prc.clear_intents(), "2": loc_prc.clear_slots(),  "3": loc_prc.extract_intents()},
            TRANSITIONS: {
                ("chat_flow", "chat_node", 0.8): loc_cnd.has_intent(["purchase"]),
                ("chat_flow", "faq_node", 1.2):  loc_cnd.has_intent(["registration", "payment", 'receipt', 'cancel', 'return'])
            },
        },
        "chat_node":{
            PRE_TRANSITIONS_PROCESSING: {"1": loc_prc.extract_intents()},
            TRANSITIONS: {
                ("chat_flow", "buy_node", 1.0): loc_cnd.is_slots_full(['hair_type', 'product_type', 'price', 'problem']),
                lbl.repeat(0.8): cnd.true()
            }
        },
        "buy_node":{
            RESPONSE: Message("Покупка совершена!")
        },
    }
}
