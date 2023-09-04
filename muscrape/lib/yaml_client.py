"""YAML client for muscrape."""

import yaml
import os

class YAMLClient:
    """YAML client class."""

    def __init__(self):
        """Initialize."""
        pass

    def load(self, path: str) -> dict:
        """Load method."""
        with open(path, "r") as yaml_file:
            data = yaml.load(yaml_file, Loader=yaml.FullLoader)
        return data

    def dump(self, path: str, data: dict) -> None:
        """Dump method."""
        # recursively create directories if they don't exist
        path_split = path.split("/")
        for i in range(1, len(path_split)):
            path_dir = "/".join(path_split[:i])
            if not os.path.exists(path_dir):
                os.mkdir(path_dir)
        with open(path, "w") as yaml_file:
            yaml.dump(data, yaml_file)
