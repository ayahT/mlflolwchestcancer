import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')
project_name="cnnClassifier"
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html" 
]
# Create directories and files
for file_path in list_of_files:
    # Resolve the file path using Pathlib
    file_path = Path(file_path)
    
    # Create parent directories if they do not exist
    if not file_path.parent.exists():
        file_path.parent.mkdir(parents=True)
        logging.info(f"Created directory: {file_path.parent}")
    
    # Create the file
    with open(file_path, 'w') as file:
        file.write("")  # Write an empty string to create the file
        logging.info(f"Created file: {file_path}")

logging.info("Directory structure and files created successfully.")
