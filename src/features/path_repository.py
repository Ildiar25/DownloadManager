from pathlib import Path

from .models.path import MyPath
from .models.file import MyFile


class PathRepository:
	def __init__(self, main_folder: Path) -> None:
		self.main_folder = MyPath(main_folder)
		self.folder_items = self.list_folder_files()

		self.duplicated = []

	def create_directory(self, dir_name) -> Path:
		new_folder = self.main_folder.joinpath(dir_name)

		if not new_folder.exists():
			new_folder.mkdir(parents=True, exist_ok=True)

		return new_folder

	def get_file(self, path: str) -> MyFile | None:
		path = Path(path)
		try:
			name = path.stem
			extension = path.suffix
			return MyFile(name, extension, MyPath(self.main_folder.joinpath(path)))

		except ValueError as no_extension:
			print(f"Error al tratar el archivo {repr(path)}: {no_extension}")
			return None

	def list_folder_files(self) -> list[MyFile]:
		list_dir = self.main_folder.path.iterdir()
		path_files = [path for path in list_dir if path.is_file()]
		files = []

		for path in path_files:
			file = self.get_file(path)
			if not file:
				continue
			files.append(file)

		return files


	def move_item(self, file: MyFile, new_path: Path) -> None:
		try:
			file.get_path().rename(new_path.joinpath(file.get_name()))

		except FileExistsError:
			self.duplicated.append(file)
