import os
import json
from enum import Enum, auto

class JsonStorageModel:
    class ReturnCode(Enum):
        SUCCESS = 0
        FILE_NOT_FOUND = auto()
        DATA_TYPE_INVALID = auto()
    
    def create_empty_json_file(self, filepath, default_data={}):
        try:
            with open(filepath, 'w') as f:
                json.dump(default_data, f)
    
        except FileNotFoundError:
            return self.ReturnCode.FILE_NOT_FOUND
    
        return self.ReturnCode.SUCCESS
    
    def load(self, filepath):
        """
        Load `data` from json file which path is `filepath`.  
        Return `data` dict when success.  
        Return FILE_NOT_FOUND when `filepath` is not exist.  
        """
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                
        except FileNotFoundError:
            return self.ReturnCode.FILE_NOT_FOUND
    
        return data
    
    def save(self, filepath, data: dict):
        """ 
        Save `data` into Json file which path is `filepath`.  
        Return SUCCESS when success.  
        Return FILE_NOT_FOUND and DATA_TYPE_INVAILD when error.  
        """
        if isinstance(data, dict) == False:
            return self.ReturnCode.DATA_TYPE_INVALID
        
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f)

        except FileNotFoundError:
            return self.ReturnCode.FILE_NOT_FOUND
        
        return self.ReturnCode.SUCCESS