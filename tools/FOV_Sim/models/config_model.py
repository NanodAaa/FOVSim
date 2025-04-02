from cores.logger import Logger
from enum import Enum, auto
import os

class ConfigModel:
    class Keys(Enum):
        CAMERA_POSITION = 'camera position'
        DISTANCE_CAM_CARBODY = 'distance cam carbody'
        DISTANCE_CAM_GROUND = 'distance cam ground'
    
    def __init__(self):
        self.default_setting = {
            self.Keys.CAMERA_POSITION : [0.0, 0.0, 0.0],
            self.Keys.DISTANCE_CAM_CARBODY : 0.0,
            self.Keys.DISTANCE_CAM_GROUND : 0.0,            
        }
        
        self.setting_filename = 'setting.json'
        self.setting_filepath = f'./tools/FOV_Sim/data/{self.setting_filename}'
        
        self.log_filename = 'app.log'
        self.log_filepath = f'./tools/FOV_Sim/data/{self.log_filename}'
        
LOGGER = Logger(os.path.dirname(ConfigModel().log_filepath), ConfigModel().log_filename)  