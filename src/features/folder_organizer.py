import os
from pathlib import Path

from src.features.models.file import MyFile
from src.features.path_repository import PathRepository


class FolderOrganizer:
	def __init__(self, main_path: Path, ext_white_dict: dict[str, list[str]], ext_black_list: list[str]) -> None:
		self.file_manager = PathRepository(main_path)
		self.ext_white_dict = ext_white_dict
		self.ext_black_list = ext_black_list
		self.counter = 0

	def organize_folder(self) -> None:
		dir_content = os.listdir(self.file_manager.main_folder.path)
		folders = [folder for folder in dir_content if os.path.isdir(self.file_manager.main_folder.path.joinpath(folder))]
		main_folders = all([main_dir in folders for main_dir in list(self.ext_white_dict.keys())])
		if dir_content and not main_folders:
			files = self.__get_folder_files_recursively(self.file_manager.main_folder.path)
			self.__move_files(files)
			return

		files = self.file_manager.list_folder_files()
		self.__move_files(files)

	def __move_files(self, files: list[MyFile]):
		for file in files:
			if file.extension in self.ext_white_dict["images"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Imágenes"))

			elif file.extension in self.ext_white_dict["audios"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Audios"))

			elif file.extension in self.ext_white_dict["videos"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Vídeos"))

			elif file.extension in self.ext_white_dict["documents"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Documentos"))

			elif file.extension in self.ext_white_dict["compress"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Carpetas comprimidas"))

			elif file.extension in self.ext_white_dict["executables"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Ejecutables"))

			elif file.extension in self.ext_white_dict["web"]:
				self.file_manager.move_item(file, self.file_manager.create_directory("Internet"))

			else:
				self.file_manager.move_item(file, self.file_manager.create_directory("Otros"))


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


def main():

	white = {
		"images":
			["bmp", "eps", "gif", "heif", "heic", "jpg", "jpeg", "png", "psd", "svg", "tif", "tiff", "drawio", "webp",
			 "ico"],

		"audios":
			["aac", "flac", "mid", "midi", "m4a", "mp3", "ogg", "wav", "wave", "wma"],

		"videos":
			["avi", "flv", "mov", "mp4", "mpeg", "mpg", "mkv", "ogg", "vob", "wmv"],

		"documents":
			["doc", "docx", "epub", "md", "odt", "pdf", "ppt", "pptx", "rtf", "txt", "xls", "xlsx", "csv", "ipynb"],

		"compress":
			["7z", "jar", "rar", "zip"],

		"executables":
			["bat", "com", "exe"],

		"web":
			["css", "eml", "html", "htm", "jar", "js", "msg", "ost", "php", "pst", "xml", "ttf", "otf"]
	}
	black = ["dll", "drv", "ini", "tmp", "temp", "crdownload", "part", "download"]

	organizer = FolderOrganizer(Path(r"C:\Users\jpast\Desktop\test_downloads"), white, black)
	organizer.organize_folder()


if __name__ == '__main__':
	main()
