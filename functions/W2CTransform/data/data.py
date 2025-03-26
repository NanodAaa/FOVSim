class Data:
    data_filename = 'data.json'
    data_filepath = f'./functions/W2CTransform/data/{data_filename}'
    data = {
        'world coordinates' : { 'x' : '', 'y' : '', 'z' : '' },
        'fitting func coefs' : { 'x5' : '', 'x4' : '', 'x3' : '', 'x2' : '', 'x1' : '', 'x0' : '' },
        'fitting func coefs reverse' : { 'x5' : '', 'x4' : '', 'x3' : '', 'x2' : '', 'x1' : '', 'x0' : '' },
        'camera pose' : { 'pitch' : '', 'yaw' : '', 'roll' : '' },
        'sensor params' : { 'width' : '', 'height' : '', 'pixel size' : '' },
        'camera coordinates' : { 'x' : '', 'y' : '', 'z' : '' },
        'pixel coordinates' : { 'x' : '', 'y' : '' },
    }