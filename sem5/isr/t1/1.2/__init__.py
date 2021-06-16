import json
import os


def open_file(file_name):
    with open(file_name) as jFile:
        lines = json.load(jFile)
    print(lines)


def write_file(reg, file_name):
    n = list(map(lambda x: x[18:], reg.keys()))
    di = {}
    for i in n:
        di.update({i: reg['_NewRegistration__' + i]})
    with open(file_name, "w+") as jFile:
        json.dump(di, jFile)


def delete_file(file_name):
    os.remove(file_name)


def create_file(file_name):
    with open(file_name) as jFile:
        pass


def rename_file(old_file, new_file):
    try:
        os.rename(old_file, new_file)
    except:
        raise FileNotFoundError
