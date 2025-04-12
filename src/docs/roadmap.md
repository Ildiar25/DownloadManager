# 🏁 Download Manager Roadmap 2025

---

## 1st Sprint

* Models
  * [x] MyPath
  * [x] MyFile
  * [x] PathRepository
  * [x] FolderOrganizer
  * [ ] Watchdog

## 2nd Sprint

* GUI
  * [ ] Main Window
  * [ ] App Bar
  * [ ] Options Section
  * [ ] Work Info

---

---

# 💻 Clients (Platform)

Currently, Download Manager is only supported by **Windows Operating System**, **Unix Operating System** and **Macintosh Operating System**.

* [x] Windows OS
* [ ] MacOS
* [ ] Linux
* [ ] Android
* [ ] iOS
* [ ] Web

# Models breakdown

### MyPath
This model represents a folder or file path and instantiates a Path object.

Parameters:
 - Path: Path(str) || Folder or file path

Return:
 - Path (joinpath) || Path object that represents folder or file path 

Methods:
 - Joinpath: Callable[[str], Path] || Returns itself


### MyFile
This models represents a File object.

Parameters:
 - Name: str || The file name
 - Extension: str || The file extension
 - Path: MyPath || The file path

Return:
 - None

Methods:
 - None


### PathRepository
blablabla

Parameters:
 - parm1

Return:
 - parm1

Methods:
 - parm1


### FolderOrganizer
blablabla

Parameters:
 - parm1

Return:
 - parm1

Methods:
 - parm1
