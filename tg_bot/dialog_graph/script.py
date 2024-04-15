import dff.script.conditions as cnd
from dff.script import RESPONSE, TRANSITIONS, Message, LOCAL, PRE_TRANSITIONS_PROCESSING


from dialog_graph import conditions as loc_cnd
from dialog_graph import response as loc_rsp
from dialog_graph import processing as loc_prc
from dialog_graph.fallbacks import fallback_response

script = {
    "general_flow": {
        "general_flow": {
            LOCAL: {
                TRANSITIONS: {
                    ("form_flow", "ask_item", 1.0): cnd.any(
                        [loc_cnd.has_intent(["shopping_list", "transfer"]), cnd.regexp(r"\border\b|\bpurchase\b")]
                    ),
                    ("chitchat_flow", "init_chitchat", 0.8): cnd.true(),
                },
                PRE_TRANSITIONS_PROCESSING: {"1": loc_prc.extract_intents()},
            },
        "start_node": {
            RESPONSE: Message(),  # the response of the initial node is skipped
            TRANSITIONS: {
                ("general_flow", "greeting_node"): cnd.exact_match(Message("/start")),
            },
        },
        "fallback_node": {
            RESPONSE: fallback_response,
            TRANSITIONS: {
                ("general_flow", "greeting_node"): cnd.true(),
            },
        },
    },
    "chat_flow": {
        LOCAL: {
            PRE_TRANSITIONS_PROCESSING: {"1": loc_prc.clear_intents(), "2": loc_prc.extract_intents()},
        "init_chat": {
            RESPONSE: Message(text="Вас приветствует бот-консультант Фаберлик!"),
            TRANSITIONS: {("chat_flow", "chat", 0.8): cnd.true()},
        },
        "chat": {

        }

    }
}
