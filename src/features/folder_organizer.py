import os
from pathlib import Path

from src.features.models.file import MyFile
from src.features.path_repository import PathRepository


class FolderOrganizer:
	def __init__(self, main_path: Path, ext_white_dict: dict[str, list[str]], ext_black_list: list[str]) -> None:
		self.file_manager = PathRepository(main_path)
		self.ext_white_list = ext_white_dict
		self.ext_black_list = ext_black_list
		self.counter = 0

	def organize_folder(self) -> None:
		if os.listdir(self.file_manager.main_folder.path):
			files = self.__get_folder_files_recursively(self.file_manager.main_folder.path)
			temp_folder = self.file_manager.create_directory("temp")

			for file in files:
				self.file_manager.move_item(file, temp_folder)

		files = self.file_manager.list_folder_items()
		self.move_files(files)

	def move_files(self, files: list[MyFile]):
		for file in files:
			if file.extension in self.ext_white_list["images"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Imágenes"))

			if file.extension in self.ext_white_list["audios"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Audios"))

			if file.extension in self.ext_white_list["videos"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Vídeos"))

			if file.extension in self.ext_white_list["documents"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Documentos"))

			if file.extension in self.ext_white_list["compress"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Carpetas comprimidas"))

			if file.extension in self.ext_white_list["executables"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Ejecutables"))

			if file.extension in self.ext_white_list["web"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Internet"))

	def __get_folder_files_recursively(self, main_path: Path) -> list[MyFile]:
		folder_files = []

		def _get_through_directories(actual_path: Path):
			root, subfolders, files = next(os.walk(actual_path))
			try:
				for file in files:
					try:
						name, extension = file.rsplit(".", 1)
						folder_files.append(self.file_manager.get_file(name, extension, actual_path.joinpath(file)))
					except ValueError as no_extension:
						print(f"Error al tratar el archivo {repr(file)}: {no_extension}")

				for folder in subfolders:
					_get_through_directories(actual_path.joinpath(folder))

			except OSError as path_error:
				print(f"There's {path_error} error while trying to access the next path: {actual_path}")
				return

		_get_through_directories(main_path)
		return folder_files


def main():
	organizer = FolderOrganizer(Path(r"C:\Users\jpast\Desktop\test_downloads"), {}, [])
	organizer.organize_folder()


if __name__ == '__main__':
	main()
