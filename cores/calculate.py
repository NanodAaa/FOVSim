# calculate.py
""" 
Data structure:
data = {
        'monitor point a' : { 'x' : '0', 'y' : '0'},
        'monitor point b' : { 'x' : '0', 'y' : '0'},
        'sensor point c' : { 'x' : '0', 'y' : '0'},
        'sensor point c converted' : { 'x' : '0', 'y' : '0'},
        'sensor point c mm' : { 'x' : '0.0', 'y' : '0.0'},
        'sensor point c mm converted' : { 'x' : '0.0', 'y' : '0.0'},
        'sensor point d' : { 'x' : '0', 'y' : '0'},
        'sensor point d converted' : { 'x' : '0', 'y' : '0'},
        'sensor point d mm' : { 'x' : '0.0', 'y' : '0.0'},
        'sensor point d mm converted' : { 'x' : '0.0', 'y' : '0.0'},
        'world point e' : { 'x' : '0.0', 'y' : '0.0', 'z' : '0.0'},
        'world point f' : { 'x' : '0.0', 'y' : '0.0', 'z' : '0.0'},
        'fitting func coefs' : { 'x5' : '0.0', 'x4' : '0.0', 'x3' : '0.0', 'x2' : '0.0', 'x1' : '0.0', 'x0' : '0.0' },
        'fitting func coefs reverse' : { 'x5' : '0.0', 'x4' : '0.0', 'x3' : '0.0', 'x2' : '0.0', 'x1' : '0.0', 'x0' : '0.0' },
        'camera pose' : { 'pitch' : '0.0', 'yaw' : '0.0', 'roll' : '0.0' },
        'sensor params' : { 'width' : '0', 'height' : '0', 'pixel size' : '0.0' },
        'monitor params' : { 'width' : '0', 'height' : '0', 'pixel size' : '0.0' },
    }
"""

import math
import numpy as np
from cores import W2CTransform as w2c

data = {
        'monitor point a' : { 'x' : '0', 'y' : '0'},
        'monitor point b' : { 'x' : '0', 'y' : '0'},
        'sensor point c' : { 'x' : '0', 'y' : '0'},
        'sensor point c converted' : { 'x' : '0', 'y' : '0'},
        'sensor point c mm' : { 'x' : '0.0', 'y' : '0.0'},
        'sensor point c mm converted' : { 'x' : '0.0', 'y' : '0.0'},
        'sensor point d' : { 'x' : '0', 'y' : '0'},
        'sensor point d converted' : { 'x' : '0', 'y' : '0'},
        'sensor point d mm' : { 'x' : '0.0', 'y' : '0.0'},
        'sensor point d mm converted' : { 'x' : '0.0', 'y' : '0.0'},
        'world point e' : { 'x' : '0.0', 'y' : '0.0', 'z' : '0.0'},
        'world point f' : { 'x' : '0.0', 'y' : '0.0', 'z' : '0.0'},
        'fitting func coefs' : { 'x5' : '0.0', 'x4' : '0.0', 'x3' : '0.0', 'x2' : '0.0', 'x1' : '0.0', 'x0' : '0.0' },
        'fitting func coefs reverse' : { 'x5' : '0.0', 'x4' : '0.0', 'x3' : '0.0', 'x2' : '0.0', 'x1' : '0.0', 'x0' : '0.0' },
        'camera pose' : { 'pitch' : '0.0', 'yaw' : '0.0', 'roll' : '0.0' },
        'sensor params' : { 'width' : '0', 'height' : '0', 'pixel size' : '0.0' },
        'monitor params' : { 'width' : '0', 'height' : '0', 'pixel size' : '0.0' },
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
    x_c_mm = round(x_c * sensor_param_pixel_size, 2)
    y_c = int(y_a * ( (sensor_param_height - 0) / (monitor_param_height - 0) ) + 0)
    y_c_mm = round(y_c * sensor_param_pixel_size, 2)
    
    x_d = int(x_b * ( (sensor_param_width - 0) / (monitor_param_width - 0) ) + 0)
    x_d_mm = round(x_d * sensor_param_pixel_size, 2)
    y_d = int(y_b * ( (sensor_param_height - 0) / (monitor_param_height - 0) ) + 0)
    y_d_mm = round(y_d * sensor_param_pixel_size, 2)
    
    data['sensor point c'] = { 'x' : x_c, 'y' : y_c }
    data['sensor point c mm'] = { 'x' : x_c_mm, 'y' : y_c_mm }
    data['sensor point d'] = { 'x' : x_d, 'y' : y_d }
    data['sensor point d mm'] = { 'x' : x_d_mm, 'y' : y_d_mm }
    
    return data

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
    
    x_c_mm_converted = round(x_c_converted * sensor_param_pixel_size, 2)
    y_c_mm_converted = round(y_c_converted * sensor_param_pixel_size, 2)
    x_d_mm_converted = round(x_d_converted * sensor_param_pixel_size, 2)
    y_d_mm_converted = round(y_d_converted * sensor_param_pixel_size, 2)
    
    data['sensor point c converted'] = { 'x' : x_c_converted, 'y' : y_c_converted }
    data['sensor point c mm converted'] = { 'x' : x_c_mm_converted, 'y' : y_c_mm_converted }
    data['sensor point d converted'] = { 'x' : x_d_converted, 'y' : y_d_converted }
    data['sensor point d mm converted'] = { 'x' : x_d_mm_converted, 'y' : y_d_mm_converted }
    
    return data

def sensor_world_transform(data):
    # Sensor coordinates to Camera coordinatess
    data['world point e'] = w2c.sensor_world_transform(data['sensor point c mm converted'], data['fitting func coefs reverse'])
    data['world point f'] = w2c.sensor_world_transform(data['sensor point d mm converted'], data['fitting func coefs reverse'])

    return data