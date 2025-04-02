# storge.py

import os
import json

def get_file_path(target_filename, input_path):
    """
    Get the file path of the given filename in the given path.  
    `target_filename`: filename for which the path is to be found.  
    `input_path`: path in which the file is to be found.  
    """
    #for dirpath, dirnames, filenames in os.walk(os.path.dirname(__file__)):
    for dirpath, dirnames, filenames in os.walk(os.path.dirname(input_path)):
        if target_filename in filenames:
            output_path = os.path.join(dirpath, target_filename)
            return output_path
        
def load_data_from_json(json_file_path):
        """ 
        Load data from json file.
        If the file does not exist, create it and write the data to it.  
        `data`: data to be loaded. 
        `json_file_path`: path of the json file.
        
        return data: data in memory.  
        return -1: if the file does not exist.  
        """
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as f:
                data = json.load(f) # Data in memory               
                f.close()
                
            return data
                
        else:
            return -1
            
                
def save_data_to_json(data, json_file_path):
    """ 
    Save data from memory to json file.
    """
    if os.path.exists(json_file_path):
        with open(json_file_path, 'w') as f:          
            json.dump(data, f)

            f.close()