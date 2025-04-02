from enum import Enum, auto
import math

class CalculateModel:
    class ReturnCode(Enum):
        OK = 0
        TYPE_ERROR = auto()
        VALUE_ERROR = auto()
    
    def get_regulation_points(self, camera_coordinates: list, distance_camera_carbody: float):
        """
        Get coordinates of 4 regulation points relative to E.P..  
        `camera_coordinates': camera_coordinates relative to E.P.  
        'distance_camera_carbody': distance between camera and carbody.    
        """
        if not isinstance(camera_coordinates, list) or not isinstance(distance_camera_carbody, float):
            return self.ReturnCode.TYPE_ERROR
        
        A = [4, -abs(camera_coordinates[1] - distance_camera_carbody)]
        B = [4, -(abs(camera_coordinates[1] - distance_camera_carbody) + 1)]
        C = [30, -abs(camera_coordinates[1] - distance_camera_carbody)]
        D = [30, -(abs(camera_coordinates[1] - distance_camera_carbody) + 5)]
                
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
        