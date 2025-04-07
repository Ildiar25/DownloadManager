import flet as ft


class Dashboard(ft.Container):
	def __init__(self, page: ft.Page) -> None:
		super().__init__()

		self.page = page