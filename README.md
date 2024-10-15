<img src="./images/badge.png?raw=true" width="128">
<div align="left">
  
[![view - Documentation](https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge)](../../wiki/ "Go to project documentation")

</div>

# OttoUpdater
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

# Examples
https://github.com/palmmc/VanillaFormWrapper/blob/983789c715c7f4846b5ea77b963a14a33cd965c6/Examples/action_form.py
https://github.com/palmmc/VanillaFormWrapper/blob/983789c715c7f4846b5ea77b963a14a33cd965c6/Examples/modal_form.py
https://github.com/palmmc/VanillaFormWrapper/blob/983789c715c7f4846b5ea77b963a14a33cd965c6/Examples/message_form.py


If you experience any issues or have a suggestion, please create an [Issue](../../issues), and I'll try to get to it when I can!
