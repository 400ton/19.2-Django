import json


def open_fixture(fixture):
    with open(f"./{fixture}") as file:
        file = json.load(file)
        return file
