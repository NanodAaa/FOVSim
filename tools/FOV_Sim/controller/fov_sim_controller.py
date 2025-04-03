from ..models.storage_model import JsonStorageModel
from ..models.config_model import ConfigModel
from ..models.config_model import LOGGER
from enum import Enum, auto
from ..models.calculate_model import CalculateModel
from cores import functions

class FovSimController:
    class ReturnCode(Enum):
        OK = 0
        FILE_NOT_FOUND = auto()
        DATA_TYPE_ERROR = auto()
        DATA_VALUE_ERROR = auto()

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
            
    def get_regulation_points_II_ep(self, camera_coordinates: list, distance_camera_carbody: float, distance_camera_ground: float) -> list:
        """ 
        Get 4 regulation points relative to EP.
        `camera_coordinates`: Camera coordinates relative to E.P. [x, y, z].    
        `distance_camera_carbody`: Distance between camera and carbody. y.  
        `distance_camera_ground`: Distance between camera and ground. z.  
        Return list of 4 Points coordinates.  
        Return DATA_TYPE_ERROR when input data type is error.  
        Return DATA_VALUE_ERROR when input data value is error.  
        """
        if not isinstance(camera_coordinates, list) or not isinstance(distance_camera_carbody, float) or not isinstance(distance_camera_ground, float):
            LOGGER.error(f'Input data type error - camera_coordinates, distance_camera_carbody, distance_camera_ground. Data: {camera_coordinates}, {distance_camera_carbody}, {distance_camera_ground}.')
            return self.ReturnCode.DATA_TYPE_ERROR
        
        if not len(camera_coordinates) == 3:
            LOGGER.error(f'Input data value error - camera_coordinates should be a list of 3 elements. Data: {camera_coordinates}.')
            return self.ReturnCode.DATA_VALUE_ERROR
        
        regulation_points = self.cal_model.get_regulation_points_II(camera_coordinates, distance_camera_carbody, distance_camera_ground)
        if regulation_points == self.cal_model.ReturnCode.TYPE_ERROR:
            LOGGER.error(f'Input data type error - camera_coordinates, distance_camera_carbody, distance_camera_ground. Data: {camera_coordinates}, {distance_camera_carbody}, {distance_camera_ground}.')
            return self.ReturnCode.DATA_TYPE_ERROR

        return regulation_points
        
    def transfrom_regulation_points_into_cam_coordinates(self, camera_coordinates: list, regulation_points: list) -> list:
        """ 
        Transform regulation points from E.P. coordinates into camera coordinates.  
        `camera_coordinates`: Camera coordinates.  
        `regulation_points`: List of regulation points - [A, B, C, D]  
        Return list of regulation points coordinates relative to camera.  
        Return DATA_TYPE_ERROR when input data type is error.  
        Return DATA_VALUE_ERROR when input data value is error.  
        """
        if not isinstance(camera_coordinates, list) or not isinstance(regulation_points, list):
            LOGGER.error(f'Input data type error - camera_coordinates, regulation_points. Data: {camera_coordinates}, {regulation_points}.')
            return self.ReturnCode.DATA_TYPE_ERROR
        
        # Transfroming regulation points from E.P. coordinates into camera coordinates.
        regulation_points_camera_coordinates = []
        for point in regulation_points:
            point_camera_coordinates = self.cal_model.coordinate_transform(camera_coordinates, point)
            if point_camera_coordinates == self.cal_model.ReturnCode.TYPE_ERROR: 
                LOGGER.error(f'Input data type error - camera_coordinates, point. Data: {camera_coordinates}, {point}.')
                return self.ReturnCode.DATA_TYPE_ERROR
            
            elif point_camera_coordinates == self.cal_model.ReturnCode.VALUE_ERROR:
                LOGGER.error(f'Input data value error - length of A and B is not equal. Data: {camera_coordinates}, {point}.')
                return self.ReturnCode.DATA_VALUE_ERROR
            
            regulation_points_camera_coordinates.append(point_camera_coordinates)
            
        return regulation_points_camera_coordinates
        
    def regulation_points_world_sensor_transform(self, regulation_points: list, camera_pose: list, sensor_params: list, monitor_params: list, fitting_func_coefs: list) -> list:
        """ 
        Transform regulation points which relative to camera into monitor coordinates.  
        regulation_points: List of regulation points coordinates.  [A, B, C, D...]
        """
        # Make params from list into dict
        camera_pose_dict = { 'pitch' : camera_pose[0], 'yaw' : camera_pose[1], 'roll' : camera_pose[2], }
        sensor_params_dict = { 'width' : sensor_params[0], 'height' : sensor_params[1], 'pixel size' : sensor_params[2], }
        monitor_params_dict = { 'width' : monitor_params[0], 'height' : monitor_params[1], 'pixel size' : monitor_params[2], }
        fitting_func_coefs_dict = { 'x5' : fitting_func_coefs[0], 'x4' : fitting_func_coefs[1], 'x3' : fitting_func_coefs[2], 'x2' : fitting_func_coefs[3], 'x1' : fitting_func_coefs[4], 'x0' : fitting_func_coefs[5], }
        
        # Transform point from world into sensor coordinates.
        regulation_points_sensor_pixel_coordinates = []
        for point in regulation_points:
            point = { 'x' : point[0], 'y' : point[1], 'z' : point[2], } # Point from list to dict
            point_sensor_pixel = functions.world_sensor_transform(point, camera_pose_dict, sensor_params_dict, fitting_func_coefs_dict)['pixel coordinates']
            point_sensor_pixel = [point_sensor_pixel['x'], point_sensor_pixel['y']]
            regulation_points_sensor_pixel_coordinates.append(point_sensor_pixel)
            
        # Move points' original point from center to leftop.
        regulation_points_sensor_pixel_coordinates_leftop = []
        for point in regulation_points_sensor_pixel_coordinates:
            point_converted = functions.move_orignal_point_center_to_leftop(point, sensor_params[0], sensor_params[1])
            regulation_points_sensor_pixel_coordinates_leftop.append(point_converted)
            
        
        
        return regulation_points_sensor_pixel_coordinates_leftop
        
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
        
    def coordinates_transform(self, point: list, old_original_point: list, new_original_point) -> list:
        data = self.cal_model.point_transform_coordinates(point, old_original_point, new_original_point)
        if data == self.cal_model.ReturnCode.TYPE_ERROR:
            LOGGER.error(f'Input data type error - point, old_original_point, new_original_point. Data: {point}, {old_original_point}, {new_original_point}.')
            return self.ReturnCode.DATA_TYPE_ERROR
        elif data == self.cal_model.ReturnCode.VALUE_ERROR:
            LOGGER.error(f'Input data value error - length of point, old_original_point, new_original_point is not equal. Data: {point}, {old_original_point}, {new_original_point}.')
            return self.ReturnCode.DATA_VALUE_ERROR
        
        return data