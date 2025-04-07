import os
from pathlib import Path

from .models.path import MyPath
from .models.file import MyFile


class PathRepository:
	def __init__(self, main_folder: Path) -> None:
		self.main_folder = MyPath(main_folder)
		self.folder_items = self.list_folder_files()

	def create_directory(self, dir_name) -> Path:
		new_folder = self.main_folder.joinpath(dir_name)

		if not os.path.exists(new_folder):
			os.makedirs(new_folder, exist_ok=True)

		return new_folder

	def get_file(self, path: str) -> MyFile | None:
		path = Path(path)
		try:
			name, extension = path.name.rsplit(sep=".", maxsplit=1)
			return MyFile(name, extension, MyPath(self.main_folder.joinpath(path)))

		except ValueError as no_extension:
			print(f"Error al tratar el archivo {repr(path)}: {no_extension}")
			return None

	def list_folder_files(self) -> list[MyFile]:
		list_dir = os.listdir(self.main_folder.path)
		path_files = [path for path in list_dir if os.path.isfile(self.main_folder.joinpath(path))]
		files = []

		for path in path_files:
			file = self.get_file(path)
			if not file:
				continue
			files.append(file)

		return files

	@staticmethod
	def move_item(file: MyFile, new_path: Path) -> None:
		os.replace(file.get_path(), new_path.joinpath(file.get_name()))
