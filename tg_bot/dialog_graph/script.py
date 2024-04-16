
from dff.script import conditions as cnd, PRE_TRANSITIONS_PROCESSING
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
            PRE_TRANSITIONS_PROCESSING: {"1": loc_prc.clear_intents(), "2": loc_prc.extract_intents()},
            TRANSITIONS: {("chat_flow", "chat", 0.1): loc_cnd.has_intent(["purchase"])},
        },
        "chat":{
            PRE_TRANSITIONS_PROCESSING: {"1": loc_prc.extract_intents()},
            TRANSITIONS: {
                ("chat_flow", "buy_node", 0.2): loc_cnd.has_intent(['purchase']),
                lbl.repeat(0.1): cnd.true()
            }
        },
        "buy_node":{
            RESPONSE: Message("Покупка совершена!")
        }
    }
}
