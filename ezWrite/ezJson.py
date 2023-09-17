import json
import os
import ezWrite as ew


def get_path(filename: str, path: str):
    if ".json" not in filename:
        filename = filename + ".json"

    filepath = os.path.join(path, filename)
    return filepath

def read_dataset(filename: str, dataset: str, path: str = os.getcwd()):
    filepath = get_path(filename, path)
    with open(filepath) as json_file:
        data = json.load(json_file)
        for i in data[dataset]:
            return i
        
def write_json(filename: str, content: str, path: str = os.getcwd(), sort_keys: bool = False):
    if ".json" not in filename:
        filename = filename + ".json"
    if sort_keys == False:
        filepath = os.path.join(path, filename)
        with open(filepath, 'a') as json_file:
            json.dump(content, json_file)
    else:
        filepath = os.path.join(path, filename)
        with open(filepath, 'a') as json_file:
            json.dump(content, json_file, sort_keys=True)

def read_data(filename: str, key: str, path: str = os.getcwd()):
    filepath = get_path(filename, path)
    with open(filepath) as json_file:
        datafile = json.load(json_file)
        output = datafile[key]
        return output

def read_whole_file(filename, path: str = os.getcwd()):
    if ".json" not in filename:
        filename = filename + ".json"
    output = ew.read_file(filename, path)
    return output


def delete_data(filename: str, key: str, path: str = os.getcwd()):
    if ".json" not in filename:
        filename = filename + ".json"

    filepath = os.path.join(path, filename)
    with open(filepath) as output:
        data = json.load(output)
        del data[key]
        with open(filepath, 'w') as f:
            json.dump(data, f)