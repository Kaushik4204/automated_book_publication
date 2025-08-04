import json
import os

def save_text(content, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def load_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def save_json(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def list_files(directory, extension=None):
    return [f for f in os.listdir(directory) if extension is None or f.endswith(extension)]
