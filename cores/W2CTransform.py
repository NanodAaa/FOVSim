# W2CTransform.py

import math
import numpy as np

def sensor_world_transform(sensor_coordinates_mm_converted: dict, fitting_func_coefs_reverse_dict: dict):
    """ 
    Sensor coordinates to World coordinates.  
    `sensor_coordinates_mm`: tuple of x and y pixel coordinates.  
    `fitting_func_coefs_reverse_dict`: dictionary of fitting function coefficients.  
    return: dictionary of world coordinates and camera coordinates.  
    data = {
        'camera coordinates' : { 'x' : x_w, 'y' : y_c, 'z' : z_c },
        'world coordinates' : {'x' : x_s, 'y' : y_s, 'z' : z_p },
    }
    """
    # Sensor coordinates to World coordinates
    x_s = sensor_coordinates_mm_converted['x']
    y_s = sensor_coordinates_mm_converted['y']
    
    fitting_func_coefs_reverse = [
        fitting_func_coefs_reverse_dict['x5'], 
        fitting_func_coefs_reverse_dict['x4'], 
        fitting_func_coefs_reverse_dict['x3'], 
        fitting_func_coefs_reverse_dict['x2'], 
        fitting_func_coefs_reverse_dict['x1'], 
        fitting_func_coefs_reverse_dict['x0'],
    ]
    
    x_c = 2000
    
    real_height = math.sqrt(x_s**2 + y_s**2)
    azimuth_on_sensor = (math.degrees(math.atan2(x_s, -y_s)) + 270) % 360 
    angle = np.polyval(fitting_func_coefs_reverse, real_height)
    distance = math.tan(math.radians(angle)) * x_c # Distance from nodal point of world coordinates
    y_c = round(distance * math.cos(math.radians(azimuth_on_sensor)), 3)
    z_c = round(distance * math.sin(math.radians(azimuth_on_sensor)), 3)
    
    x_w = x_c
    y_w = y_c
    z_w = z_c
    
    # Write data to memory
    data = {
        'camera coordinates' : { 'x' : x_w, 'y' : y_c, 'z' : z_c },
        'world coordinates' : {'x' : x_w, 'y' : y_w, 'z' : z_w },
    }

    return data

def world_sensor_transform(world_coordinates: dict, sensor_params: dict, fitting_func_coefs: dict):
    """ 
    Transform world coordinates to sensor coordinates (Pixel format).  
    `world_coordinates`: dictionary of world coordinates.  
    `sensor_params`: dictionary of sensor parameters.  
    `fitting_func_coefs`: dictionary of fitting function coefficients.  
    return: dictionary of sensor coordinates.  
    """
    # World coordinates to Camera coordinates
    x_w = world_coordinates['x']
    y_w = world_coordinates['y']
    z_w = world_coordinates['z']
    
    world_coordinates_vector = np.array(
        [
            [x_w],
            [y_w],
            [z_w],
        ]
    )
    
    pitch_radians = math.radians(sensor_params['pitch'])
    yaw_radians = math.radians(sensor_params['yaw'])
    roll_radians = math.radians(sensor_params['roll'])
    
    pitch_rotate_matrix = np.array(
        [
            [math.cos(pitch_radians), 0, math.sin(pitch_radians)],
            [0, 1, 0],
            [-math.sin(pitch_radians), 0, math.cos(pitch_radians)],
        ]
    )
    
    yaw_rotate_matrix = np.array(
        [
            [math.cos(yaw_radians), -math.sin(yaw_radians), 0],
            [math.sin(yaw_radians), math.cos(yaw_radians), 0],
            [0, 0, 1],
        ]
    )
    
    roll_rotate_matrix = np.array(
        [
            [1, 0, 0],
            [0, math.cos(roll_radians), -math.sin(roll_radians)],
            [0, math.sin(roll_radians), math.cos(roll_radians)],
        ]
    )
    
    world_coordinates_vector_pitched = np.dot(pitch_rotate_matrix, world_coordinates_vector)
    world_coordinates_vector_pitched_yawed = np.dot(yaw_rotate_matrix, world_coordinates_vector_pitched)
    world_coordinates_vector_pitched_yawed_rolled = np.dot(roll_rotate_matrix, world_coordinates_vector_pitched_yawed)

    x_c = round(float(world_coordinates_vector_pitched_yawed_rolled[0][0]), 3)
    y_c = round(float(world_coordinates_vector_pitched_yawed_rolled[1][0]), 3)
    z_c = round(float(world_coordinates_vector_pitched_yawed_rolled[2][0]), 3)
    
    # Camera coordinates to Pixel coordinates
    distance = math.sqrt(x_c**2 + y_c**2 + z_c**2) # Distance to nodal point
    angle = math.degrees(math.acos(x_c / distance))
    fitting_func_coefs = [fitting_func_coefs['x5'], fitting_func_coefs['x4'], fitting_func_coefs['x3'], fitting_func_coefs['x2'], fitting_func_coefs['x1'], fitting_func_coefs['x0']]
    real_height = np.polyval(fitting_func_coefs, angle)
    azimuth_radians = math.atan2(z_c, -y_c)
    azimuth = (math.degrees(azimuth_radians) + 360 ) % 360
    
    pixel_size = sensor_params['pixel size']
    x_p = round((real_height / pixel_size) * math.cos(azimuth_radians), 3)
    y_p = round((real_height / pixel_size) * math.sin(azimuth_radians), 3)
    
    # Write data to memory
    data = {}
    data['camera coordinates'] = { 'x' : x_c, 'y' : y_c, 'z' : z_c }
    data['pixel coordinates'] = { 'x' : x_p, 'y' : y_p }
    
    return