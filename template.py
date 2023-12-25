import os
from pathlib import Path
import logging

#logging stirng
logging.basicConfig(level=logging.INFO,format="[%(asctime)s]: %(message)s:")

project_name = 'cnnClassifier'

list_of_files=[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init_.py",
    f"src/{project_name}/entity/__init_.py",
    f"src/{project_name}/constants/__init.py",
    "config/config.yml",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")
    
    if(not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{filename} is already exists")
