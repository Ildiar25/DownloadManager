from dataclasses import dataclass
from pathlib import Path


@dataclass()
class MyFile:
	name: str
	extension: str
	path: Path

	def __post_init__(self) -> None:
		if not self.extension:
			raise ValueError(f"File {repr(self.name)} has not extension!")

	def complete_name(self) -> str:
		return self.name + "." + self.extension
