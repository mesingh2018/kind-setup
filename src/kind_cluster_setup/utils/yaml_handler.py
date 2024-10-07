import yaml
from typing import Any, TextIO

def load_yaml(file_path: str) -> Any:
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def dump_yaml(data: Any, file: TextIO) -> None:
    yaml.dump(data, file)