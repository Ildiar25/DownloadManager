# 🏁 Downloadmanager Roadmap 2025

---

## 1st Sprint

* Models
  * [x] MyPath
  * [x] MyFile
  * [x] PathRepository
  * [x] FolderOrganizer
  * [ ] Watchdog

# Models breakdown

### MyPath
This model represents a folder or file path and instantiates a Path object.

Parameters:
 - Path: Path(str) || Folder or file path

Return:
 - Path (joinpath) || Path object that represents folder or file path 

Methods:
 - Joinpath: Callable[[str], Path] || Returns itself