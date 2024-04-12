from dff import Context, Pipeline
from dff.script import Message


def fallback_response(ctx: Context, _: Pipeline) -> Message:
    """
    Generate a special fallback response depending on the situation.
    """
    if ctx.last_request is not None:
        if ctx.last_request.text != "/start" and ctx.last_label is None:
            # an empty last_label indicates start_node
            return Message("You should've started the dialog with '/start'")
        else:
            return Message(
                text=f"That was against the rules!\n"
                     f"You should've written 'Ping', not '{ctx.last_request.text}'!"
            )
    else:
        raise RuntimeError("Error occurred: last request is None!")