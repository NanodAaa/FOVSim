# setting_window.py
import tkinter as tk
from assets.styles.tkinter_style import TkinterStyle
from ..controller.setting_window_controller import SettingWindowController
from gui.selection_window import SelectionWindow
from enum import Enum
from ..models.config_model import ConfigModel
from ..models.config_model import LOGGER

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
    
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.swc = SettingWindowController()
        self.config_model = ConfigModel()
        self._init_gui()
        self.grab_set()
        self.wait_window()
        
    def _init_setting_data(self):
        self.swc.init_setting_data()
    def _init_gui(self):
        # Menu
        self.menu = tk.Menu(self)
        self.menu.add_command(label='Save', command=self._onclick_menu_save)
        
        self.config(menu=self.menu)
        
        # Camera coordinates relative to E.P.
        self.camera_position_label = tk.Label(self, text='Camera position', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.camera_position_label.grid(row=self.camera_position_widgets_position_dict['label']['row'], column=self.camera_position_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.camera_position_x_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_position_x_entry.grid(row=self.camera_position_widgets_position_dict['x entry']['row'], column=self.camera_position_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.camera_position_y_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_position_y_entry.grid(row=self.camera_position_widgets_position_dict['y entry']['row'], column=self.camera_position_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.camera_position_z_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_position_z_entry.grid(row=self.camera_position_widgets_position_dict['z entry']['row'], column=self.camera_position_widgets_position_dict['z entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])

        # Distance between camera & car body.
        self.distance_cam_carbody_label = tk.Label(self, text='Cam-CarBody', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.distance_cam_carbody_label.grid(row=self.distance_cam_carbody_position_dict['label']['row'], column=self.distance_cam_carbody_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.distance_cam_carbody_y_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.distance_cam_carbody_y_entry.grid(row=self.distance_cam_carbody_position_dict['y entry']['row'], column=self.distance_cam_carbody_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])

        # Distance between camera & ground.
        self.distance_cam_ground_label = tk.Label(self, text='Cam-CarBody', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.distance_cam_ground_label.grid(row=self.distance_cam_ground_position_dict['label']['row'], column=self.distance_cam_ground_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.distance_cam_ground_z_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.distance_cam_ground_z_entry.grid(row=self.distance_cam_ground_position_dict['y entry']['row'], column=self.distance_cam_ground_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])

        # Camera Pose
        self.camera_pose_label = tk.Label(self, text='Pose(PYR): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.camera_pose_label.grid(row=self.camera_pose_widgets_position_dict['label']['row'], column=self.camera_pose_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.camera_pose_pitch_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_pose_pitch_entry.grid(row=self.camera_pose_widgets_position_dict['pitch entry']['row'], column=self.camera_pose_widgets_position_dict['pitch entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        
        self.camera_pose_yaw_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_pose_yaw_entry.grid(row=self.camera_pose_widgets_position_dict['yaw entry']['row'], column=self.camera_pose_widgets_position_dict['yaw entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        
        self.camera_pose_roll_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_pose_roll_entry.grid(row=self.camera_pose_widgets_position_dict['roll entry']['row'], column=self.camera_pose_widgets_position_dict['roll entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        
        # Fitting Function Coefficients
        self.fitting_func_coefs_label = tk.Label(self, text='FitCoe(X5>0): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.fitting_func_coefs_label.grid(row=self.fitting_func_coefs_widgets_position_dict['label']['row'], column=self.fitting_func_coefs_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.fitting_func_coefs_x5_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x5_entry.grid(row=self.fitting_func_coefs_widgets_position_dict['x5 entry']['row'], column=self.fitting_func_coefs_widgets_position_dict['x5 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        
        self.fitting_func_coefs_x4_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x4_entry.grid(row=self.fitting_func_coefs_widgets_position_dict['x4 entry']['row'], column=self.fitting_func_coefs_widgets_position_dict['x4 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        
        self.fitting_func_coefs_x3_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x3_entry.grid(row=self.fitting_func_coefs_widgets_position_dict['x3 entry']['row'], column=self.fitting_func_coefs_widgets_position_dict['x3 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.fitting_func_coefs_x2_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x2_entry.grid(row=self.fitting_func_coefs_widgets_position_dict['x2 entry']['row'], column=self.fitting_func_coefs_widgets_position_dict['x2 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.fitting_func_coefs_x1_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x1_entry.grid(row=self.fitting_func_coefs_widgets_position_dict['x1 entry']['row'], column=self.fitting_func_coefs_widgets_position_dict['x1 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.fitting_func_coefs_x0_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x0_entry.grid(row=self.fitting_func_coefs_widgets_position_dict['x0 entry']['row'], column=self.fitting_func_coefs_widgets_position_dict['x0 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        # Fitting Function Coefficients Reverse
        self.fitting_func_coefs_reverse_label = tk.Label(self, text='FitCoeR(X5>0): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.fitting_func_coefs_reverse_label.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['label']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.fitting_func_coefs_reverse_x5_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_reverse_x5_entry.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['x5 entry']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['x5 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.fitting_func_coefs_reverse_x4_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_reverse_x4_entry.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['x4 entry']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['x4 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.fitting_func_coefs_reverse_x3_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_reverse_x3_entry.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['x3 entry']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['x3 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.fitting_func_coefs_reverse_x2_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_reverse_x2_entry.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['x2 entry']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['x2 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.fitting_func_coefs_reverse_x1_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_reverse_x1_entry.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['x1 entry']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['x1 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.fitting_func_coefs_reverse_x0_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_reverse_x0_entry.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['x0 entry']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['x0 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        # Sensor Params
        self.sensor_params_label = tk.Label(self, text='SenPrms(WHP): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.sensor_params_label.grid(row=self.sensor_params_widgets_position_dict['label']['row'], column=self.sensor_params_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.sensor_params_width_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_params_width_entry.grid(row=self.sensor_params_widgets_position_dict['width entry']['row'], column=self.sensor_params_widgets_position_dict['width entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.sensor_params_height_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_params_height_entry.grid(row=self.sensor_params_widgets_position_dict['height entry']['row'], column=self.sensor_params_widgets_position_dict['height entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.sensor_params_pixel_size_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_params_pixel_size_entry.grid(row=self.sensor_params_widgets_position_dict['pixel size entry']['row'], column=self.sensor_params_widgets_position_dict['pixel size entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
            
        # Monitor Params
        self.monitor_params_label = tk.Label(self, text='MonPrms(WHP): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.monitor_params_label.grid(row=self.monitor_params_widgets_position_dict['label']['row'], column=self.monitor_params_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.monitor_params_width_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_params_width_entry.grid(row=self.monitor_params_widgets_position_dict['width entry']['row'], column=self.monitor_params_widgets_position_dict['width entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.monitor_params_height_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_params_height_entry.grid(row=self.monitor_params_widgets_position_dict['height entry']['row'], column=self.monitor_params_widgets_position_dict['height entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        
        self.monitor_params_pixel_size_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_params_pixel_size_entry.grid(row=self.monitor_params_widgets_position_dict['pixel size entry']['row'], column=self.monitor_params_widgets_position_dict['pixel size entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])

        self._refresh_entrys()
        
    def _onclick_menu_save(self):
        # Get data from entries.
        data = {}
        data[self.config_model.Keys.CAMERA_POSITION.value] = float(self.camera_position_x_entry.get().replace('E', 'e')), float(self.camera_position_y_entry.get().replace('E', 'e')), float(self.camera_position_z_entry.get().replace('E', 'e'))
        data[self.config_model.Keys.DISTANCE_CAM_CARBODY.value] = float(self.distance_cam_carbody_y_entry.get().replace('E', 'e'))
        data[self.config_model.Keys.DISTANCE_CAM_GROUND.value] = float(self.distance_cam_ground_z_entry.get().replace('E', 'e'))
        
        # Save data using controller.
        result = self.swc.save_data_to_json(data)
        if result == self.swc.ReturnCode.FILE_NOT_FOUND:
            error_window = SelectionWindow()
            error_window.set_label_text('File not found!')
            error_window.set_button_left_text('OK')
            error_window.set_button_right_text('Cancel')
        
        # Refresh entries.
        self._refresh_entrys()
        
        LOGGER.info(f'Data saved to the json. Data: {data}')
         
    def _refresh_entrys(self):
        """
        Refresh values in entrys.  
        """
        data = self.swc.read_data_from_json()
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