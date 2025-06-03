import yaml
import os


class ConfigLoader:
    def __init__(self, env):
        self.env = env
        self.config = self.load_config()

    def load_config(self):
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
        with open(config_path, 'r') as f:
            full_config = yaml.safe_load(f)
        env_config = full_config['environments'][self.env]
        return env_config

    def get(self, key):
        return self.config.get(key)
