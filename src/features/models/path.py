from dataclasses import dataclass
from pathlib import Path

@dataclass()
class MyPath:

	path: Path

	def __post_init__(self) -> None:
		if not self.path.exists():
			raise ValueError(f"Path {repr(self.path)} does not exist!")

	def joinpath(self, new_path: str | Path) -> Path:
		return self.path.joinpath(new_path)

	def __str__(self) -> str:
		return repr(self.path)
