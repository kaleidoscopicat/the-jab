# @name: JSONHelper.py
# @desc: Merged version of write_to_json.py and import_json.py
#        Intended to be used as a module to be imported!

## @last-modified: 1:19 19/10/25
## | Merged "write_to_json.py" && "import_to_json.py"

import json

def write(filename, jsonData):
    try:
        with open(filename, 'w+') as f:
            json.dump(jsonData, f, indent=4) ## Indenting by 4 is the general standard, not 2.
            f.close()
        return True
    except Exception as e:
        print(f"JSONHelper - Cannot write to file {filename}:\n    {e}")
        return False
    
def read(filename):
    try:
        with open(filename, 'r+') as f:
            data = json.load(f)
            f.close()
        return data
    except Exception as e:
        print(f"JSONHelper - Cannot read from file {filename}:\n    {e}")
        return None