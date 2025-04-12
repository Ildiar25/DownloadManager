from enum import Enum

import flet as ft


class SnackbarStyle(Enum):
    DANGER = "danger"
    INFO = "info"
    RESET = "reset"
    SUCCESS = "success"
    WARNING = "warning"


class Snackbar(ft.SnackBar):
    """Creates a custom snackbar to display info based on their style."""
    def __init__(
            self,
            content: str = "",
            style: SnackbarStyle = SnackbarStyle.RESET
    ) -> None:
        super().__init__(ft.Text(content, text_align=ft.TextAlign.CENTER))

        # Sets style & Update
        self.style = style
        self.__update_appearance()

    def change_style(self, msg: str, style: SnackbarStyle) -> None:
        self.content.value = msg
        self.style = style
        self.__update_appearance()

    def __update_appearance(self) -> None:
        match self.style:
            case SnackbarStyle.INFO:
                self.bgcolor = None
                self.content.color = None
                self.open = True

            case SnackbarStyle.WARNING:
                self.bgcolor = None
                self.content.color = None
                self.open = True

            case SnackbarStyle.DANGER:
                self.bgcolor = None
                self.content.color = None
                self.open = True

            case SnackbarStyle.SUCCESS:
                self.bgcolor = None
                self.content.color = None
                self.open = True

            case SnackbarStyle.RESET:
                self.bgcolor = None
                self.content.value = ""
                self.open = False
