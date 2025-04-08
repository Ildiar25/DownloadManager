import os
from pathlib import Path

from src.features.models.file import MyFile
from src.features.path_repository import PathRepository


class FolderOrganizer:
	def __init__(self, main_path: Path, ext_white_dict: dict[str, list[str]], ext_black_list: list[str]) -> None:

		self.main_path = main_path
		self.white_dict = ext_white_dict
		self.black_list = ext_black_list
		self.folders_selected = ext_white_dict.keys()

		self.file_manager = PathRepository(self.main_path)
		self.old_folders = []

		self.counter = 0

	def organize_folder(self) -> None:
		dir_content = os.listdir(self.main_path)
		folders = [folder for folder in dir_content if os.path.isdir(self.main_path.joinpath(folder))]
		main_folders = all([main_dir in folders for main_dir in self.folders_selected])

		if dir_content and not main_folders:
			files = self.__get_folder_files_recursively(self.file_manager.main_folder.path)
			self.__move_files(files)
			print(self.file_manager.duplicated)
			self.__clean_empty_folders(self.old_folders)
			print(self.counter)
			return

		files = self.file_manager.list_folder_files()
		self.__move_files(files)
		print(self.counter)

	def __move_files(self, files: list[MyFile]):
		for file in files:
			is_moved = False
			if file.extension in self.white_dict.get("images", []):
				if self.file_manager.move_item(file, self.file_manager.create_directory("Imágenes")):
					is_moved = True

			elif file.extension in self.white_dict.get("audios", []):
				if self.file_manager.move_item(file, self.file_manager.create_directory("Audios")):
					is_moved = True

			elif file.extension in self.white_dict.get("videos", []):
				if self.file_manager.move_item(file, self.file_manager.create_directory("Vídeos")):
					is_moved = True

			elif file.extension in self.white_dict.get("documents", []):
				if self.file_manager.move_item(file, self.file_manager.create_directory("Documentos")):
					is_moved = True

			elif file.extension in self.white_dict.get("compress", []):
				if self.file_manager.move_item(file, self.file_manager.create_directory("Carpetas comprimidas")):
					is_moved = True

			elif file.extension in self.white_dict.get("executables", []):
				if self.file_manager.move_item(file, self.file_manager.create_directory("Ejecutables")):
					is_moved = True

			elif file.extension in self.white_dict.get("web", []):
				if self.file_manager.move_item(file, self.file_manager.create_directory("Internet")):
					is_moved = True

			else:
				if self.file_manager.move_item(file, self.file_manager.create_directory("Otros")):
					is_moved = True

			if is_moved:
				self.counter += 1
			self.old_folders.append(file.get_path().parent)

	def __get_folder_files_recursively(self, main_path: Path) -> list[MyFile]:
		folder_files = []

		def _get_through_directories(actual_path: Path):
			_, subfolders, files = next(os.walk(actual_path))
			try:
				for file in files:
					fold_file = self.file_manager.get_file(str(actual_path.joinpath(file)))
					if not fold_file:
						continue

					folder_files.append(fold_file)

				for folder in subfolders:
					_get_through_directories(actual_path.joinpath(folder))

			except OSError as path_error:
				print(f"There's {path_error} error while trying to access the next path: {actual_path}")
				return

		_get_through_directories(main_path)
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


def main():

	white = {
		"images":
			[".bmp", ".eps", ".gif", ".heif", ".heic", ".jpg", ".jpeg", ".png", ".psd", ".svg", ".tif", ".tiff", ".drawio", ".webp",
			 ".ico"],

		"audios":
			[".aac", ".flac", ".mid", ".midi", ".m4a", ".mp3", ".ogg", ".wav", ".wave", ".wma"],

		"videos":
			[".avi", ".flv", ".mov", ".mp4", ".mpeg", ".mpg", ".mkv", ".ogg", ".vob", ".wmv"],

		"documents":
			[".doc", ".docx", ".epub", ".md", ".odt", ".pdf", ".ppt", ".pptx", ".rtf", ".txt", ".xls", ".xlsx", ".csv", ".ipynb"],

		"compress":
			[".7z", ".jar", ".rar", ".zip"],

		"executables":
			[".bat", ".com", ".exe"],

		"web":
			[".css", ".eml", ".html", ".htm", ".jar", ".js", ".msg", ".ost", ".php", ".pst", ".xml", ".ttf", ".otf"],

		"other": []
	}
	black = [".dll", ".drv", ".ini", ".tmp", ".temp", ".crdownload", ".part", ".download"]

	organizer = FolderOrganizer(Path(r"C:\Users\jpast\Desktop\test_downloads"), white, black)
	organizer.organize_folder()


if __name__ == '__main__':
	main()
