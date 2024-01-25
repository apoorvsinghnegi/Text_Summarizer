import os
from pathlib import Path
import logging #For logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",#to write CI/CD deployment files(.github used to do deployment- directly take any commit from github
    # to cloud. # creating.gitkeep as hidden file so that when we commit we don't have any emplty file to deploy)

    f"src/{project_name}/__init__.py",#(__init__.py"- used as constructor- to import from folder which are local to the project i.e.
    # install them as local package it is used as when we do installation of this local package it looks for this constructor file
    #whenever this constructor file present it is considered to be local package)

    f"src/{project_name}/components/__init__.py",# another local package
    f"src/{project_name}/utils/__init__.py", # to write all utility
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",#contains training and prediction pipeline
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",#model related parameters 
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)# to avoid path issue we use this library i.e. to convert path to our desired path.
    filedir, filename = os.path.split(filepath)#to split folder and filename separately we use this split function

    if filedir != "": 
        os.makedirs(filedir, exist_ok=True)# it creates file folder here if we didn't have directory already.
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):#if file size is 0 or file with the same name don't already exists
        with open(filepath,'w') as f:# open file in write mode 
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")