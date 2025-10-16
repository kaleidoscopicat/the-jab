import json

def import_json(filename):
    try:
        with open(filename, 'r') as file:
            save_data = json.load(file)
        return save_data
    except FileNotFoundError:
        raise exit(f"Save file '{filename}' not found! Deal with it.")
    except json.JSONDecodeError:
        print(f"Error reading save file '{filename}'. Invalid JSON format.")
        return None
