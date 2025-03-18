import os
import sys
import json

class JsonStorage:
    """
    A class to handle JSON file storage operations, including:
    - Loading data from a JSON file.
    - Saving data to a JSON file.
    """
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
    
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(filepath):
            self._create_empty_json_file()
            
        return
            
    def _create_empty_json_file(self):
        """ 
        Create an empty JSON file.
        """
        with open(self.filepath, 'w') as f:
            json.dump({}, f)
            f.close()
            
        return
    
    def load(self):
        """ 
        Load data from a JSON file.
        return: data in memory.
        """
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                data = json.load(f)
                f.close()
            
            return data
        
        else:
            return -1
    
    def save(self, data):
        """ 
        Save data from memory to a JSON file.
        `data`: data to be saved.
        """
        if os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump(data, f)
                f.close()
            
            return
        else:
            return -1