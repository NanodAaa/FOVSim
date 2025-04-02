from cores.logger import Logger
import os

class ConfigModel:
    def __init__(self):
        self.default_setting = {
            'camera position' : [0.0, 0.0, 0.0],
            'distance cam carbody' : 0.0,
        }
        
        self.setting_filename = 'setting.json'
        self.setting_filepath = f'./tools/FOV_Sim/data/{self.setting_filename}'
        
        self.log_filename = 'app.log'
        self.log_filepath = f'./tools/FOV_Sim/data/{self.log_filename}'
        
LOGGER = Logger(os.path.dirname(ConfigModel().log_filepath), ConfigModel().log_filename)