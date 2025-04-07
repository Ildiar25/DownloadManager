import os
from dataclasses import dataclass
from pathlib import Path

@dataclass()
class MyPath:

	path: Path

	def __post_init__(self) -> None:
		if not os.path.exists(self.path):
			raise ValueError(f"Path {repr(self.path)} does not exist!")

	def joinpath(self, folder: str) -> Path:
		return self.path.joinpath(folder)