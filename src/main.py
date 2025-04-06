import flet as ft
from interface.controls.appbar import AppBar
from shared.themes import EmeraldTheme


def main(page: ft.Page):
    # Window settings
    page.window.maximizable = False
    page.window.resizable = False
    page.window.width = 980
    page.window.height = 720
    page.title = "Download Manager"

    # Main page design
    page.fonts = {
        "MontserratR": r"fonts\Montserrat-Regular.ttf",
    }
    page.theme = EmeraldTheme("MontserratR")
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 8

    def pick_files_result(e: ft.FilePickerResultEvent):
        print(type(e.path), e.path)
        selected_files.value = (
            e.path
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.TextField()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Container(
            image=ft.DecorationImage(src="bg01.png", fit=ft.ImageFit.COVER),
            expand=True,
            padding=32,
            content=ft.Column(
                controls=[
                    ft.ElevatedButton(
                        "Styled button 1",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(2),

                        ),
                        on_click=lambda _: pick_files_dialog.get_directory_path()
                    ),
                    selected_files
                ]
            )
        )
    )


if __name__ == '__main__':
    ft.app(main)
