import os 

def write_file(filename: str, content: str, path: str = os.getcwd()):
    filepath = os.path.join(path, filename)
    with open(filepath, 'w') as f:
        try: 
            f.write(content)
            f.close()
        except Exception as e:
            print(f"Error writing file: {e}")
            f.close()

def append_file(filename: str, content: str, path: str = os.getcwd()):
    filepath = os.path.join(path, filename)
    with open(filepath, 'a') as f:
        try: 
            f.write(content)
            f.close()
        except Exception as e:
            print(f"Error writing file: {e}")
            f.close()

def read_file(filename: str, path: str = os.getcwd(), line: int = None):
    filepath = os.path.join(path, filename)
    if line is None:
        try:
            with open(filepath, 'r') as f:
                output = f.read()
                return output
        except Exception as e:
            print(f"Error reading file {e}")
    elif line is not None:
        try:
            with open(filepath, 'r') as f:
                output = f.readlines()
                output = output[line - 1]
                return output
        except Exception as e:
            print(f"Error reading file {e}")
def read_lines(filename: str, path: str = os.getcwd(), fromLine: int = 0, toLine: int = 1):
    filepath = os.path.join(path, filename)
    try: 
        with open(filepath, 'r') as f:
            output = f.readlines()
            output = output[fromLine:toLine]
            f.close()
            return output
    except Exception as e: 
        print(f"Error reading: {e}")

def deleteFile(filename: str, path: str = os.getcwd()):
    filepath = os.path.join(path, filename)
    try:
        os.remove(filepath)
    except Exception as e:
        print(f"Could not remove File: {e}")