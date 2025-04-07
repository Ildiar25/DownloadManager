from dataclasses import dataclass
from .path import MyPath, Path


@dataclass()
class MyFile:
	name: str
	extension: str
	path: MyPath

	def __post_init__(self) -> None:
		if not self.extension:
			raise ValueError(f"File {repr(self.name)} has not extension!")

	def get_path(self) -> Path:
		return self.path.path

	def get_name(self) -> str:
		return self.name + "." + self.extension

	def __str__(self) -> str:
		return f"File: {self.get_name()}, Path: {self.path}"
