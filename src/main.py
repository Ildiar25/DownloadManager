import flet as ft
from interface.dashboard import Dashboard


def main(page: ft.Page):
    # Window settings
    page.window.maximizable = False
    page.window.resizable = False
    page.window.width = 980
    page.window.height = 720
    page.padding = 0
    page.title = "Download Manager"

    # Main page design
    page.fonts = {
        "MontserratR": r"fonts\Montserrat-Regular.ttf",
    }
    page.theme = ft.Theme(font_family="MontserratR", color_scheme_seed=ft.Colors.TEAL)
    page.theme_mode = ft.ThemeMode.DARK

    page.add(Dashboard(page))


if __name__ == '__main__':
    ft.app(main)
