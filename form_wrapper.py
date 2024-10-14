from endstone._internal.endstone_python import ActionForm, Player


class ActionFormResponse:
    def __init__(self, canceled: bool, selection: str):
        self.canceled = canceled
        self.selection = selection


class ActionFormData:
    def __init__(self):
        self._form = ActionForm()

    def body(self, body_text: str):
        """
        Method that sets the body text for the modal form.

        :param body_text: The body text to set.
        """
        self._form.content = body_text
        return self

    def button(self, text: str, icon_path: str | None = None):
        """
        Adds a button to this form with an icon from a resource pack.

        :param text: The text to display on the button.
        """
        self._form.add_button(text, icon_path)
        return self

    def show(self, player: Player):
        """
        Creates and shows this modal popup form. Returns asynchronously when the player confirms or cancels the dialog.
        This function can't be called in read-only mode.

        :param player: Player to show this dialog to.
        :raises: This function can throw errors.
        """
        self._form.on_submit = lambda p=Player, r=int: self.__form_submit(
            p, r, result=ActionFormResponse(False, r)
        )
        self._form.on_close = lambda p=Player: self.__form_submit(
            p, 0, result=ActionFormResponse(True, None)
        )
        player.send_form(self._form)
        return self

    def then(self, callback):
        """
        Sets the callback to be called on form submission.

        :param callback: Callback function to be called on form submission.
        """
        self._callback = callback
        return self

    def title(self, title_text: str):
        """
        This builder method sets the title for the modal dialog.

        :param title_text: The title text to set.
        """
        self._form.title = title_text
        return self

    def __form_submit(self, player: Player, i, result):
        """
        Private method to handle form submission.

        :param player: Player who submitted the form.
        :param result: Result of the form submission.
        """
        if self._callback:
            self._callback(player, result)
