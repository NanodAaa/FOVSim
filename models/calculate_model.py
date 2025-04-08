from enum import Enum, auto

class CalculateModel:
    class ReturnCode(Enum):
        OK = 0
        TYPE_ERROR = auto()
        VALUE_ERROR = auto()
    
    def get_regulation_points_II(self, camera_coordinates: list, distance_camera_carbody: float, distance_camera_ground: float) -> list:
        """
        Get coordinates of 4 regulation points relative to E.P.  
        `camera_coordinates': camera_coordinates relative to E.P.  
        'distance_camera_carbody': distance between camera and carbody.    
        Return list of 4 Points coordinates.  
        """
        if not isinstance(camera_coordinates, list) or not isinstance(distance_camera_carbody, float) or not isinstance(distance_camera_ground, float):
            return self.ReturnCode.TYPE_ERROR
        
        z = -abs(camera_coordinates[2] + distance_camera_ground)
        A = [4, -abs(camera_coordinates[1] - distance_camera_carbody), z]
        B = [4, -(abs(camera_coordinates[1] - distance_camera_carbody) + 1), z]
        C = [30, -abs(camera_coordinates[1] - distance_camera_carbody), z]
        D = [30, -(abs(camera_coordinates[1] - distance_camera_carbody) + 5), z]
        
        return [A, B, C, D]
                
    def coordinate_transform(self, A: list, B: list) -> list:
        """
        Transform B so that the original point is A.  
        """
        if not isinstance(A, list) or not isinstance(B, list):
            return self.ReturnCode.TYPE_ERROR
        
        if not len(A) == len(B):
            return self.ReturnCode.VALUE_ERROR
        
        B_convert = [B[0] - A[0], B[1] - A[1], B[2] - A[2]]
        return B_convert
    
    def point_transform_coordinates(self, point: list, old_original_point: list, new_original_point) -> list:
        """
        Transform point from old_original_point to new_original_point.  
        """
        if not isinstance(point, list) or not isinstance(old_original_point, list) or not isinstance(new_original_point, list):
            return self.ReturnCode.TYPE_ERROR
        
        if not len(point) == len(old_original_point) == len(new_original_point):
            return self.ReturnCode.VALUE_ERROR
        
        point_convert = [
            point[0] - (new_original_point[0] - old_original_point[0]),
            point[1] - (new_original_point[1] - old_original_point[1]),
        ]

        return point_convert        
    
    def sensor_monitor_transform(self, sensor_coordinates_pixel: list, sensor_params: list, monitor_params: list):
        """
        Sensor coordinates transform to monitor coordinate, Pixel.  
        `sensor_coordinates_pixel`: [x, y, z]
        `sensor_params`: [witdh, height, pixel size]
        `monitor_params`: [width, height, pixel size]  
        """
        x_m = int(sensor_coordinates_pixel[0] * monitor_params[0] / sensor_params[0])
        y_m = int(sensor_coordinates_pixel[1] * monitor_params[1] / sensor_params[1])
        
        return [x_m, y_m]