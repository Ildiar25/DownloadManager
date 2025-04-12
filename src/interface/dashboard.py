import flet as ft

from .controls import AppBar, Snackbar


class Dashboard(ft.Container):
	def __init__(self, page: ft.Page) -> None:
		super().__init__()

		# General settings
		self.page = page
		self.snackbar = Snackbar()


		self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
		self.selected_files = ft.TextField()

		self.page.overlay.append(self.pick_files_dialog)
		self.expand = True
		self.image = ft.DecorationImage(r"bg01.png", fit=ft.ImageFit.COVER)

		self.page.appbar = AppBar(self.page, self.snackbar)
		self.padding = ft.padding.all(32)

		self.content = ft.Row(
			spacing=16,
			expand=True,
			controls=[
				ft.Container(
					# blur=10,
					opacity=0.2,
					bgcolor=ft.Colors.TEAL_900,
					expand=True,
					content=ft.Column(
						expand=True,
						controls=[

						]
					)
				),
				ft.Container(
					# blur=10,
					opacity=0.2,
					bgcolor=ft.Colors.TEAL_900,
					expand=True,
					content=ft.Column(
						expand=True,
						controls=[

						]
					)
				),
			]
		)

	def pick_files_result(self, e: ft.FilePickerResultEvent):
		print(type(e.path), e.path)
		self.selected_files.value = (
			e.path
		)
		self.selected_files.update()

