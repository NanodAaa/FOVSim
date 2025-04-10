# setting_window.py
# When adding new entry, please modify save_data, refresh_entrys, init_gui, and keys in config_model.py.

import tkinter as tk
from assets.styles.tkinter_style import TkinterStyle
from controller.setting_window_controller import SettingWindowController
from gui.selection_window import SelectionWindow
from models.config_model import ConfigModel
from models.config_model import LOGGER
from gui.help_window import HelpWindow
from tkinter import ttk

class SettingWindow(tk.Toplevel):    
    label_format_dict = TkinterStyle.label_format_dict
    entry_format_dict = TkinterStyle.entry_format_dict
    button_format_dict = TkinterStyle.button_format_dict
    
    camera_position_widgets_position_dict = {
        'label' : { 'row' : 0, 'column' : 0 }, 'x entry' : { 'row' : 0, 'column' : 1 }, 'y entry' : { 'row' : 0, 'column' : 2 }, 'z entry' : { 'row' : 0, 'column' : 3 },
    }
    distance_cam_carbody_position_dict = {
        'label' : { 'row' : 1, 'column' : 0 }, 'y entry' : { 'row' : 1, 'column' : 1 },
    }
    distance_cam_ground_position_dict = {
        'label' : { 'row' : 2, 'column' : 0 }, 'y entry' : { 'row' : 2, 'column' : 1 },
    }
    camera_pose_widgets_position_dict = {
        'label' : {'row' : 3, 'column' : 0}, 'pitch entry' : {'row' : 3, 'column' : 1}, 
        'yaw entry' : {'row' : 3, 'column' : 2}, 'roll entry' : {'row' : 3, 'column' : 3}
    }
    fitting_func_coefs_widgets_position_dict = {
        'label' : {'row' : 4, 'column' : 0}, 'x5 entry' : {'row' : 4, 'column' : 1}, 'x4 entry' : {'row' : 4, 'column' : 2}, 
        'x3 entry' : {'row' : 4, 'column' : 3}, 'x2 entry' : {'row' : 4, 'column' : 4}, 'x1 entry' : {'row' : 4, 'column' : 5}, 
        'x0 entry' : {'row' : 4, 'column' : 6}
    }
    fitting_func_coefs_reverse_widgets_position_dict = {
        'label' : {'row' : 5, 'column' : 0}, 'x5 entry' : {'row' : 5, 'column' : 1}, 'x4 entry' : {'row' : 5, 'column' : 2}, 
        'x3 entry' : {'row' : 5, 'column' : 3}, 'x2 entry' : {'row' : 5, 'column' : 4}, 'x1 entry' : {'row' : 5, 'column' : 5}, 
        'x0 entry' : {'row' : 5, 'column' : 6}
    }
    sensor_params_widgets_position_dict = {
        'label' : {'row' : 6, 'column' : 0}, 'width entry' : {'row' : 6, 'column' : 1}, 
        'height entry' : {'row' : 6, 'column' : 2}, 'pixel size entry' : {'row' : 6, 'column' : 3}
    }
    monitor_params_widgets_position_dict = {
        'label' : {'row' : 7, 'column' : 0}, 'width entry' : {'row' : 7, 'column' : 1}, 
        'height entry' : {'row' : 7, 'column' : 2}, 'pixel size entry' : {'row' : 7, 'column' : 3}
    }
    crop_region_widgets_position_dict = {
        'label' : {'row' : 8, 'column' : 0}, 'x entry' : {'row' : 8, 'column' : 1}, 
        'y entry' : {'row' : 8, 'column' : 2}, 'width entry' : {'row' : 8, 'column' : 3}, 
        'height entry' : {'row' : 8, 'column' : 4}
    }
    profile_selection_widgets_position_dict = {
        'label' : {'row' : 9, 'column' : 0}, 'combobox' : {'row' : 9, 'column' : 1}
    }
    
    def __init__(self, root, profile_list: list, profile_var: tk.StringVar):
        super().__init__(root)
        self.root = root
        self.swc = SettingWindowController()
        self.config_model = ConfigModel()

        if not isinstance(profile_list, list):
            raise TypeError('profile_list should be a list')
        if not isinstance(profile_var, tk.StringVar):
            raise TypeError('profile_var should be a StringVar')

        self.profile_list = profile_list
        self.profile_var = profile_var

        self._init_gui()
        #self._set_modal()
        #self.protocol('WM_DELETE_WINDOW', self._onclick_close)
        
    def _init_setting_data(self):
        self.swc.init_setting_data()
        
    def _init_gui(self):
        self.title('Settings')
        
        # Menu
        self.menu = tk.Menu(self)
        self.menu.add_command(label='Save', command=self._onclick_menu_save)    
        self.menu.add_command(label='Reset', command=self._onclick_menu_reset)
        self.menu.add_command(label='Help', command=self._onclick_menu_help)
    
        self.config(menu=self.menu)
        
        # Camera coordinates relative to E.P.
        self.camera_position_label = self._create_description_label('Cam Position: ')
        self._grid_description_label(self.camera_position_label, **self.camera_position_widgets_position_dict['label'])
        
        self.camera_position_x_entry = self._create_entry()
        self._grid_entry(self.camera_position_x_entry, **self.camera_position_widgets_position_dict['x entry'])
        
        self.camera_position_y_entry = self._create_entry()
        self._grid_entry(self.camera_position_y_entry, **self.camera_position_widgets_position_dict['y entry'])
        
        self.camera_position_z_entry = self._create_entry()
        self._grid_entry(self.camera_position_z_entry, **self.camera_position_widgets_position_dict['z entry'])

        # Distance between camera & car body.
        self.distance_cam_carbody_label = self._create_description_label('Cam-Carbody: ')
        self._grid_description_label(self.distance_cam_carbody_label, **self.distance_cam_carbody_position_dict['label'])
        
        self.distance_cam_carbody_y_entry = self._create_entry()
        self._grid_entry(self.distance_cam_carbody_y_entry, **self.distance_cam_carbody_position_dict['y entry'])

        # Distance between camera & ground.
        self.distance_cam_ground_label = self._create_description_label('Cam-Ground: ')
        self._grid_description_label(self.distance_cam_ground_label, **self.distance_cam_ground_position_dict['label'])
        
        self.distance_cam_ground_z_entry = self._create_entry()
        self._grid_entry(self.distance_cam_ground_z_entry, **self.distance_cam_ground_position_dict['y entry'])

        # Camera Pose
        self.camera_pose_label = self._create_description_label('Camera Pose: ')
        self._grid_description_label(self.camera_pose_label, **self.camera_pose_widgets_position_dict['label'])
        
        self.camera_pose_pitch_entry = self._create_entry()
        self._grid_entry(self.camera_pose_pitch_entry, **self.camera_pose_widgets_position_dict['pitch entry'])
               
        self.camera_pose_yaw_entry = self._create_entry()
        self._grid_entry(self.camera_pose_yaw_entry, **self.camera_pose_widgets_position_dict['yaw entry'])
        
        self.camera_pose_roll_entry = self._create_entry()
        self._grid_entry(self.camera_pose_roll_entry, **self.camera_pose_widgets_position_dict['roll entry'])
        
        # Fitting Function Coefficients
        self.fitting_func_coefs_label = self._create_description_label('FitCoe: ')
        self._grid_description_label(self.fitting_func_coefs_label, **self.fitting_func_coefs_widgets_position_dict['label'])
        
        self.fitting_func_coefs_x5_entry = self._create_entry()
        self._grid_entry(self.fitting_func_coefs_x5_entry, **self.fitting_func_coefs_widgets_position_dict['x5 entry'])
        
        self.fitting_func_coefs_x4_entry = self._create_entry()
        self._grid_entry(self.fitting_func_coefs_x4_entry, **self.fitting_func_coefs_widgets_position_dict['x4 entry'])
        
        self.fitting_func_coefs_x3_entry = self._create_entry()
        self._grid_entry(self.fitting_func_coefs_x3_entry, **self.fitting_func_coefs_widgets_position_dict['x3 entry'])
        
        self.fitting_func_coefs_x2_entry = self._create_entry()
        self._grid_entry(self.fitting_func_coefs_x2_entry, **self.fitting_func_coefs_widgets_position_dict['x2 entry'])
        
        self.fitting_func_coefs_x1_entry = self._create_entry()
        self._grid_entry(self.fitting_func_coefs_x1_entry, **self.fitting_func_coefs_widgets_position_dict['x1 entry'])
        
        self.fitting_func_coefs_x0_entry = self._create_entry()
        self._grid_entry(self.fitting_func_coefs_x0_entry, **self.fitting_func_coefs_widgets_position_dict['x0 entry'])
        
        # Fitting Function Coefficients Reverse
        self.fitting_func_coefs_reverse_label = self._create_description_label('FitCoeR: ')
        self._grid_description_label(self.fitting_func_coefs_reverse_label, **self.fitting_func_coefs_reverse_widgets_position_dict['label'])
        
        self.fitting_func_coefs_reverse_x5_entry = self._create_entry()
        self._grid_entry(self.fitting_func_coefs_reverse_x5_entry, **self.fitting_func_coefs_reverse_widgets_position_dict['x5 entry'])
        
        self.fitting_func_coefs_reverse_x4_entry = self._create_entry()
        self._grid_entry(self.fitting_func_coefs_reverse_x4_entry, **self.fitting_func_coefs_reverse_widgets_position_dict['x4 entry'])
        
        self.fitting_func_coefs_reverse_x3_entry = self._create_entry()
        self._grid_entry(self.fitting_func_coefs_reverse_x3_entry, **self.fitting_func_coefs_reverse_widgets_position_dict['x3 entry'])
        
        self.fitting_func_coefs_reverse_x2_entry = self._create_entry()
        self._grid_entry(self.fitting_func_coefs_reverse_x2_entry, **self.fitting_func_coefs_reverse_widgets_position_dict['x2 entry'])
        
        self.fitting_func_coefs_reverse_x1_entry = self._create_entry()
        self._grid_entry(self.fitting_func_coefs_reverse_x1_entry, **self.fitting_func_coefs_reverse_widgets_position_dict['x1 entry'])
        
        self.fitting_func_coefs_reverse_x0_entry = self._create_entry()
        self._grid_entry(self.fitting_func_coefs_reverse_x0_entry, **self.fitting_func_coefs_reverse_widgets_position_dict['x0 entry'])
        
        # Sensor Params
        self.sensor_params_label = self._create_description_label('SensorPrms: ')
        self._grid_description_label(self.sensor_params_label, **self.sensor_params_widgets_position_dict['label'])
        
        self.sensor_params_width_entry = self._create_entry()
        self._grid_entry(self.sensor_params_width_entry, **self.sensor_params_widgets_position_dict['width entry'])
        
        self.sensor_params_height_entry = self._create_entry()
        self._grid_entry(self.sensor_params_height_entry, **self.sensor_params_widgets_position_dict['height entry'])
        
        self.sensor_params_pixel_size_entry = self._create_entry()
        self._grid_entry(self.sensor_params_pixel_size_entry, **self.sensor_params_widgets_position_dict['pixel size entry'])
            
        # Monitor Params
        self.monitor_params_label = self._create_description_label('MonitorPrms: ')
        self._grid_description_label(self.monitor_params_label, **self.monitor_params_widgets_position_dict['label'])
        
        self.monitor_params_width_entry = self._create_entry()
        self._grid_entry(self.monitor_params_width_entry, **self.monitor_params_widgets_position_dict['width entry'])
        
        self.monitor_params_height_entry = self._create_entry()
        self._grid_entry(self.monitor_params_height_entry, **self.monitor_params_widgets_position_dict['height entry'])
        
        self.monitor_params_pixel_size_entry = self._create_entry()
        self._grid_entry(self.monitor_params_pixel_size_entry, **self.monitor_params_widgets_position_dict['pixel size entry'])

        # Crop Region
        self.crop_region_label = self._create_description_label('Crop Region: ')
        self._grid_description_label(self.crop_region_label, **self.crop_region_widgets_position_dict['label'])
        
        self.crop_region_x_entry = self._create_entry()
        self._grid_entry(self.crop_region_x_entry, **self.crop_region_widgets_position_dict['x entry']) 
        
        self.crop_region_y_entry = self._create_entry()
        self._grid_entry(self.crop_region_y_entry, **self.crop_region_widgets_position_dict['y entry'])
        
        self.crop_region_width_entry = self._create_entry()
        self._grid_entry(self.crop_region_width_entry, **self.crop_region_widgets_position_dict['width entry'])
        
        self.crop_region_height_entry = self._create_entry()
        self._grid_entry(self.crop_region_height_entry, **self.crop_region_widgets_position_dict['height entry'])

        # Profile Selection
        self.profile_selection_label = self._create_description_label('Profile: ')
        self._grid_description_label(self.profile_selection_label, **self.profile_selection_widgets_position_dict['label'])
        
        self.profile_selection_combobox = ttk.Combobox(self, textvariable=self.profile_var, values=self.profile_list, **self.config_model.profile_selection_combobox_format_dict)
        self.profile_selection_combobox.bind('<<ComboboxSelected>>', self._onclick_profile_selection_combobox)
        self.profile_selection_combobox.grid(**self.profile_selection_widgets_position_dict['combobox'])

        self._refresh_entrys()
        
    def _onclick_menu_save(self):
        # Get data from entries.
        data = {}
        data[self.config_model.Keys.CAMERA_POSITION.value] = [float(self.camera_position_x_entry.get().replace('E', 'e')), float(self.camera_position_y_entry.get().replace('E', 'e')), float(self.camera_position_z_entry.get().replace('E', 'e'))]
        data[self.config_model.Keys.DISTANCE_CAM_CARBODY.value] = float(self.distance_cam_carbody_y_entry.get().replace('E', 'e'))
        data[self.config_model.Keys.DISTANCE_CAM_GROUND.value] = float(self.distance_cam_ground_z_entry.get().replace('E', 'e'))
        data[self.config_model.Keys.CAMERA_POSE.value] = [float(self.camera_pose_pitch_entry.get().replace('E', 'e')), float(self.camera_pose_yaw_entry.get().replace('E', 'e')), float(self.camera_pose_roll_entry.get().replace('E', 'e')) ]
        data[self.config_model.Keys.SENSOR_PARAMS.value] = [int(self.sensor_params_width_entry.get()), int(self.sensor_params_height_entry.get()), float(self.sensor_params_pixel_size_entry.get().replace('E', 'e'))]
        data[self.config_model.Keys.MONITOR_PARAMS.value] = [int(self.monitor_params_width_entry.get()), int(self.monitor_params_height_entry.get()), float(self.monitor_params_pixel_size_entry.get().replace('E', 'e'))]
        data[self.config_model.Keys.FITTING_FUNC_COEFS.value] = [float(self.fitting_func_coefs_x5_entry.get().replace('E', 'e')), float(self.fitting_func_coefs_x4_entry.get().replace('E', 'e')), float(self.fitting_func_coefs_x3_entry.get().replace('E', 'e')), float(self.fitting_func_coefs_x2_entry.get().replace('E', 'e')), float(self.fitting_func_coefs_x1_entry.get().replace('E', 'e')), float(self.fitting_func_coefs_x0_entry.get().replace('E', 'e'))] 
        data[self.config_model.Keys.FITTING_FUNC_COEFS_REVERSE.value] = [float(self.fitting_func_coefs_reverse_x5_entry.get().replace('E', 'e')), float(self.fitting_func_coefs_reverse_x4_entry.get().replace('E', 'e')),float(self.fitting_func_coefs_reverse_x3_entry.get().replace('E', 'e')), float(self.fitting_func_coefs_reverse_x2_entry.get().replace('E', 'e')),float(self.fitting_func_coefs_reverse_x1_entry.get().replace('E', 'e')), float(self.fitting_func_coefs_reverse_x0_entry.get().replace('E', 'e'))]
        data[self.config_model.Keys.CROP_REGION.value] = [int(self.crop_region_x_entry.get()), int(self.crop_region_y_entry.get()), int(self.crop_region_width_entry.get()), int(self.crop_region_height_entry.get())]
        
        # Save data using controller.
        result = self.swc.save_data_to_json(data, self.profile_var.get())
        if result == self.swc.ReturnCode.FILE_NOT_FOUND:
            error_window = SelectionWindow()
            error_window.set_label_text('File not found!')
            error_window.set_button_left_text('OK')
            error_window.set_button_right_text('Cancel')
        
        # Refresh entries.
        self._refresh_entrys()
        
        LOGGER.info(f'Data saved to the json. Data: {data}')
         
    def _onclick_menu_reset(self):
        LOGGER.info('User clicked menu-reset')
        selection_window = SelectionWindow(self)
        label_text = 'Are you sure to reset data?'
        selection_window.set_label_text(label_text)
        selection_window.set_button_left_text('OK')
        selection_window.set_button_right_text('Cancel')
        selection_window.set_modal()
        
        button_status = selection_window.get_button_status()
        if button_status == selection_window.ButtonStatus.LEFT:
            LOGGER.info('User confirmed to reset setting.')
            self.swc.reset_default_setting(self.profile_var.get())
            self._refresh_entrys()
            
        elif button_status == selection_window.ButtonStatus.RIGHT:
            LOGGER.info('User canceled reset')
            return
         
    def _refresh_entrys(self):
        """
        Refresh values in entrys.  
        """
        data = self.swc.read_data_from_json(self.profile_var.get())
        if data == self.swc.ReturnCode.FILE_NOT_FOUND:
            LOGGER.error('Error when load data from json! - File not Found.')
            error_window = SelectionWindow(self)
            error_window.set_label_text('File not found!')
            error_window.set_button_left_text('OK')
            error_window.set_button_right_text('Cancel')
            error_window.set_modal()
            return
        
        
        keys = data.keys()
        key = self.config_model.Keys.CAMERA_POSITION.value
        # If the key which represent the entry is exist in the json file, then refresh this bunch of entrys.
        # Otherwise skip the refresh project so that it won't get error.
        if key in keys:
            self.camera_position_x_entry.delete(0, tk.END)
            self.camera_position_y_entry.delete(0, tk.END)
            self.camera_position_z_entry.delete(0, tk.END)
            self.camera_position_x_entry.insert(0, data[key][0])
            self.camera_position_y_entry.insert(0, data[key][1])
            self.camera_position_z_entry.insert(0, data[key][2])
        else:
            LOGGER.warning(f'The key "{key}" is missing in the json file, the refresh process of these entrys is skipped.')
        
        key = self.config_model.Keys.DISTANCE_CAM_CARBODY.value
        if key in keys:
            self.distance_cam_carbody_y_entry.delete(0, tk.END)
            self.distance_cam_carbody_y_entry.insert(0, data[key])
        else:
            LOGGER.warning(f'The key "{key}" is missing in the json file, the refresh process of these entrys is skipped.')
            
        key = self.config_model.Keys.DISTANCE_CAM_GROUND.value
        if key in keys:
            self.distance_cam_ground_z_entry.delete(0, tk.END)
            self.distance_cam_ground_z_entry.insert(0, data[key])
        else:
            LOGGER.warning(f'The key "{key}" is missing in the json file, the refresh process of these entrys is skipped.')            
            
        key = self.config_model.Keys.CAMERA_POSE.value
        if key in keys:
            self.camera_pose_pitch_entry.delete(0, tk.END)
            self.camera_pose_yaw_entry.delete(0, tk.END)
            self.camera_pose_roll_entry.delete(0, tk.END)
            self.camera_pose_pitch_entry.insert(0, data[key][0])
            self.camera_pose_yaw_entry.insert(0, data[key][1])
            self.camera_pose_roll_entry.insert(0, data[key][2])
        else:
            LOGGER.warning(f'The key "{key}" is missing in the json file, the refresh process of these entrys is skipped.')
            
        key = self.config_model.Keys.SENSOR_PARAMS.value
        if key in keys:
            self.sensor_params_width_entry.delete(0, tk.END)
            self.sensor_params_height_entry.delete(0, tk.END)
            self.sensor_params_pixel_size_entry.delete(0, tk.END)
            self.sensor_params_width_entry.insert(0, data[key][0])
            self.sensor_params_height_entry.insert(0, data[key][1])
            self.sensor_params_pixel_size_entry.insert(0, data[key][2])
        else:
            LOGGER.warning(f'The key "{key}" is missing in the json file, the refresh process of these entrys is skipped.')
            
        key = self.config_model.Keys.MONITOR_PARAMS.value
        if key in keys:
            self.monitor_params_width_entry.delete(0, tk.END)
            self.monitor_params_height_entry.delete(0, tk.END)
            self.monitor_params_pixel_size_entry.delete(0, tk.END)
            self.monitor_params_width_entry.insert(0, data[key][0])
            self.monitor_params_height_entry.insert(0, data[key][1])
            self.monitor_params_pixel_size_entry.insert(0, data[key][2])
        else:
            LOGGER.warning(f'The key "{key}" is missing in the json file, the refresh process of these entrys is skipped.')
            
        key = self.config_model.Keys.FITTING_FUNC_COEFS.value
        if key in keys:
            self.fitting_func_coefs_x5_entry.delete(0, tk.END)
            self.fitting_func_coefs_x4_entry.delete(0, tk.END)
            self.fitting_func_coefs_x3_entry.delete(0, tk.END)
            self.fitting_func_coefs_x2_entry.delete(0, tk.END)
            self.fitting_func_coefs_x1_entry.delete(0, tk.END)
            self.fitting_func_coefs_x0_entry.delete(0, tk.END)
            self.fitting_func_coefs_x5_entry.insert(0, data[key][0])
            self.fitting_func_coefs_x4_entry.insert(0, data[key][1])
            self.fitting_func_coefs_x3_entry.insert(0, data[key][2])
            self.fitting_func_coefs_x2_entry.insert(0, data[key][3])
            self.fitting_func_coefs_x1_entry.insert(0, data[key][4])
            self.fitting_func_coefs_x0_entry.insert(0, data[key][5])
        else:
            LOGGER.warning(f'The key "{key}" is missing in the json file, the refresh process of these entrys is skipped.')
            
        key = self.config_model.Keys.FITTING_FUNC_COEFS_REVERSE.value
        if key in keys:
            self.fitting_func_coefs_reverse_x5_entry.delete(0, tk.END)
            self.fitting_func_coefs_reverse_x4_entry.delete(0, tk.END)
            self.fitting_func_coefs_reverse_x3_entry.delete(0, tk.END)
            self.fitting_func_coefs_reverse_x2_entry.delete(0, tk.END)
            self.fitting_func_coefs_reverse_x1_entry.delete(0, tk.END)
            self.fitting_func_coefs_reverse_x0_entry.delete(0, tk.END)
            self.fitting_func_coefs_reverse_x5_entry.insert(0, data[key][0])
            self.fitting_func_coefs_reverse_x4_entry.insert(0, data[key][1])
            self.fitting_func_coefs_reverse_x3_entry.insert(0, data[key][2])
            self.fitting_func_coefs_reverse_x2_entry.insert(0, data[key][3])
            self.fitting_func_coefs_reverse_x1_entry.insert(0, data[key][4])
            self.fitting_func_coefs_reverse_x0_entry.insert(0, data[key][5])
        else:
            LOGGER.warning(f'The key "{key}" is missing in the json file, the refresh process of these entrys is skipped.')
            
        key = self.config_model.Keys.CROP_REGION.value
        if key in keys:
            self.crop_region_x_entry.delete(0, tk.END)
            self.crop_region_y_entry.delete(0, tk.END)
            self.crop_region_width_entry.delete(0, tk.END)
            self.crop_region_height_entry.delete(0, tk.END)
            self.crop_region_x_entry.insert(0, data[key][0])
            self.crop_region_y_entry.insert(0, data[key][1])
            self.crop_region_width_entry.insert(0, data[key][2])
            self.crop_region_height_entry.insert(0, data[key][3])
        else:
            LOGGER.warning(f'The key "{key}" is missing in the json file, the refresh process of these entrys is skipped.')
            
    def _set_modal(self):
        """
        Set the window as modal.
        """
        self.grab_set()
        self.wait_window()
        
    def _onclick_menu_help(self):
        """
        Open help window.
        """
        LOGGER.info('User clicked menu-help')
        help_window = HelpWindow(self)
        help_window.set_modal()
        
    def _create_description_label(self, text: str, **kwargs) -> tk.Label:
        return tk.Label(self, text=text, font=self.label_format_dict['font'], width=self.label_format_dict['width'], anchor='e',**kwargs)
    
    def _grid_description_label(self, label: tk.Label, row: int, column: int, **kwargs) -> None:
        label.grid(row=row, column=column, padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'], **kwargs)
    
    def _create_entry(self, **kwargs) -> tk.Entry:
        return tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'], **kwargs)
    
    def _grid_entry(self, entry: tk.Entry, row: int, column: int, **kwargs) -> None:
        entry.grid(row=row, column=column, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'], **kwargs)
        
    def _onclick_profile_selection_combobox(self, event):
        """
        When the profile selection combobox is clicked, refresh the entrys.
        """
        LOGGER.info('User clicked profile selection combobox')
        self._refresh_entrys()