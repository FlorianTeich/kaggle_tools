import subprocess
import string
import os
from pathlib import Path
import zipfile
import sys


def get_dataset(datasetname:str="spaceship-titanic"):
    """
    Download the Dataset and unpack it

    Args:
        datasetname (str): The competition name of which the dataset need to be downloaded
    """
    if not(is_running_on_kaggle()):
        dp = get_data_path()
        dp_input = dp + "input/"
        zipfile_path = dp_input + datasetname + ".zip"
        donezip_path = dp_input + "unzip.done"
        Path(dp + "input/").mkdir(parents=True, exist_ok=True)
        if not os.path.exists(zipfile_path):
            proc = subprocess.Popen(["kaggle competitions download -c " + datasetname + " -p " + dp_input], stdout=subprocess.PIPE, shell=True)
            proc.wait()
            if not os.path.exists(donezip_path):
                with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
                    zip_ref.extractall(dp_input + datasetname + "/")
                proc = subprocess.Popen(["touch " + donezip_path], stdout=subprocess.PIPE, shell=True)
                proc.wait()


def is_running_on_kaggle() -> bool:
    """
    Return whether the notebook is running online on kaggle.com or locally

    Returns:
        bool: Whether the notebook is running online on kaggle.com
    """
    proc = subprocess.Popen(["ls /home/"], stdout=subprocess.PIPE, shell=True)
    (res, err) = proc.communicate()
    return res == b"jupyter\n"


def get_data_path() -> str:
    """
    Returns appropriate working directory depending on whether notebook is running on kaggle.com or locally
    
    Returns:
        str: The working directory
    """
    if is_running_on_kaggle():
        return "/kaggle/"
    else:
        return os.getcwd() + "/"
