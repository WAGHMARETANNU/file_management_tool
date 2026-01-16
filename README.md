# Desktop File Explorer 📂

[![Python Quality Check](https://github.com/WAGHMARETANNU/file_management_tool/actions/workflows/lint.yml/badge.gif)](https://github.com/WAGHMARETANNU/file_management_tool/actions)

A robust, GUI-based file management utility built with Python. This tool simplifies local file organization by allowing users to browse, search, and sort files with real-time file-system interaction.

## 🚀 Key Features
- **Dynamic Sorting:** Sort local files instantly by Name, Date Modified, or File Type.
- **Search Capability:** Integrated search bar to locate specific files within directories.
- **File Metadata:** Displays real-time file counts and system details.
- **Cross-Platform Design:** Built using `tkinter` for a lightweight, native experience on Windows.

## 🛠️ Technical Stack
- **Language:** Python 3.x
- **GUI Framework:** Tkinter
- **File System Logic:** `os`, `shutil`, and `pathlib` modules.
- **CI/CD:** GitHub Actions (Automated PEP8 Linting)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/WAGHMARETANNU/file_management_tool.git](https://github.com/WAGHMARETANNU/file_management_tool.git)
   cd file_management_tool


2. **Run the application:**
*(No external dependencies required)*
```bash
python main.py

```


## ⚙️ Engineering Standards

This repository follows standard Python development practices:

* **CI/CD Integration:** Uses GitHub Actions to run `flake8` linting on every push to ensure code quality and adherence to PEP8 standards.
* **Modular Code:** Functions are separated into logical blocks for maintainability and easier debugging.

## 🤝 Contribution

This project was developed with a focus on clean logic and user-friendly GUI design. Suggestions and Pull Requests are welcome.
