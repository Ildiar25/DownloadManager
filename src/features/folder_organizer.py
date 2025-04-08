from abc import ABC, abstractmethod
from pathlib import Path
from typing import Type

from src.features.models.file import MyFile
from src.features.path_repository import PathRepository


class MoveFileStrategy(ABC):
	@abstractmethod
	def move(self, file_manager: PathRepository, file: MyFile, path: Path) -> bool: ...


class MoveImages(MoveFileStrategy):
	def move(self, file_manager: PathRepository, file: MyFile, path: Path) -> bool:
		return file_manager.move_item(file, file_manager.create("Imágenes"))


class MoveAudios(MoveFileStrategy):
	def move(self, file_manager: PathRepository, file: MyFile, path: Path) -> bool:
		return file_manager.move_item(file, file_manager.create("Audios"))


class MoveVideos(MoveFileStrategy):
	def move(self, file_manager: PathRepository, file: MyFile, path: Path) -> bool:
		return file_manager.move_item(file, file_manager.create("Vídeos"))


class MoveDocuments(MoveFileStrategy):
	def move(self, file_manager: PathRepository, file: MyFile, path: Path) -> bool:
		return file_manager.move_item(file, file_manager.create("Documentos"))


class MoveCompress(MoveFileStrategy):
	def move(self, file_manager: PathRepository, file: MyFile, path: Path) -> bool:
		return file_manager.move_item(file, file_manager.create("Carpetas Comprimidas"))


class MoveExecutables(MoveFileStrategy):
	def move(self, file_manager: PathRepository, file: MyFile, path: Path) -> bool:
		return file_manager.move_item(file, file_manager.create("Instaladores"))


class MoveWebs(MoveFileStrategy):
	def move(self, file_manager: PathRepository, file: MyFile, path: Path) -> bool:
		return file_manager.move_item(file, file_manager.create("Archivos Web"))


class MoveOthers(MoveFileStrategy):
	def move(self, file_manager: PathRepository, file: MyFile, path: Path) -> bool:
		return file_manager.move_item(file, file_manager.create("Otros"))


class MoveController:
	def __init__(self, white_dict: dict[str, list[str]], black_list: [str]) -> None:
		self.__white_dict = white_dict
		self.__black_list = black_list
		self.__strategies: dict[str, Type[MoveFileStrategy]] = {
			"images": MoveImages,
			"audios": MoveAudios,
			"videos": MoveVideos,
			"documents": MoveDocuments,
			"compress": MoveCompress,
			"executables": MoveExecutables,
			"web": MoveWebs,
			"other": MoveOthers
		}

	def __new_strategy(self, extension: str) -> str:
		for doc_type, extensions in self.__white_dict.items():
			if extension in extensions:
				return doc_type

		return "other"

	def move_files(self, file_manager: PathRepository, file: MyFile, path: Path) -> bool:
		strategy = self.__strategies.get(self.__new_strategy(file.extension), )
		if file.extension not in self.__black_list and strategy:
			return strategy().move(file_manager, file, path)

		else:
			return False


class FolderOrganizer:
	def __init__(self, main_path: Path, ext_white_dict: dict[str, list[str]], ext_black_list: list[str]) -> None:

		self.main_path = main_path
		self.__white_dict = ext_white_dict
		self.__black_list = ext_black_list
		self.__folders_selected = ext_white_dict.keys()

		self.__file_manager = PathRepository(self.main_path)
		self.__move_controller = MoveController(self.__white_dict, self.__black_list)
		self.__old_folders = []

		self.counter = 0

	def organize_folder(self) -> None:
		dir_content = list(self.main_path.iterdir())
		folders = [folder for folder in dir_content if self.main_path.joinpath(folder).is_dir()]
		main_folders = all([main_dir in folders for main_dir in self.__folders_selected])

		if dir_content and not main_folders:
			files = self.__get_folder_files_recursively(self.__file_manager.main_folder.path)
			self.__move_files(files)
			self.__clean_empty_folders(self.__old_folders)
			return

		files = self.__file_manager.list_folder_files()
		self.__move_files(files)

	def __move_files(self, files: list[MyFile]):
		for file in files:
			is_moved = False

			if self.__move_controller.move_files(self.__file_manager, file, self.__file_manager.main_folder):
				is_moved = True

			if is_moved:
				self.counter += 1

			self.__old_folders.append(file.get_path().parent)

	def __get_folder_files_recursively(self, main_path: Path) -> list[MyFile]:
		folder_files = []

		for item in main_path.rglob("*.*"):
			if item.is_file():
				fold_file = self.__file_manager.get_file(item)
				if not fold_file:
					continue
				folder_files.append(fold_file)

		return folder_files

	@staticmethod
	def __clean_empty_folders(old_folders: list[Path]) -> None:
		old_folders.reverse()
		for folder in old_folders:
			if folder.exists() and not list(folder.iterdir()):
				try:
					folder.rmdir()

				except OSError as os_error:
					print(f"No se ha podido eliminar el directorio {repr(folder)}: {os_error}.")
