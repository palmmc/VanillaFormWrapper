from endstone._internal.endstone_python import Player
from ..form_wrapper import (
    ModalFormData,
    ModalFormResponse,
)


def example_modal_form(player: Player):
    form = ModalFormData()
    options = ["Option 1", "Option 2", "Option 3"]
    form.title("Test Form")
    form.dropdown("Test Dropdown", options)
    form.slider("Test Slider", 0, 100, 1)
    form.text_field("Test Text Field", "Enter text here")
    form.toggle("Test Toggle", False)
    form.submit_button("Booger")

    def submit(player: Player, response: ModalFormResponse):
        if response.canceled:
            player.send_message("§cForm canceled.")
            return
        else:
            player.send_message("§aDropdown: §f" + options[response.formValues[0]])
            player.send_message("§aSlider: §f" + str(response.formValues[1]))
            player.send_message("§aText Field: §f" + response.formValues[2])
            player.send_message("§aToggle: §f" + str(response.formValues[3]))
            return

    form.show(player).then(
        lambda player=Player, response=ModalFormResponse: submit(player, response)
    )
