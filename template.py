import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "tech_know_bot"

list_of_files = [
    "config/sagemaker/__init__.py",
    "data/__init__.py",
    "infrastructure/__init__.py",
    "notebooks/__init__.py",
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/utils/common.py",
    "tests/__init__.py",
    ".github/workflows/.gitkeep",
    ".gitignore",
    "README.md",
    "Dockerfile",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")