from ..models.storage_model import JsonStorageModel
from ..models.config_model import ConfigModel
from ..models.config_model import LOGGER
from enum import Enum, auto
from ..models.calculate_model import CalculateModel

class FovSimController:
    class ReturnCode(Enum):
        OK = 0
        FILE_NOT_FOUND = auto()
        DATA_TYPE_ERROR = auto()

    def __init__(self):
        self.cal_model = CalculateModel()
        self.json_save_model = JsonStorageModel()
        self.config_model = ConfigModel()

    def init_setting_data(self):
        data = self.json_save_model.load(self.config_model.setting_filepath)
        if data == JsonStorageModel.ReturnCode.FILE_NOT_FOUND:
            if self.json_save_model.create_empty_json_file(self.config_model.setting_filepath, self.config_model.default_setting) == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
                return self.ReturnCode.FILE_NOT_FOUND
            
        elif data == {}:
            if self.json_save_model.create_empty_json_file(self.config_model.setting_filepath, self.config_model.default_setting) == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
                return self.ReturnCode.FILE_NOT_FOUND
            
    def get_regulation_points_ep(self, camera_coordinates: list, distance_camera_carbody: float, distance_camera_ground: float) -> list:
        """ 
        Get 4 regulation points relative to EP.
        """
        regulation_points = self.cal_model.get_regulation_points(camera_coordinates, distance_camera_carbody, distance_camera_ground)
        if regulation_points == self.cal_model.ReturnCode.TYPE_ERROR:
            return self.ReturnCode.DATA_TYPE_ERROR

        return regulation_points
        
    def transfrom_regulation_points_into_cam_coordinates(self, camera_coordinates: list, regulation_points: list) -> list:
        """ 
        Transform regulation points from E.P. coordinates into camera coordinates.  
        `camera_coordinates`: Camera coordinates.  
        `regulation_points`: List of regulation points - [A, B, C, D]  
        """
        if not isinstance(camera_coordinates, list) or not isinstance(regulation_points, list):
            return self.ReturnCode.DATA_TYPE_ERROR
        
        regulation_points_camera_coordinates = []
        for point in regulation_points:
            point_camera_coordinates = self.cal_model.coordinate_transform(camera_coordinates, point)
            regulation_points_camera_coordinates.append(point_camera_coordinates)
            
        return regulation_points_camera_coordinates
        
    def read_data_from_json(self) -> dict:
        """ 
        Read data from json.  
        Return FILE_NOT_FOUND when json file does not exist.  
        Return data when success.  
        """
        data = self.json_save_model.load(self.config_model.setting_filepath)
        if data == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            return self.ReturnCode.FILE_NOT_FOUND

        return data
    
    def save_data_to_json(self, data: dict):
        """ 
        Receive data from view and save it to json file.
        """
        # If data is not a list, raise TypeError
        if not isinstance(data, dict):
            LOGGER.error('data_list should be a dict!')
            return self.ReturnCode.DATA_TYPE_ERROR

        # Write data into json
        result = self.json_save_model.save(filepath=self.config_model.setting_filepath, data=data)
        if result == self.json_save_model.ReturnCode.DATA_TYPE_INVALID:
            LOGGER.error('Error when write data into json! - Data type error')
            return self.ReturnCode.DATA_TYPE_ERROR
        elif result == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when write data into json! - File not found.')
            return self.ReturnCode.FILE_NOT_FOUND