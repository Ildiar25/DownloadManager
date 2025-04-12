from pathlib import Path

import flet as ft

from .e_button import ButtonStyle, CustomElevatedButton
from .snackbar import Snackbar, SnackbarStyle
from .switch import CustomSwitch


class AppBar(ft.AppBar):
	def __init__(self, page: ft.Page, snackbar: Snackbar) -> None:
		super().__init__()

		# General settings
		self.page = page
		self.snackbar = snackbar

		# Appbar settings
		self.__toolbar_height = 40
		self.__folder_picker_dialog = ft.FilePicker(on_result=self.__select_new_folder)
		self.page.overlay.append(self.__folder_picker_dialog)

		# Appbar elements
		self.switch = CustomSwitch(title="Monitorear", expand=True)
		self.path = ft.Text(value=str(Path.home()), style=ft.TextStyle(size=12))
		self.__path_container = ft.Container(
			bgcolor="#161D1C",
			padding=ft.padding.symmetric(horizontal=16, vertical=4),
			border_radius=40,
			expand=True,
			content=ft.Row(
				spacing=8,
				controls=[
					ft.Icon(ft.Icons.FOLDER_OFF_ROUNDED, size=20),
					self.path,
				]
			)
		)

		# Leading
		self.leading_width = 162
		self.leading = ft.Container(
			padding=ft.padding.only(left=32, right=16),
			content=self.switch
		)

		# Path bar
		self.center_title = True
		self.title = self.__path_container

		# Actions
		self.actions = [
			ft.Container(
				padding=ft.padding.only(left=16, right=32),
				content=CustomElevatedButton(
					name="Seleccionar Carpeta",
					style=ButtonStyle.DEFAULT,
					on_click=lambda _: self.__folder_picker_dialog.get_directory_path(
						initial_directory=str(Path.home())
					)
				)
			)
		]

	def __select_new_folder(self, event: ft.FilePickerResultEvent) -> None:
		self.path.value = event.path
		self.__path_container.update()
