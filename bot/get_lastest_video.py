import glob
import os


def last_modified_file(folder, count) -> list:
    files = list(filter(os.path.isfile, glob.glob(folder + "/*")))
    if len(files) > 0:
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        return files
    else:
        return None