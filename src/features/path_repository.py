import os
from pathlib import Path

from .models.path import MyPath
from .models.file import MyFile


class PathRepository:
	def __init__(self, main_folder: Path) -> None:
		self.main_folder = MyPath(main_folder)
		self.folder_items = self.list_folder_items()

	def create_directory(self, dir_name) -> Path:
		new_folder = self.main_folder.joinpath(dir_name)

		if not os.path.exists(new_folder):
			os.makedirs(new_folder, exist_ok=True)

		return new_folder

	def list_folder_items(self) -> list[MyFile]:
		folder_items = []
		files = [file for file in os.listdir(self.main_folder.path) if os.path.isfile(self.main_folder.joinpath(file))]

		for file in files:
			try:
				name, extension = file.rsplit(".", 1)
				folder_items.append(MyFile(name, extension, self.main_folder.joinpath(file)))

			except ValueError as no_extension:
				print(f"Error al tratar el archivo {repr(file)}: {no_extension}")

		return folder_items

	@staticmethod
	def move_item(file: MyFile, new_path: Path) -> None:
		os.replace(file.path, new_path.joinpath(file.complete_name()))

	@staticmethod
	def get_file(name: str, extension: str, path: Path) -> MyFile:
		return MyFile(name, extension, path)
