from dataclasses import dataclass
from pathlib import Path


@dataclass()
class MyFile:
	name: str
	extension: str
	path: Path

	def complete_name(self) -> str:
		return self.name + "." + self.extension
