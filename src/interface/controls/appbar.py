import flet as ft


class AppBar(ft.AppBar):
	def __init__(self) -> None:
		super().__init__()

		self.toolbar_height = 40
