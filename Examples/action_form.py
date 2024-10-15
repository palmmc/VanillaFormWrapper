from endstone._internal.endstone_python import Player
from ..form_wrapper import (
    ActionFormData,
    ActionFormResponse,
)


def example_action_form(player: Player):
    form = ActionFormData()
    form.title("Test Form")
    form.body("This is a test form.")
    form.button("Test", "textures/ui/refresh_light")
    form.button("Test 2", "textures/ui/anvil_icon")
    form.button("Test 3", "textures/ui/refresh_light")

    def submit(player: Player, result: ActionFormResponse):
        if result.canceled:
            player.send_message("§cForm canceled.")
            return
        else:
            player.send_message(f"§aForm result: §f{result.selection}")
            return

    form.show(player).then(
        lambda player=Player, result=ActionFormResponse: submit(player, result)
    )
