# sim2real/config/__init__.py

import yaml

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)
