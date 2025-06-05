# utils/config_loader.py
import yaml
import os

class ConfigLoader:
    def __init__(self, env):
        self.env = env
        self.config = self.load_config()

    def load_config(self):
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
        with open(config_path, 'r') as f:
            all_config = yaml.safe_load(f)
        return all_config['environments'][self.env]

    def get(self, key):
        return self.config.get(key)
