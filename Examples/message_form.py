from endstone._internal.endstone_python import Player
from ..form_wrapper import (
    MessageFormData,
    MessageFormResponse,
)


def example_message_form(player: Player):
    form = MessageFormData()
    form.title("Test Form")
    form.body("This is a test form.")
    form.button1("Okay")
    form.button2("No Thanks")

    def submit(player: Player, response: MessageFormResponse):
        if response.canceled:
            player.send_message("§cForm canceled.")
            return
        else:
            if response.selection == 0:
                player.send_message("Okay")
            else:
                player.send_message("No Thanks")
            return

    form.show(player).then(
        lambda player=Player, response=MessageFormResponse: submit(player, response)
    )
