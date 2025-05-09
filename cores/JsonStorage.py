import os
import json

class JsonStorage:
    """
    A class to handle JSON file storage operations, including:
    - Loading data from a JSON file.
    - Saving data to a JSON file.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(filepath):
            # If the file does not exist            
            self._create_empty_json_file()

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
        with open(self.filepath, 'r') as f:
            data = json.load(f)
            f.close()
        
        return data
    
    def save(self, data):
        """ 
        Save data from memory to a JSON file.
        `data`: data to be saved.
        """
        with open(self.filepath, 'w') as f:
            json.dump(data, f)
            f.close()
        
        return