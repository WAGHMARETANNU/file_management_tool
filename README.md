# Desktop File Explorer 📂

[![Python Quality Check](https://github.com/WAGHMARETANNU/file_management_tool/actions/workflows/lint.yml/badge.gif)](https://github.com/WAGHMARETANNU/file_management_tool/actions)

A robust, GUI-based file management utility built with Python. This tool simplifies local file organization by allowing users to browse, search, and sort files with real-time file-system interaction.

## 🚀 Key Features
- **Dynamic Sorting:** Toggle between Alphabetical, Chronological (Date Modified), and Type-based sorting via a native GUI.
- **Directory Browsing:** Integrated `filedialog` allows users to select any system folder for immediate indexing.
- **Real-time Metadata Interaction:** Leverages Python's `os` module to fetch and display actual system file structures.
- **Lightweight Footprint:** A zero-dependency tool using Python's standard library for maximum portability.

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

[![Python Quality Check](https://github.com/WAGHMARETANNU/file_management_tool/actions/workflows/lint.yml/badge.svg)](https://github.com/WAGHMARETANNU/file_management_tool/actions/workflows/lint.yml)
