import glob
import os


def last_modified_file(folder) -> list:
    files = glob.glob(folder + "/*")
    return files