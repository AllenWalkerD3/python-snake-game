
import os


def read_file(path):
    file_path = os.path.dirname(os.path.abspath(__file__))
    with open(file_path+path) as file:
        data = file.read()
    return data

def write_file(path, data):
    file_path = os.path.dirname(os.path.abspath(__file__))
    with open(file_path+path, mode="w") as file:
        data = file.write(data)