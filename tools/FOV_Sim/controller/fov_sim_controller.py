from ..models.storage_model import JsonStorageModel
from ..models.config_model import ConfigModel
from ..models.config_model import LOGGER
from enum import Enum, auto

class FovSimController:
    class ReturnCode(Enum):
        OK = 0
        FILE_NOT_FOUND = auto()

    def init_setting_data(self):
        data = JsonStorageModel().load(ConfigModel().setting_filepath)
        if data == JsonStorageModel.ReturnCode.FILE_NOT_FOUND:
            if JsonStorageModel().create_empty_json_file(ConfigModel().setting_filepath, ConfigModel().default_setting) == JsonStorageModel().ReturnCode.FILE_NOT_FOUND:
                return self.ReturnCode.FILE_NOT_FOUND
            
        elif data == {}:
            if JsonStorageModel().create_empty_json_file(ConfigModel().setting_filepath, ConfigModel().default_setting) == JsonStorageModel().ReturnCode.FILE_NOT_FOUND:
                return self.ReturnCode.FILE_NOT_FOUND