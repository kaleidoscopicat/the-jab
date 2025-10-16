import json
import os

def save_to_file(save_data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(save_data, file, indent=2)
            file.flush()
            os.fsync(file.fileno())

        return True
    except Exception as e:
        print(f"Error saving to file: {e}")
        return False