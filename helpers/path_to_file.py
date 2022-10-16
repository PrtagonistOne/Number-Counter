import os

import pandas as pd

extension_list = [".xlsx", ".xlsm", ".xltx", ".xltm"]


def check_for_datasheets():
    # return all files as a list
    for file in os.listdir():
        # check the files which are end with specific extension
        for ext in extension_list:
            if file.endswith(ext):
                # print path name of selected file
                return absolute_file_path(file), file


def absolute_file_path(path_fname: str):
    return os.path.abspath(path_fname)


def get_dataset(path_fname: str):
    df = pd.read_excel(path_fname)
    initial_set = df["Set"].to_list() if df["Set"].any() else []
    initial_target = int(df["Target"].to_list()[0]) if df["Target"].any() else None
    initial_results = df["Result"].to_list() if df["Result"].any() else None

    return initial_set, initial_target, initial_results
