#  FileForge - File Organizer

A minimal Python CLI tool to organize files in a folder by type (Images, Documents, Music, Videos, Archives, Others). Includes a test file generator for easy demo and testing.

## Project Files

- `fileforge_ultra.py` — Main program. View files (recursive), organize into type-based folders, and show help.
- `test_files.py` — Helper script. Creates sample files in a folder for quick testing and demo.
- `Readme.md`

## Requirements

- Python 3.7+
- Standard library only (`os`, `shutil`)

## Setup

1. Place both files in the same folder:
   - `fileforge_ultra.py`
   - `test_files.py`
2. Ensure you have write permissions to the target folder you want to organize.

## Quick Start

1) Generate sample files (for demo)
2) Run the organizer
3) Use the menu
- 1) View files — lists files recursively inside the given folder and subfolders
- 2) Organize files — creates subfolders (Images, Documents, Music, Videos, Archives, Others) and moves files into them
- 3) Help — short usage description
- 4) Exit — quits the program