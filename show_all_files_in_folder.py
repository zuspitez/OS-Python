# show all files in a folder #

import os

path = ("data_set")

def show_all_files_in_folder(path):

    # Get all file path
    filename = [os.path.join(path,file) for file in os.listdir(path)]
    print(filename)

show_all_files_in_folder(path)