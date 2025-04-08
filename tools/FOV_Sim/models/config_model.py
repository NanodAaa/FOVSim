from cores.logger import Logger
from enum import Enum, auto
import os

class ConfigModel:
    class Keys(Enum):
        CAMERA_POSITION = 'camera position'
        DISTANCE_CAM_CARBODY = 'distance cam carbody'
        DISTANCE_CAM_GROUND = 'distance cam ground'
        FITTING_FUNC_COEFS = 'fitting func coefs'
        FITTING_FUNC_COEFS_REVERSE = 'fitting func coefs reverse'
        CAMERA_POSE = 'camera pose'
        SENSOR_PARAMS = 'sensor params'
        MONITOR_PARAMS = 'monitor params'
        CROP_REGION = 'crop region'
        REGULATION_POINTS = 'regulation points'
        
    class TableFormatKeys(Enum):
        WIDTH = 'width'
        ANCHOR = 'anchor'
        STICKY = 'sticky'
    
    def __init__(self):
        self.default_setting = {
            self.Keys.CAMERA_POSITION.value : [0.0, 0.0, 0.0],
            self.Keys.DISTANCE_CAM_CARBODY.value : 0.0,
            self.Keys.DISTANCE_CAM_GROUND.value : 0.0,       
            self.Keys.FITTING_FUNC_COEFS.value : [-6.84e-11, 5.14e-9, -1.12e-6, 4.13e-6, 0.0599, 4.95e-5],
            self.Keys.FITTING_FUNC_COEFS_REVERSE.value : [0.0103, -0.0589, 0.215, -0.154, 16.8, -0.00596],
            self.Keys.CAMERA_POSE.value : [0.0, 0.0, 0.0],
            self.Keys.SENSOR_PARAMS.value : [1920, 1536, 0.003],
            self.Keys.MONITOR_PARAMS.value : [720, 540, 0.1521],
            self.Keys.CROP_REGION.value : [0, 0, 720, 540],
            self.Keys.REGULATION_POINTS.value : {}, # Regulation Points relative to camera coordinates.
        }

        self.setting_filename = 'setting.json'
        self.setting_filepath = f'./tools/FOV_Sim/data/{self.setting_filename}'
        
        self.log_filename = 'app.log'
        self.log_filepath = f'./tools/FOV_Sim/data/{self.log_filename}'
        
        self.table_format_dict = {
            self.TableFormatKeys.WIDTH.value : 50,
            self.TableFormatKeys.ANCHOR.value : 'center',
            self.TableFormatKeys.STICKY.value : 'nsew',
        }
        self.result_table_column = ['X_mm', 'Y_mm', 'Z_mm', 'Sensor_x', 'Sensor_y', 'Monitor_x', 'Monitor_y', 'Name', 'Result']
        
        
LOGGER = Logger(os.path.dirname(ConfigModel().log_filepath), ConfigModel().log_filename)  