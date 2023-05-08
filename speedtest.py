from pathlib import Path, PurePath


def pure_path(files_list):
    for file in files_list:
        path = Path(file)
        path.name


def concrete_path(files_list):
    for file in files_list:
        path = PurePath(file)
        path.name


files_list = Path("file_list.txt").read_text().splitlines()
pure_path(files_list)
# concrete_path(files_list)
