# calculate.py

import math
import numpy as np
from cores import W2CTransform as w2c

data = {
        'monitor point a' : { 'x' : 702, 'y' : 270 },
        'monitor point b' : { 'x' : 19, 'y' : 270 },
        'sensor point c' : { 'x' : 0, 'y' : 0 },
        'sensor point c converted' : { 'x' : 0, 'y' : 0 },
        'sensor point c mm' : { 'x' : 0.0, 'y' : 0.0 },
        'sensor point c mm converted' : { 'x' : 0.0, 'y' : 0.0 },
        'sensor point d' : { 'x' : 0, 'y' : 0 },
        'sensor point d converted' : { 'x' : 0, 'y' : 0 },
        'sensor point d mm' : { 'x' : 0.0, 'y' : 0.0 },
        'sensor point d mm converted' : { 'x' : 0.0, 'y' : 0.0 },
        'world point e' : { 'x' : 0.0, 'y' : 0.0, 'z' : 0.0 },
        'world point f' : { 'x' : 0.0, 'y' : 0.0, 'z' : 0.0 },
        'points within ef' : [],
        'points within ef sensor' : [],
        'points within ef monitor' : [],
        'fitting func coefs' : { 'x5' : -6.84e-11, 'x4' : 5.14e-9, 'x3' : -1.12e-6, 'x2' : 4.13e-6, 'x1' : 0.0599, 'x0' : 4.95e-5 },
        'fitting func coefs reverse' : { 'x5' : 0.0103, 'x4' : -0.0589, 'x3' : 0.215, 'x2' : -0.154, 'x1' : 16.8, 'x0' : -0.00596 },
        'camera pose' : { 'pitch' : 0.0, 'yaw' : 0.0, 'roll' : 0.0 },
        'sensor params' : { 'width' : 1920, 'height' : 1536, 'pixel size' : 0.003 },
        'monitor params' : { 'width' : 720, 'height' : 540, 'pixel size' : 0.1521 },
    }

def monitor_sensor_transform(data):
    """ 
    Transform monitor coordinates to sensor coordinates (Pixel format).
    """
    x_a = data['monitor point a']['x']
    y_a = data['monitor point a']['y']
    x_b = data['monitor point b']['x']
    y_b = data['monitor point b']['y']
    
    sensor_param_width = data['sensor params']['width']
    sensor_param_height = data['sensor params']['height']
    sensor_param_pixel_size = data['sensor params']['pixel size']
    
    monitor_param_width = data['monitor params']['width']
    monitor_param_height = data['monitor params']['height']
    
    x_c = int(x_a * ( (sensor_param_width - 0) / (monitor_param_width - 0) ) + 0)
    x_c_mm = round(x_c * sensor_param_pixel_size, 3)
    y_c = int(y_a * ( (sensor_param_height - 0) / (monitor_param_height - 0) ) + 0)
    y_c_mm = round(y_c * sensor_param_pixel_size, 3)
    
    x_d = int(x_b * ( (sensor_param_width - 0) / (monitor_param_width - 0) ) + 0)
    x_d_mm = round(x_d * sensor_param_pixel_size, 3)
    y_d = int(y_b * ( (sensor_param_height - 0) / (monitor_param_height - 0) ) + 0)
    y_d_mm = round(y_d * sensor_param_pixel_size, 3)
    
    data['sensor point c'] = { 'x' : x_c, 'y' : y_c }
    data['sensor point c mm'] = { 'x' : x_c_mm, 'y' : y_c_mm }
    data['sensor point d'] = { 'x' : x_d, 'y' : y_d }
    data['sensor point d mm'] = { 'x' : x_d_mm, 'y' : y_d_mm }
    
    return data

def sensor_monitor_transform(data):
    
    return

def sensor_origin_point_convert(data):
    """ 
    Convert sensor coordinates to origin coordinates.
    """
    x_c = data['sensor point c']['x']
    y_c = data['sensor point c']['y']
    x_d = data['sensor point d']['x']
    y_d = data['sensor point d']['y']
    
    sensor_param_width = data['sensor params']['width']
    sensor_param_height = data['sensor params']['height']
    sensor_param_pixel_size = data['sensor params']['pixel size']
    
    x_c_converted = int(x_c - sensor_param_width / 2)
    y_c_converted = int(y_c - sensor_param_height / 2)
    x_d_converted = int(x_d - sensor_param_width / 2)
    y_d_converted = int(y_d - sensor_param_height / 2)
    
    x_c_mm_converted = round(x_c_converted * sensor_param_pixel_size, 3)
    y_c_mm_converted = round(y_c_converted * sensor_param_pixel_size, 3)
    x_d_mm_converted = round(x_d_converted * sensor_param_pixel_size, 3)
    y_d_mm_converted = round(y_d_converted * sensor_param_pixel_size, 3)
    
    data['sensor point c converted'] = { 'x' : x_c_converted, 'y' : y_c_converted }
    data['sensor point c mm converted'] = { 'x' : x_c_mm_converted, 'y' : y_c_mm_converted }
    data['sensor point d converted'] = { 'x' : x_d_converted, 'y' : y_d_converted }
    data['sensor point d mm converted'] = { 'x' : x_d_mm_converted, 'y' : y_d_mm_converted }
    
    return data

def sensor_world_transform(data):
    # Sensor coordinates to Camera coordinatess
    data['world point e'] = w2c.sensor_world_transform(data['sensor point d mm converted'], data['fitting func coefs reverse'])['world coordinates']
    data['world point f'] = w2c.sensor_world_transform(data['sensor point c mm converted'], data['fitting func coefs reverse'])['world coordinates']

    return data

def insert_points_into_range(data):
    points = w2c.insert_point_into_range((data['world point e']['y'], data['world point f']['y']), 20)
    points_within_ef = []
    for point in points:
        points_within_ef.append({ 'x' : data['world point e']['x'], 'y' : point, 'z' : data['world point e']['z'], })
    
    data['points within ef'] = tuple(points_within_ef)
    return data

def points_world_sensor_transform(data):
    """ 
    """
    points = data['points within ef']
    points_sensor = []
    for point in points:
        point_sensor = w2c.world_sensor_transform(point, data['camera pose'], data['sensor params'], data['fitting func coefs'])['sensor coordinates']
        points_sensor.append(point_sensor)
    
    data['points within ef sensor'] = points_sensor
    
    return data