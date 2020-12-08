# check if directory exist and create directory if not exist. #

import os

def assure_path_exists(path):
    dir = os.path.dirname(path)

    if os.path.exists(dir):
        print("The folder already exists")

    if not os.path.exists(dir):
        print("The folder does not exist.  It will be created for you.")
        os.makedirs(dir)

assure_path_exists("ABC/")