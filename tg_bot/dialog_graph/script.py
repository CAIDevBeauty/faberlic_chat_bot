from dff.script import TRANSITIONS, RESPONSE, Message
import dff.script.conditions as cnd
from fallbacks import fallback_response
script = {
    "greeting_flow": {
        "start_node": {
            RESPONSE: Message(),  # the response of the initial node is skipped
            TRANSITIONS: {
                ("greeting_flow", "greeting_node"):
                    cnd.exact_match(Message("/start")),
            },
            "greeting_node": {
                RESPONSE: Message("Вас приветствует бот-консультант Фаберлик!"),
                #todo: трансмишн
            },
            "fallback_node": {
                RESPONSE: fallback_response,
                TRANSITIONS: {
                    ("greeting_flow", "greeting_node"): cnd.true(),
                },
            },
        },
        },


}
