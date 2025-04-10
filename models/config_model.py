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
        CAMERA_CLASS = 'camera class'
        CAMERA_SIDE = 'camera side'
        
    class TableFormatKeys(Enum):
        WIDTH = 'width'
        ANCHOR = 'anchor'
        STICKY = 'sticky'
        
    class ProfileSelectionComboboxIndexs(Enum):
        CLASS_II_DRIVER = 'Class II - Driver side'
        CLASS_II_PASSANGER = 'Class II - Passenger side'
        CLASS_IV_DRIVER = 'Class IV - Driver side'
        CLASS_IV_PASSANGER = 'Class IV - Passenger side'
    
    def __init__(self):
        # Default setting values.
        self.default_setting_2_driver = {
            self.Keys.CAMERA_POSITION.value : [0.01, -0.01, -0.01],
            self.Keys.DISTANCE_CAM_CARBODY.value : 0.01,
            self.Keys.DISTANCE_CAM_GROUND.value : 1.0,       
            self.Keys.FITTING_FUNC_COEFS.value : [-6.84e-11, 5.14e-9, -1.12e-6, 4.13e-6, 0.0599, 4.95e-5],
            self.Keys.FITTING_FUNC_COEFS_REVERSE.value : [0.0103, -0.0589, 0.215, -0.154, 16.8, -0.00596],
            self.Keys.CAMERA_POSE.value : [0.0, 0.0, 0.0],
            self.Keys.SENSOR_PARAMS.value : [1536, 1920, 0.003],
            self.Keys.MONITOR_PARAMS.value : [540, 720, 0.1521],
            self.Keys.CROP_REGION.value : [550, 451, 540, 720],
            self.Keys.REGULATION_POINTS.value : {}, # Regulation Points relative to camera coordinates.
        }
        self.default_setting_2_passanger = {
            self.Keys.CAMERA_POSITION.value : [0.01, -0.01, -0.01],
            self.Keys.DISTANCE_CAM_CARBODY.value : 0.01,
            self.Keys.DISTANCE_CAM_GROUND.value : 1.0,       
            self.Keys.FITTING_FUNC_COEFS.value : [-6.84e-11, 5.14e-9, -1.12e-6, 4.13e-6, 0.0599, 4.95e-5],
            self.Keys.FITTING_FUNC_COEFS_REVERSE.value : [0.0103, -0.0589, 0.215, -0.154, 16.8, -0.00596],
            self.Keys.CAMERA_POSE.value : [0.0, 0.0, 0.0],
            self.Keys.SENSOR_PARAMS.value : [1536, 1920, 0.003],
            self.Keys.MONITOR_PARAMS.value : [540, 720, 0.1521],
            self.Keys.CROP_REGION.value : [550, 451, 540, 720],
            self.Keys.REGULATION_POINTS.value : {}, # Regulation Points relative to camera coordinates.
        }
        self.default_setting_4_driver = {
            self.Keys.CAMERA_POSITION.value : [0.01, -0.01, -0.01],
            self.Keys.DISTANCE_CAM_CARBODY.value : 0.01,
            self.Keys.DISTANCE_CAM_GROUND.value : 1.0,       
            self.Keys.FITTING_FUNC_COEFS.value : [-6.84e-11, 5.14e-9, -1.12e-6, 4.13e-6, 0.0599, 4.95e-5],
            self.Keys.FITTING_FUNC_COEFS_REVERSE.value : [0.0103, -0.0589, 0.215, -0.154, 16.8, -0.00596],
            self.Keys.CAMERA_POSE.value : [0.0, 0.0, 0.0],
            self.Keys.SENSOR_PARAMS.value : [1536, 1920, 0.003],
            self.Keys.MONITOR_PARAMS.value : [540, 720, 0.1521],
            self.Keys.CROP_REGION.value : [550, 451, 540, 720],
            self.Keys.REGULATION_POINTS.value : {}, # Regulation Points relative to camera coordinates.
        }
        self.default_setting_4_passanger = {
            self.Keys.CAMERA_POSITION.value : [0.01, -0.01, -0.01],
            self.Keys.DISTANCE_CAM_CARBODY.value : 0.01,
            self.Keys.DISTANCE_CAM_GROUND.value : 1.0,       
            self.Keys.FITTING_FUNC_COEFS.value : [-6.84e-11, 5.14e-9, -1.12e-6, 4.13e-6, 0.0599, 4.95e-5],
            self.Keys.FITTING_FUNC_COEFS_REVERSE.value : [0.0103, -0.0589, 0.215, -0.154, 16.8, -0.00596],
            self.Keys.CAMERA_POSE.value : [0.0, 0.0, 0.0],
            self.Keys.SENSOR_PARAMS.value : [1536, 1920, 0.003],
            self.Keys.MONITOR_PARAMS.value : [540, 720, 0.1521],
            self.Keys.CROP_REGION.value : [550, 451, 540, 720],
            self.Keys.REGULATION_POINTS.value : {}, # Regulation Points relative to camera coordinates.
        }

        # Setting files name & path.
        self.setting_2_driver_filename = 'setting_2_driver.json'
        self.setting_2_driver_filepath = f'./data/{self.setting_2_driver_filename}'
        
        self.setting_2_passanger_filename = 'setting_2_passanger.json'
        self.setting_2_passanger_filepath = f'./data/{self.setting_2_passanger_filename}'
        
        self.setting_4_driver_filename = 'setting_4_driver.json'
        self.setting_4_driver_filepath = f'./data/{self.setting_4_driver_filename}'
        
        self.setting_4_passanger_filename = 'setting_4_passanger.json'
        self.setting_4_passanger_filepath = f'./data/{self.setting_4_passanger_filename}'
        
        # Log file name & path.
        self.log_filename = 'app.log'
        self.log_filepath = f'./data/{self.log_filename}'
        
        self.table_format_dict = {
            self.TableFormatKeys.WIDTH.value : 50,
            self.TableFormatKeys.ANCHOR.value : 'center',
            self.TableFormatKeys.STICKY.value : 'nsew',
        }
        
        self.result_table_column = ['X_mm', 'Y_mm', 'Z_mm', 'Sensor_x', 'Sensor_y', 'Monitor_x', 'Monitor_y', 'Name', 'Result']
         
        self.profile_selection_combobox_format_dict = {
            'state' : 'readonly',          
        }
        
        # Profile selection combobox values.
        self.profile_selection_combobox_values = [
            self.ProfileSelectionComboboxIndexs.CLASS_II_DRIVER.value,
            self.ProfileSelectionComboboxIndexs.CLASS_II_PASSANGER.value,
            self.ProfileSelectionComboboxIndexs.CLASS_IV_DRIVER.value,
            self.ProfileSelectionComboboxIndexs.CLASS_IV_PASSANGER.value,
        ]
         
LOGGER = Logger(os.path.dirname(ConfigModel().log_filepath), ConfigModel().log_filename)  