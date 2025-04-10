from models.storage_model import JsonStorageModel
from models.config_model import ConfigModel
from models.config_model import LOGGER
from enum import Enum, auto
from models.calculate_model import CalculateModel
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
        # Class II - Driver side.
        data = self.json_save_model.load(self.config_model.setting_2_driver_filepath)
        if data == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            return self.ReturnCode.FILE_NOT_FOUND
        
        # If data is empty or {} write default data.
        if data is None or data == {} or not isinstance(data, dict):
            result = self.json_save_model.save(filepath=self.config_model.setting_2_driver_filepath, data=self.config_model.default_setting_2_driver)
            if result == self.json_save_model.ReturnCode.DATA_TYPE_INVALID:
                LOGGER.error('Error when write data into json! - Data type error')
                return self.ReturnCode.DATA_TYPE_ERROR
            elif result == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
                LOGGER.error('Error when write data into json! - File not found.')
                return self.ReturnCode.FILE_NOT_FOUND
            
        # Class II - Passenger side.
        data = self.json_save_model.load(self.config_model.setting_2_passanger_filepath)
        if data == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            return self.ReturnCode.FILE_NOT_FOUND
        
        # If data is empty or {} write default data.
        if data is None or data == {} or not isinstance(data, dict):
            result = self.json_save_model.save(filepath=self.config_model.setting_2_passanger_filepath, data=self.config_model.default_setting_2_passanger)
            if result == self.json_save_model.ReturnCode.DATA_TYPE_INVALID:
                LOGGER.error('Error when write data into json! - Data type error')
                return self.ReturnCode.DATA_TYPE_ERROR
            elif result == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
                LOGGER.error('Error when write data into json! - File not found.')
                return self.ReturnCode.FILE_NOT_FOUND
        
        # Class IV - Driver side.
        data = self.json_save_model.load(self.config_model.setting_4_driver_filepath)
        if data == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            return self.ReturnCode.FILE_NOT_FOUND
        
        # If data is empty or {} write default data.
        if data is None or data == {} or not isinstance(data, dict):
            result = self.json_save_model.save(filepath=self.config_model.setting_4_driver_filepath, data=self.config_model.default_setting_4_driver)
            if result == self.json_save_model.ReturnCode.DATA_TYPE_INVALID:
                LOGGER.error('Error when write data into json! - Data type error')
                return self.ReturnCode.DATA_TYPE_ERROR
            elif result == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
                LOGGER.error('Error when write data into json! - File not found.')
                return self.ReturnCode.FILE_NOT_FOUND
            
        # Class IV - Passenger side.
        data = self.json_save_model.load(self.config_model.setting_4_passanger_filepath)
        if data == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            return self.ReturnCode.FILE_NOT_FOUND
        
        # If data is empty or {} write default data.
        if data is None or data == {} or not isinstance(data, dict):
            result = self.json_save_model.save(filepath=self.config_model.setting_4_passanger_filepath, data=self.config_model.default_setting_4_passanger)
            if result == self.json_save_model.ReturnCode.DATA_TYPE_INVALID:
                LOGGER.error('Error when write data into json! - Data type error')
                return self.ReturnCode.DATA_TYPE_ERROR
            elif result == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
                LOGGER.error('Error when write data into json! - File not found.')
                return self.ReturnCode.FILE_NOT_FOUND
    
    def get_regulation_points(self, camera_coordinates: list, distance_camera_carbody: float, distance_camera_ground: float, profile: str) -> list:
        """ 
        """
        if profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_II_DRIVER.value:
            return self._get_regulation_points_II_driver_ep(camera_coordinates, distance_camera_carbody, distance_camera_ground)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_II_PASSANGER.value:
            return self._get_regulation_points_II_passanger_ep(camera_coordinates, distance_camera_carbody, distance_camera_ground)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_IV_DRIVER.value:
            return self.get_regulation_points_IV_driver_ep(camera_coordinates, distance_camera_carbody, distance_camera_ground)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_IV_PASSANGER.value:
            return self.get_regulation_points_IV_passanger_ep(camera_coordinates, distance_camera_carbody, distance_camera_ground)
        else:
            LOGGER.error('Error when get regulation points! - Profile not found.')
            return None
        
    def _get_regulation_points_II_driver_ep(self, camera_coordinates: list, distance_camera_carbody: float, distance_camera_ground: float) -> list:
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
        
        regulation_points = self.cal_model.get_regulation_points_II_driver(camera_coordinates, distance_camera_carbody, distance_camera_ground)
        if regulation_points == self.cal_model.ReturnCode.TYPE_ERROR:
            LOGGER.error(f'Input data type error - camera_coordinates, distance_camera_carbody, distance_camera_ground. Data: {camera_coordinates}, {distance_camera_carbody}, {distance_camera_ground}.')
            return self.ReturnCode.DATA_TYPE_ERROR

        return regulation_points
    
    def _get_regulation_points_II_passanger_ep(self, camera_coordinates: list, distance_camera_carbody: float, distance_camera_ground: float) -> list:
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
        
        regulation_points = self.cal_model.get_regulation_points_II_passanger(camera_coordinates, distance_camera_carbody, distance_camera_ground)
        if regulation_points == self.cal_model.ReturnCode.TYPE_ERROR:
            LOGGER.error(f'Input data type error - camera_coordinates, distance_camera_carbody, distance_camera_ground. Data: {camera_coordinates}, {distance_camera_carbody}, {distance_camera_ground}.')
            return self.ReturnCode.DATA_TYPE_ERROR
        
        return regulation_points
    
    def get_regulation_points_IV_driver_ep(self, camera_coordinates: list, distance_camera_carbody: float, distance_camera_ground: float) -> list:
        pass
    
    def get_regulation_points_IV_passanger_ep(self, camera_coordinates: list, distance_camera_carbody: float, distance_camera_ground: float) -> list:
        pass
        
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
        
    def read_data_from_json(self, profile: str) -> dict:
        """ 
        Read data from json.  
        Return FILE_NOT_FOUND when json file does not exist.  
        Return data when success.  
        """
        if profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_II_DRIVER.value:
            data = self.json_save_model.load(self.config_model.setting_2_driver_filepath)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_II_PASSANGER.value:
            data = self.json_save_model.load(self.config_model.setting_2_passanger_filepath)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_IV_DRIVER.value:
            data = self.json_save_model.load(self.config_model.setting_4_driver_filepath)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_IV_PASSANGER.value:
            data = self.json_save_model.load(self.config_model.setting_4_passanger_filepath)
        else:
            LOGGER.error('Error when load data from json! - Profile not found.')
            return self.ReturnCode.FILE_NOT_FOUND
        
        if data == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            return self.ReturnCode.FILE_NOT_FOUND
        
        return data
    
    def save_data_to_json(self, data: dict, profile: str):
        """ 
        Receive data from view and save it to json file.
        """
        # If data is not a list, raise TypeError
        if not isinstance(data, dict):
            LOGGER.error('data_list should be a dict!')
            return self.ReturnCode.DATA_TYPE_ERROR
        
        """ # Check data in data_list.
        for data in data_list:
            if not isinstance(data, dict):
                LOGGER.error('data in data_list should be a dict!')
                raise TypeError('data in data_list should be a dict!')
            
            if not len(list(data.keys())) == 1:
                LOGGER.error('data in data_list can have only 1 key!')
                raise ValueError('data in data_list can have only 1 key!')
                
            if not len(list(data.values())) == 1:
                LOGGER.error('data in data_list can have only 1 value!')
                raise ValueError('data in data_list can have only 1 value!')
                
            if not isinstance(next(iter(data.values())), list):
                LOGGER.error('value in data should be a list!')
                raise TypeError('value in data should be a list!') """

        # Write data into json
        if profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_II_DRIVER.value:
            result = self.json_save_model.save(filepath=self.config_model.setting_2_driver_filepath, data=data)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_II_PASSANGER.value:
            result = self.json_save_model.save(filepath=self.config_model.setting_2_passanger_filepath, data=data)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_IV_DRIVER.value:
            result = self.json_save_model.save(filepath=self.config_model.setting_4_driver_filepath, data=data)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_IV_PASSANGER.value:
            result = self.json_save_model.save(filepath=self.config_model.setting_4_passanger_filepath, data=data)
        else:
            LOGGER.error('Error when write data into json! - Profile not found.')
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
    
    def sensor_monitor_transform(self, sensor_coordinates_pixel: list, sensor_params: list, monitor_params: list):
        """
        Sensor coordinates transform to monitor coordinate, Pixel.  
        `sensor_coordinates_pixel`: [x, y, z]
        `sensor_params`: [witdh, height, pixel size]
        `monitor_params`: [width, height, pixel size]  
        """
        data = self.cal_model.sensor_monitor_transform(sensor_coordinates_pixel, sensor_params, monitor_params)
        if data == self.cal_model.ReturnCode.TYPE_ERROR:
            LOGGER.error(f'Input data type error - sensor_coordinates_pixel, sensor_params, monitor_params. Data: {sensor_coordinates_pixel}, {sensor_params}, {monitor_params}.')
            return self.ReturnCode.DATA_TYPE_ERROR
        elif data == self.cal_model.ReturnCode.VALUE_ERROR:
            LOGGER.error(f'Input data value error - length of sensor_coordinates_pixel, sensor_params, monitor_params is not equal. Data: {sensor_coordinates_pixel}, {sensor_params}, {monitor_params}.')
            return self.ReturnCode.DATA_VALUE_ERROR
        
        return data