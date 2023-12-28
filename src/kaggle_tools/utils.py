import subprocess
import string
import os
from pathlib import Path
import zipfile
import sys


def get_dataset():
    if not(is_running_on_kaggle()):
        dp = get_data_path()
        Path(dp + "input/").mkdir(parents=True, exist_ok=True)
        if not os.path.exists(dp + "input/" + "spaceship-titanic.zip"):
            proc = subprocess.Popen(["kaggle competitions download -c spaceship-titanic -p " + dp + "input/"], stdout=subprocess.PIPE, shell=True)
            proc.wait()
            if not os.path.exists(dp + "input/" + "unzip.done"):
                with zipfile.ZipFile(dp + "input/" + "spaceship-titanic.zip", 'r') as zip_ref:
                    zip_ref.extractall(dp + "input/spaceship-titanic/")
                proc = subprocess.Popen(["touch " + dp + "input/" + "unzip.done"], stdout=subprocess.PIPE, shell=True)
                proc.wait()


def is_running_on_kaggle():
    proc = subprocess.Popen(["ls /home/"], stdout=subprocess.PIPE, shell=True)
    (res, err) = proc.communicate()
    return res == b"jupyter\n"


def get_data_path():
    if is_running_on_kaggle():
        return "/kaggle/"
    else:
        return os.getcwd() + "/"
