from models.storage_model import JsonStorageModel
from models.config_model import ConfigModel
from models.config_model import LOGGER
from enum import Enum, auto

class SettingWindowController:
    class ReturnCode(Enum):
        SUCCESS = 0
        FILE_NOT_FOUND = auto()
        DATA_TYPE_ERROR = auto()
    
    def __init__(self):
        self.config_model = ConfigModel()
        self.json_save_model = JsonStorageModel()
    
    def init_setting_data(self):
        """ 
        Initialize setting data.
        """
        # Class II - Driver side.
        data = self.json_save_model.load(self.config_model.setting_2_driver_filepath)
        if data == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            return self.ReturnCode.FILE_NOT_FOUND
        
        # If data is empty or {} write default data.
        if data is None or data == {} or not isinstance(data, dict):
            result = self.json_save_model.save(filepath=self.config_model.setting_2_driver_filepath, data=self.config_model.default_setting_2_driver)
            if result == self.json_save_model.ReturnCode.DATA_TYPE_INVALID:
                LOGGER.error('Error when write data into json! - Data type error')
                return self.ReturnCode.DATA_TYPE_ERROR
            elif result == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
                LOGGER.error('Error when write data into json! - File not found.')
                return self.ReturnCode.FILE_NOT_FOUND
            
        # Class II - Passenger side.
        data = self.json_save_model.load(self.config_model.setting_2_passanger_filepath)
        if data == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            return self.ReturnCode.FILE_NOT_FOUND
        
        # If data is empty or {} write default data.
        if data is None or data == {} or not isinstance(data, dict):
            result = self.json_save_model.save(filepath=self.config_model.setting_2_passanger_filepath, data=self.config_model.default_setting_2_passanger)
            if result == self.json_save_model.ReturnCode.DATA_TYPE_INVALID:
                LOGGER.error('Error when write data into json! - Data type error')
                return self.ReturnCode.DATA_TYPE_ERROR
            elif result == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
                LOGGER.error('Error when write data into json! - File not found.')
                return self.ReturnCode.FILE_NOT_FOUND
        
        # Class IV - Driver side.
        data = self.json_save_model.load(self.config_model.setting_4_driver_filepath)
        if data == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            return self.ReturnCode.FILE_NOT_FOUND
        
        # If data is empty or {} write default data.
        if data is None or data == {} or not isinstance(data, dict):
            result = self.json_save_model.save(filepath=self.config_model.setting_4_driver_filepath, data=self.config_model.default_setting_4_driver)
            if result == self.json_save_model.ReturnCode.DATA_TYPE_INVALID:
                LOGGER.error('Error when write data into json! - Data type error')
                return self.ReturnCode.DATA_TYPE_ERROR
            elif result == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
                LOGGER.error('Error when write data into json! - File not found.')
                return self.ReturnCode.FILE_NOT_FOUND
            
        # Class IV - Passenger side.
        data = self.json_save_model.load(self.config_model.setting_4_passanger_filepath)
        if data == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            return self.ReturnCode.FILE_NOT_FOUND
                
    def save_data_to_json(self, data: dict, profile: str):
        """ 
        Receive data from view and save it to json file.
        """
        # If data is not a list, raise TypeError
        if not isinstance(data, dict):
            LOGGER.error('data_list should be a dict!')
            return self.ReturnCode.DATA_TYPE_ERROR
        
        """ # Check data in data_list.
        for data in data_list:
            if not isinstance(data, dict):
                LOGGER.error('data in data_list should be a dict!')
                raise TypeError('data in data_list should be a dict!')
            
            if not len(list(data.keys())) == 1:
                LOGGER.error('data in data_list can have only 1 key!')
                raise ValueError('data in data_list can have only 1 key!')
                
            if not len(list(data.values())) == 1:
                LOGGER.error('data in data_list can have only 1 value!')
                raise ValueError('data in data_list can have only 1 value!')
                
            if not isinstance(next(iter(data.values())), list):
                LOGGER.error('value in data should be a list!')
                raise TypeError('value in data should be a list!') """

        # Write data into json
        if profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_II_DRIVER.value:
            result = self.json_save_model.save(filepath=self.config_model.setting_2_driver_filepath, data=data)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_II_PASSANGER.value:
            result = self.json_save_model.save(filepath=self.config_model.setting_2_passanger_filepath, data=data)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_IV_DRIVER.value:
            result = self.json_save_model.save(filepath=self.config_model.setting_4_driver_filepath, data=data)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_IV_PASSANGER.value:
            result = self.json_save_model.save(filepath=self.config_model.setting_4_passanger_filepath, data=data)
        else:
            LOGGER.error('Error when write data into json! - Profile not found.')
            return self.ReturnCode.FILE_NOT_FOUND
            
        
    def read_data_from_json(self, profile: str) -> dict:
        """ 
        Read data from json.  
        Return FILE_NOT_FOUND when json file does not exist.  
        Return data when success.  
        """
        """ data = self.json_save_model.load(self.config_model.setting_filepath)
        if data == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            return self.ReturnCode.FILE_NOT_FOUND """
    
        if profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_II_DRIVER.value:
            data = self.json_save_model.load(self.config_model.setting_2_driver_filepath)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_II_PASSANGER.value:
            data = self.json_save_model.load(self.config_model.setting_2_passanger_filepath)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_IV_DRIVER.value:
            data = self.json_save_model.load(self.config_model.setting_4_driver_filepath)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_IV_PASSANGER.value:
            data = self.json_save_model.load(self.config_model.setting_4_passanger_filepath)
        else:
            LOGGER.error('Error when load data from json! - Profile not found.')
            return self.ReturnCode.FILE_NOT_FOUND
        
        if data == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            return self.ReturnCode.FILE_NOT_FOUND
    
        return data
    
    def reset_default_setting(self, profile: str):
        """ 
        Reset default setting data.
        """
        if profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_II_DRIVER.value:
            result = self.json_save_model.save(filepath=self.config_model.setting_2_driver_filepath, data=self.config_model.default_setting_2_driver)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_II_PASSANGER.value:
            result = self.json_save_model.save(filepath=self.config_model.setting_2_passanger_filepath, data=self.config_model.default_setting_2_passanger)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_IV_DRIVER.value:
            result = self.json_save_model.save(filepath=self.config_model.setting_4_driver_filepath, data=self.config_model.default_setting_4_driver)
        elif profile == self.config_model.ProfileSelectionComboboxIndexs.CLASS_IV_PASSANGER.value:
            result = self.json_save_model.save(filepath=self.config_model.setting_4_passanger_filepath, data=self.config_model.default_setting_4_passanger)
        else:
            LOGGER.error('Error when write data into json! - Profile not found.')
            return self.ReturnCode.FILE_NOT_FOUND
        
        if result == self.json_save_model.ReturnCode.DATA_TYPE_INVALID:
            LOGGER.error('Error when write data into json! - Data type error')
            return self.ReturnCode.DATA_TYPE_ERROR
        elif result == self.json_save_model.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when write data into json! - File not found.')
            return self.ReturnCode.FILE_NOT_FOUND
        
        return self.ReturnCode.SUCCESS
        
        
