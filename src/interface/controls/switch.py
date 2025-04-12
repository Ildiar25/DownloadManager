from collections.abc import Callable

import flet as ft


class CustomSwitch(ft.Container):
	"""Creates a custom switch button with text name."""
	def __init__(
			self,
			title: str,
			width: int | None = None,
			expand: bool = False,
			on_change: Callable[[ft.ControlEvent], None] | None = None,
			value: bool = False
	) -> None:
		super().__init__()

		self.width = width
		self.expand = expand

		# Title
		self.title = ft.Text(
			title,
			size=14
		)

		# Actions
		self.switch = ft.Switch(
			value=value,
			width=36,
			on_change=on_change,
		)

		self.content = ft.Row(
			alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
			controls=[
				self.title,
				self.switch
			]
		)

	def get_value(self) -> bool:
		return self.switch.value

	def set_value(self, value: bool) -> None:
		self.switch.value = value
