"""JSON client for the muscrape API."""

import os
import json

class JSONClient:
    """JSON client class"""

    def __init__(self):
        pass

    def load(self, file_path: str):
        """Load JSON file"""
        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    def dump(self, file_path: str, data: dict):
        """Dump JSON file"""
        path_split = file_path.split("/")
        for i in range(1, len(path_split)):
            path_dir = "/".join(path_split[:i])
            if not os.path.exists(path_dir):
                os.mkdir(path_dir)
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
