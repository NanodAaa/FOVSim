import math
import numpy as np

def coordinates_pixel_to_mm(point_coordinates: dict, pixel_size):
    """ 
    Converting coordinates from pixel to mm.  
    `point_coordinates`: { 'x': x, 'y' : y, 'z' : z }  
    `pixel_size`: pixel size.  
    return: point_coordinates_mm = { 'x' : x_mm, 'y' : y_mm }  
    """
    x = point_coordinates['x']
    y = point_coordinates['y']

    x_mm = round(x * pixel_size, 3)
    y_mm = round(y * pixel_size, 3)
    
    point_coordinates_mm = { 'x' : x_mm, 'y' : y_mm, }
    
    return point_coordinates_mm

def coordinates_mm_to_pixel(point_coordinates: dict, pixel_size):
    """ 
    Converting coordinates from mm to pixel.  
    `point_coordinates`: { 'x': x, 'y' : y, 'z' : z }  
    `pixel_size`: pixel size.  
    return: point_coordinates_pixel = { 'x' : x_pixel, 'y' : y_pixel}  
    """
    x = point_coordinates['x']
    y = point_coordinates['y']
    
    x_pixel = int(x / pixel_size)
    y_pixel = int(y / pixel_size)
    
    point_coordinates_pixel = { 'x' : x_pixel, 'y' : y_pixel, }
    
    return point_coordinates_pixel

def sensor_monitor_transform(sensor_coordinates_pixel: dict, sensor_params: dict, monitor_params: dict):
    """
    Sensor coordinates transform to monitor coordinate, Pixel.  
    `sensor_coordinates_pixel`: { 'x', 'y', 'z', }  
    `sensor_params`: { 'width', 'height', 'pixel size', }  
    `monitor_params`: { 'width', 'height', 'pixel size', }  
    """
    x_m = int(sensor_coordinates_pixel['x'] * monitor_params['width'] / sensor_params['width'])
    y_m = int(sensor_coordinates_pixel['y'] * monitor_params['height'] / sensor_params['height'])

    return { 'x' : x_m, 'y' : y_m, }

def sensor_world_transform(sensor_coordinates_mm_converted: dict, fitting_func_coefs_reverse_dict: dict, x_c=2000):
    """ 
    Sensor coordinates to World coordinates.  
    `sensor_coordinates_mm_converted`: Dict of x and y in sensor_mm_coordinates.  
    `fitting_func_coefs_reverse_dict`: Dict of fitting function coefficients reverse (RealHeight vs Angle).  
    return: Dict of world coordinates and camera coordinates.  
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

def insert_point_into_range(range: tuple, points_num: int):
    """ 
    Insert points into range.  
    `range`: tuple of range.  
    `points_num`: number of points to insert.  
    return: list of points.  
    """
    points = np.round(np.linspace(range[0], range[1], points_num), 3)
    return points

def world_sensor_transform(world_coordinates: dict, camera_pose: dict, sensor_params: dict, fitting_func_coefs: dict):
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
    
    pitch_radians = math.radians(camera_pose['pitch'])
    yaw_radians = math.radians(camera_pose['yaw'])
    roll_radians = math.radians(camera_pose['roll'])
    
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
    x_s = round((real_height) * math.cos(azimuth_radians), 3)
    y_s = round((real_height) * math.sin(azimuth_radians), 3)
    x_p = int((real_height / pixel_size) * math.cos(azimuth_radians))
    y_p = int((real_height / pixel_size) * math.sin(azimuth_radians))
    
    # Write data to memory
    data = {}
    data['camera coordinates'] = { 'x' : x_c, 'y' : y_c, 'z' : z_c, }
    data['sensor coordinates'] = { 'x' : x_s, 'y' : y_s, }
    data['pixel coordinates'] = { 'x' : x_p, 'y' : y_p, }
    
    return data