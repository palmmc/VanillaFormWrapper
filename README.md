<a href="../../"><img src="./images/badge.png?raw=true" width="128">
<div align="left">
  
[![view - Examples](https://img.shields.io/badge/view-Examples-purple?style=for-the-badge)](../../tree/main/Examples/ "Go to project documentation")

</div>

# VanillaFormWrapper
A wrapper for [Endstone](https://github.com/EndstoneMC/endstone) in python to mimic Vanilla ScriptAPI form UIs.

# Usage
1) Download the latest [release](../../releases).
2) Drop it into your plugin at the same level as your entry point script.
3) Add the following import to the top of your script:
   
   ```python
   from .form_wrapper import (
     ActionFormData,
     ActionFormResponse,
     ModalFormData,
     ModalFormResponse,
     MessageFormData,
     MessageFormResponse
   )
   ```
4) And you're done!

> Keep in mind that (due to the *language barrier*) this wrapper doesn't replicate vanilla forms 1:1.
>
> However, it will still make the form process feel a lot more familiar, and hopefully, easier to understand.

# Example

```python
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

```

# Issues

If you experience any issues or have a suggestion, please create an [Issue](../../issues), and I'll try to get to it when I can!
