#writing common code/functions which we will be using again and again in our project
#creating a module here that we will use again and again i.e. they are called utility functions
import os
from box.exceptions import BoxValueError #for handling exceptions
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox #config box  which provides a way to create dot-accessible dictionaries. 
#This means you can access dictionary items using dot notation, which can make the code cleaner and easier to read.
from pathlib import Path
from typing import Any



@ensure_annotations
#@ensure_annotations?
#this is generally used when if we are passing arguments of different data type and we are using input of different data type
#this is will then error to us then but if we don't put this then this will not throw any exceptions to us so we won't know
#if this is correct or wrong
#reading yaml file till it returns all the content inside the yaml file. Here in every function we are using datatype hence,
#we are using this.

#read yaml file and return all the content in the yaml file
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    