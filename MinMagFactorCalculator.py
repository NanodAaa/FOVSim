# MinMagFactorCalculator.py
from gui import main_window as mw

""" data = {
        'monitor point a' : { 'x' : 702, 'y' : 270},
        'monitor point b' : { 'x' : 19, 'y' : 270},
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
        'fitting func coefs' : { 'x5' : '-6.84e-11', 'x4' : '5.14e-9', 'x3' : '-1.12e-6', 'x2' : '4.13e-6', 'x1' : '0.0599', 'x0' : '4.95e-5' },
        'fitting func coefs reverse' : { 'x5' : '0.0103', 'x4' : '-0.0589', 'x3' : '0.215', 'x2' : '-0.154', 'x1' : '16.8', 'x0' : '-0.00596' },
        'camera pose' : { 'pitch' : '0.0', 'yaw' : '0.0', 'roll' : '0.0' },
        'sensor params' : { 'width' : '1920', 'height' : '1536', 'pixel size' : '0.003' },
        'monitor params' : { 'width' : '720', 'height' : '540', 'pixel size' : '0.1521' },
    } """

if __name__ == '__main__':
    main_window = mw.MainWindow('root')