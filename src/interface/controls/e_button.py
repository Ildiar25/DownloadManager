from collections.abc import Callable
from enum import Enum

import flet as ft


class ButtonStyle(Enum):
	DEFAULT = "default"


class CustomElevatedButton(ft.ElevatedButton):
	def __init__(
			self,
			name: str,
			style: ButtonStyle,
			on_click: Callable[[ft.ControlEvent], None] | None = None,
			**kwargs
	) -> None:
		super().__init__(**kwargs)

		# Button settings
		self.text = name
		self.on_click = on_click


		# Button style
		self.height = 30
		self.elevation = 2
		self.__update_appearance(style)

	def __update_appearance(self, style: ButtonStyle) -> None:
		match style:
			case ButtonStyle.DEFAULT:
				self.style = ft.ButtonStyle(
					shape=ft.RoundedRectangleBorder(4),
					padding=ft.padding.symmetric(vertical=10, horizontal=18),
					text_style=ft.TextStyle(
						size=14, font_family="MontserratR"
					)

				)
