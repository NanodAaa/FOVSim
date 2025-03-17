# options_window.py

import tkinter as tk
from cores import JsonStorage as js
import sys

class ParamsWindow(tk.Toplevel):
    label_format_dict = { 'font' : ('consolas', 11), 'padx' : 5, 'pady' : 5, 'sticky' : 'w', 'width' : 14 }
    entry_format_dict = { 'font' : ('consolas', 12), 'padx' : 5, 'pady' : 5, 'sticky' : 'ew', 'width' : 13 }
    button_format_dict = { 'bg' : 'lightblue', 'padx' : 5, 'pady' : 5, 'sticky' : 'ewsn', 'width' : 13 }

    monitor_point_a_widgets_position_dict = {
        'label' : {'row' : 0, 'column' : 0}, 'x entry' : {'row' : 0, 'column' : 1}, 
        'y entry' : {'row' : 0, 'column' : 2}, 'z entry' : {'row' : 0, 'column' : 3}
    }
    monitor_point_b_widgets_position_dict = {
        'label' : {'row' : 1, 'column' : 0}, 'x entry' : {'row' : 1, 'column' : 1}, 
        'y entry' : {'row' : 1, 'column' : 2}, 'z entry' : {'row' : 1, 'column' : 3}
    }
    camera_pose_widgets_position_dict = {
        'label' : {'row' : 2, 'column' : 0}, 'pitch entry' : {'row' : 2, 'column' : 1}, 
        'yaw entry' : {'row' : 2, 'column' : 2}, 'roll entry' : {'row' : 2, 'column' : 3}
    }
    fitting_func_coefs_widgets_position_dict = {
        'label' : {'row' : 3, 'column' : 0}, 'x5 entry' : {'row' : 3, 'column' : 1}, 'x4 entry' : {'row' : 3, 'column' : 2}, 
        'x3 entry' : {'row' : 3, 'column' : 3}, 'x2 entry' : {'row' : 3, 'column' : 4}, 'x1 entry' : {'row' : 3, 'column' : 5}, 
        'x0 entry' : {'row' : 3, 'column' : 6}
    }
    fitting_func_coefs_reverse_widgets_position_dict = {
        'label' : {'row' : 4, 'column' : 0}, 'x5 entry' : {'row' : 4, 'column' : 1}, 'x4 entry' : {'row' : 4, 'column' : 2}, 
        'x3 entry' : {'row' : 4, 'column' : 3}, 'x2 entry' : {'row' : 4, 'column' : 4}, 'x1 entry' : {'row' : 4, 'column' : 5}, 
        'x0 entry' : {'row' : 4, 'column' : 6}
    }
    sensor_params_widgets_position_dict = {
        'label' : {'row' : 5, 'column' : 0}, 'width entry' : {'row' : 5, 'column' : 1}, 
        'height entry' : {'row' : 5, 'column' : 2}, 'pixel size entry' : {'row' : 5, 'column' : 3}
    }
    monitor_params_widgets_position_dict = {
        'label' : {'row' : 6, 'column' : 0}, 'width entry' : {'row' : 6, 'column' : 1}, 
        'height entry' : {'row' : 6, 'column' : 2}, 'pixel size entry' : {'row' : 6, 'column' : 3}
    }
    button_widgets_position_dict = {
        'save' : {'row' : 7, 'column' : 0},
    }
    label_widgets_position_dict = {
        'message' : {'row' : 8, 'column' : 2}
    }
    
    """ world_coordinates_widgets_postion_dict = {
        'label' : {'row' : 0, 'column' : 0}, 'x entry' : {'row' : 0, 'column' : 1}, 'y entry' : {'row' : 0, 'column' : 2}, 'z entry' : {'row' : 0, 'column' : 3}
    } """
    """ camera_coordinates_widgets_position_dict = {
        'label' : {'row' : 5, 'column' : 0}, 'x entry' : {'row' : 5, 'column' : 1}, 'y entry' : {'row' : 5, 'column' : 2}, 'z entry' : {'row' : 5, 'column' : 3}} """
    """ pixel_coordinates_widgets_position_dict = {
        'label' : {'row' : 6, 'column' : 0}, 'x entry' : {'row' : 6, 'column' : 1}, 'y entry' : {'row' : 6, 'column' : 2}} """
    
    data = {
        'monitor point a' : { 'x' : '', 'y' : '', 'z' : '' },
        'monitor point b' : { 'x' : '', 'y' : '', 'z' : '' },
        'fitting func coefs' : { 'x5' : '', 'x4' : '', 'x3' : '', 'x2' : '', 'x1' : '', 'x0' : '' },
        'fitting func coefs reverse' : { 'x5' : '', 'x4' : '', 'x3' : '', 'x2' : '', 'x1' : '', 'x0' : '' },
        'camera pose' : { 'pitch' : '', 'yaw' : '', 'roll' : '' },
        'sensor params' : { 'width' : '', 'height' : '', 'pixel size' : '' },
        'monitor params' : { 'width' : '', 'height' : '', 'pixel size' : '' },
    }
    
    config_filename = 'config.json'
    config_filepath = f'./{config_filename}'
    
    def __init__(self, root):
        super().__init__(root)
        self._init_config_data()
        self._init_gui()
        
    def _init_gui(self):
    
        self.title("Parmas")
        
        """ # World Coordinates
        self.world_coordinate_label = tk.Label(self, text='P_w(XYZ): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.world_coordinate_label.grid(row=self.world_coordinates_widgets_postion_dict['label']['row'], column=self.world_coordinates_widgets_postion_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])

        self.world_coordinate_x_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_coordinate_x_entry.grid(row=self.world_coordinates_widgets_postion_dict['x entry']['row'], column=self.world_coordinates_widgets_postion_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_coordinate_x_entry.insert(0, self.data['world coordinates']['x'])
        
        self.world_coordinate_y_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_coordinate_y_entry.grid(row=self.world_coordinates_widgets_postion_dict['y entry']['row'], column=self.world_coordinates_widgets_postion_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_coordinate_y_entry.insert(0, self.data['world coordinates']['y'])
        
        self.world_coordinate_z_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_coordinate_z_entry.grid(row=self.world_coordinates_widgets_postion_dict['z entry']['row'], column=self.world_coordinates_widgets_postion_dict['z entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_coordinate_z_entry.insert(0, self.data['world coordinates']['z']) """
            
        # Monitor Point A Coordinates
        self.monitor_point_a_label = tk.Label(self, text='MP_A(XYZ): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.monitor_point_a_label.grid(row=self.monitor_point_a_widgets_position_dict['label']['row'], column=self.monitor_point_a_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.monitor_point_a_x_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_point_a_x_entry.grid(row=self.monitor_point_a_widgets_position_dict['x entry']['row'], column=self.monitor_point_a_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_point_a_x_entry.insert(0, self.data['monitor point a']['x'])
        
        self.monitor_point_a_y_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_point_a_y_entry.grid(row=self.monitor_point_a_widgets_position_dict['y entry']['row'], column=self.monitor_point_a_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_point_a_y_entry.insert(0, self.data['monitor point a']['y'])
        
        self.monitor_point_a_z_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_point_a_z_entry.grid(row=self.monitor_point_a_widgets_position_dict['z entry']['row'], column=self.monitor_point_a_widgets_position_dict['z entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_point_a_z_entry.insert(0, self.data['monitor point a']['z'])
        
        # Monitor Point B Coordinates
        self.monitor_point_b_label = tk.Label(self, text='MP_B(XYZ): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.monitor_point_b_label.grid(row=self.monitor_point_b_widgets_position_dict['label']['row'], column=self.monitor_point_b_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.monitor_point_b_x_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_point_b_x_entry.grid(row=self.monitor_point_b_widgets_position_dict['x entry']['row'], column=self.monitor_point_b_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_point_b_x_entry.insert(0, self.data['monitor point b']['x'])
        
        self.monitor_point_b_y_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_point_b_y_entry.grid(row=self.monitor_point_b_widgets_position_dict['y entry']['row'], column=self.monitor_point_b_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_point_b_y_entry.insert(0, self.data['monitor point b']['y'])
        
        self.monitor_point_b_z_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_point_b_z_entry.grid(row=self.monitor_point_b_widgets_position_dict['z entry']['row'], column=self.monitor_point_b_widgets_position_dict['z entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_point_b_z_entry.insert(0, self.data['monitor point b']['z'])
        
        # Camera Pose
        self.camera_pose_label = tk.Label(self, text='Pose(PYR): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.camera_pose_label.grid(row=self.camera_pose_widgets_position_dict['label']['row'], column=self.camera_pose_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.camera_pose_pitch_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_pose_pitch_entry.grid(row=self.camera_pose_widgets_position_dict['pitch entry']['row'], column=self.camera_pose_widgets_position_dict['pitch entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.camera_pose_pitch_entry.insert(0, self.data['camera pose']['pitch'])
        
        self.camera_pose_yaw_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_pose_yaw_entry.grid(row=self.camera_pose_widgets_position_dict['yaw entry']['row'], column=self.camera_pose_widgets_position_dict['yaw entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.camera_pose_yaw_entry.insert(0, self.data['camera pose']['yaw'])
        
        self.camera_pose_roll_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_pose_roll_entry.grid(row=self.camera_pose_widgets_position_dict['roll entry']['row'], column=self.camera_pose_widgets_position_dict['roll entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.camera_pose_roll_entry.insert(0, self.data['camera pose']['roll'])
        
        # Fitting Function Coefficients
        self.fitting_func_coefs_label = tk.Label(self, text='FitCoe(X5>0): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.fitting_func_coefs_label.grid(row=self.fitting_func_coefs_widgets_position_dict['label']['row'], column=self.fitting_func_coefs_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.fitting_func_coefs_x5_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x5_entry.grid(row=self.fitting_func_coefs_widgets_position_dict['x5 entry']['row'], column=self.fitting_func_coefs_widgets_position_dict['x5 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x5_entry.insert(0, self.data['fitting func coefs']['x5'])
        
        self.fitting_func_coefs_x4_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x4_entry.grid(row=self.fitting_func_coefs_widgets_position_dict['x4 entry']['row'], column=self.fitting_func_coefs_widgets_position_dict['x4 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x4_entry.insert(0, self.data['fitting func coefs']['x4'])
        
        self.fitting_func_coefs_x3_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x3_entry.grid(row=self.fitting_func_coefs_widgets_position_dict['x3 entry']['row'], column=self.fitting_func_coefs_widgets_position_dict['x3 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x3_entry.insert(0, self.data['fitting func coefs']['x3'])
        
        self.fitting_func_coefs_x2_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x2_entry.grid(row=self.fitting_func_coefs_widgets_position_dict['x2 entry']['row'], column=self.fitting_func_coefs_widgets_position_dict['x2 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x2_entry.insert(0, self.data['fitting func coefs']['x2'])
        
        self.fitting_func_coefs_x1_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x1_entry.grid(row=self.fitting_func_coefs_widgets_position_dict['x1 entry']['row'], column=self.fitting_func_coefs_widgets_position_dict['x1 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x1_entry.insert(0, self.data['fitting func coefs']['x1'])
        
        self.fitting_func_coefs_x0_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x0_entry.grid(row=self.fitting_func_coefs_widgets_position_dict['x0 entry']['row'], column=self.fitting_func_coefs_widgets_position_dict['x0 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x0_entry.insert(0, self.data['fitting func coefs']['x0'])
        
        # Fitting Function Coefficients Reverse
        self.fitting_func_coefs_reverse_label = tk.Label(self, text='FitCoeR(X5>0): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.fitting_func_coefs_reverse_label.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['label']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.fitting_func_coefs_reverse_x5_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_reverse_x5_entry.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['x5 entry']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['x5 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_reverse_x5_entry.insert(0, self.data['fitting func coefs reverse']['x5'])
        
        self.fitting_func_coefs_reverse_x4_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_reverse_x4_entry.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['x4 entry']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['x4 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_reverse_x4_entry.insert(0, self.data['fitting func coefs reverse']['x4'])
        
        self.fitting_func_coefs_reverse_x3_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_reverse_x3_entry.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['x3 entry']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['x3 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_reverse_x3_entry.insert(0, self.data['fitting func coefs reverse']['x3'])
        
        self.fitting_func_coefs_reverse_x2_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_reverse_x2_entry.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['x2 entry']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['x2 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_reverse_x2_entry.insert(0, self.data['fitting func coefs reverse']['x2'])
        
        self.fitting_func_coefs_reverse_x1_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_reverse_x1_entry.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['x1 entry']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['x1 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_reverse_x1_entry.insert(0, self.data['fitting func coefs reverse']['x1'])
        
        self.fitting_func_coefs_reverse_x0_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_reverse_x0_entry.grid(row=self.fitting_func_coefs_reverse_widgets_position_dict['x0 entry']['row'], column=self.fitting_func_coefs_reverse_widgets_position_dict['x0 entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_reverse_x0_entry.insert(0, self.data['fitting func coefs reverse']['x0'])
        
        # Sensor Params
        self.sensor_params_label = tk.Label(self, text='SenPrms(WHP): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.sensor_params_label.grid(row=self.sensor_params_widgets_position_dict['label']['row'], column=self.sensor_params_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.sensor_params_width_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_params_width_entry.grid(row=self.sensor_params_widgets_position_dict['width entry']['row'], column=self.sensor_params_widgets_position_dict['width entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_params_width_entry.insert(0, self.data['sensor params']['width'])
        
        self.sensor_params_height_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_params_height_entry.grid(row=self.sensor_params_widgets_position_dict['height entry']['row'], column=self.sensor_params_widgets_position_dict['height entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_params_height_entry.insert(0, self.data['sensor params']['height'])
        
        self.sensor_params_pixel_size_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_params_pixel_size_entry.grid(row=self.sensor_params_widgets_position_dict['pixel size entry']['row'], column=self.sensor_params_widgets_position_dict['pixel size entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_params_pixel_size_entry.insert(0, self.data['sensor params']['pixel size'])
            
        # Monitor Params
        self.monitor_params_label = tk.Label(self, text='MonPrms(WHP): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.monitor_params_label.grid(row=self.monitor_params_widgets_position_dict['label']['row'], column=self.monitor_params_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.monitor_params_width_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_params_width_entry.grid(row=self.monitor_params_widgets_position_dict['width entry']['row'], column=self.monitor_params_widgets_position_dict['width entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_params_width_entry.insert(0, self.data['monitor params']['width'])
        
        self.monitor_params_height_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_params_height_entry.grid(row=self.monitor_params_widgets_position_dict['height entry']['row'], column=self.monitor_params_widgets_position_dict['height entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_params_height_entry.insert(0, self.data['monitor params']['height'])
        
        self.monitor_params_pixel_size_entry = tk.Entry(self, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_params_pixel_size_entry.grid(row=self.monitor_params_widgets_position_dict['pixel size entry']['row'], column=self.monitor_params_widgets_position_dict['pixel size entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_params_pixel_size_entry.insert(0, self.data['monitor params']['pixel size'])
                
        # Save Button
        self.save_button = tk.Button(self, text='Save', bg=self.button_format_dict['bg'], width=self.button_format_dict['width'], command=self._onclick_button_save)
        self.save_button.grid(row=self.button_widgets_position_dict['save']['row'], column=self.button_widgets_position_dict['save']['column'], padx=self.button_format_dict['padx'], pady=self.button_format_dict['pady'], sticky=self.button_format_dict['sticky'])        
        
        return
    
    def _init_config_data(self):
        storage = js.JsonStorage(self.config_filepath)
        temp_data = storage.load()
        if temp_data != {}:
            self.data = temp_data
        else:
            storage.save(self.data)
            
    def _save_data_from_entry_to_memory(self):      
        """
        Save data to memory. 
        """   
        # World Coordinates
        self.data['world coordinates'] = { 
            'x' : float(self.world_coordinate_x_entry.get().replace('E', 'e')), 
            'y' : float(self.world_coordinate_y_entry.get().replace('E', 'e')), 
            'z' : float(self.world_coordinate_z_entry.get().replace('E', 'e')) 
        }
        
        # Fitting Functiong Coefficients
        self.data['fitting func coefs'] = { 
            'x5' : float(self.fitting_func_coefs_x5_entry.get().replace('E', 'e')), 
            'x4' : float(self.fitting_func_coefs_x4_entry.get().replace('E', 'e')),
            'x3' : float(self.fitting_func_coefs_x3_entry.get().replace('E', 'e')), 
            'x2' : float(self.fitting_func_coefs_x2_entry.get().replace('E', 'e')),
            'x1' : float(self.fitting_func_coefs_x1_entry.get().replace('E', 'e')), 
            'x0' : float(self.fitting_func_coefs_x0_entry.get().replace('E', 'e')),
        }
        
        # Fitting Functiong Coefficients Reverse
        self.data['fitting func coefs reverse'] = { 
            'x5' : float(self.fitting_func_coefs_reverse_x5_entry.get().replace('E', 'e')), 
            'x4' : float(self.fitting_func_coefs_reverse_x4_entry.get().replace('E', 'e')),
            'x3' : float(self.fitting_func_coefs_reverse_x3_entry.get().replace('E', 'e')), 
            'x2' : float(self.fitting_func_coefs_reverse_x2_entry.get().replace('E', 'e')),
            'x1' : float(self.fitting_func_coefs_reverse_x1_entry.get().replace('E', 'e')), 
            'x0' : float(self.fitting_func_coefs_reverse_x0_entry.get().replace('E', 'e')),
        }
        
        # Camera Pose
        self.data['camera pose'] = { 
            'pitch' : float(self.camera_pose_pitch_entry.get().replace('E', 'e')), 
            'yaw' : float(self.camera_pose_yaw_entry.get().replace('E', 'e')), 
            'roll' : float(self.camera_pose_roll_entry.get().replace('E', 'e')) 
        }
        
        # Sensor Params
        self.data['sensor params'] = { 
            'width' : int(self.sensor_params_width_entry.get()), 
            'height' : int(self.sensor_params_height_entry.get()), 
            'pixel size' : float(self.sensor_params_pixel_size_entry.get().replace('E', 'e')) 
        }       
           
        # Camera Coordinates
        self.data['camera coordinates'] = {
            'x' : float(self.camera_corrdinates_x_entry.get().replace('E', 'e')), 
            'y' : float(self.camera_corrdinates_y_entry.get().replace('E', 'e')), 
            'z' : float(self.camera_corrdinates_z_entry.get().replace('E', 'e'))
        }
           
        # Pixel Coordinates
        self.data['pixel coordinates'] = {
            'x' : float(self.pixel_coordinate_x_entry.get().replace('E', 'e')), 
            'y' : float(self.pixel_coordinate_y_entry.get().replace('E', 'e'))
        }
           
        return
    
    def _refresh_data_in_gui(self):
        """ 
        Write data from memory to entry.
        """
        # Pose
        self.camera_pose_pitch_entry.delete(0, tk.END)
        self.camera_pose_yaw_entry.delete(0, tk.END)
        self.camera_pose_roll_entry.delete(0, tk.END)
        
        self.camera_pose_pitch_entry.insert(0, self.data['camera pose']['pitch'])
        self.camera_pose_yaw_entry.insert(0, self.data['camera pose']['yaw'])
        self.camera_pose_roll_entry.insert(0, self.data['camera pose']['roll'])

        # Fitting funcion coefficients
        self.fitting_func_coefs_x5_entry.delete(0, tk.END)
        self.fitting_func_coefs_x4_entry.delete(0, tk.END)
        self.fitting_func_coefs_x3_entry.delete(0, tk.END)
        self.fitting_func_coefs_x2_entry.delete(0, tk.END)
        self.fitting_func_coefs_x1_entry.delete(0, tk.END)
        self.fitting_func_coefs_x0_entry.delete(0, tk.END)
        
        self.fitting_func_coefs_x5_entry.insert(0, self.data['fitting func coefs']['x5'])
        self.fitting_func_coefs_x4_entry.insert(0, self.data['fitting func coefs']['x4'])
        self.fitting_func_coefs_x3_entry.insert(0, self.data['fitting func coefs']['x3'])
        self.fitting_func_coefs_x2_entry.insert(0, self.data['fitting func coefs']['x2'])
        self.fitting_func_coefs_x1_entry.insert(0, self.data['fitting func coefs']['x1'])
        self.fitting_func_coefs_x0_entry.insert(0, self.data['fitting func coefs']['x0'])
        
        # Fitting funcion coefficients reverse
        self.fitting_func_coefs_reverse_x5_entry.delete(0, tk.END)
        self.fitting_func_coefs_reverse_x4_entry.delete(0, tk.END)
        self.fitting_func_coefs_reverse_x3_entry.delete(0, tk.END)
        self.fitting_func_coefs_reverse_x2_entry.delete(0, tk.END)
        self.fitting_func_coefs_reverse_x1_entry.delete(0, tk.END)
        self.fitting_func_coefs_reverse_x0_entry.delete(0, tk.END)
        
        self.fitting_func_coefs_reverse_x5_entry.insert(0, self.data['fitting func coefs reverse']['x5'])
        self.fitting_func_coefs_reverse_x4_entry.insert(0, self.data['fitting func coefs reverse']['x4'])
        self.fitting_func_coefs_reverse_x3_entry.insert(0, self.data['fitting func coefs reverse']['x3'])
        self.fitting_func_coefs_reverse_x2_entry.insert(0, self.data['fitting func coefs reverse']['x2'])
        self.fitting_func_coefs_reverse_x1_entry.insert(0, self.data['fitting func coefs reverse']['x1'])
        self.fitting_func_coefs_reverse_x0_entry.insert(0, self.data['fitting func coefs reverse']['x0'])
        
        # Sensor params
        self.sensor_params_width_entry.delete(0, tk.END)
        self.sensor_params_height_entry.delete(0, tk.END)
        self.sensor_params_pixel_size_entry.delete(0, tk.END)
        
        self.sensor_params_width_entry.insert(0, self.data['sensor params']['width'])
        self.sensor_params_height_entry.insert(0, self.data['sensor params']['height'])
        self.sensor_params_pixel_size_entry.insert(0, self.data['sensor params']['pixel size'])
        
        # World coordinates
        self.world_coordinate_x_entry.delete(0, tk.END)
        self.world_coordinate_y_entry.delete(0, tk.END)
        self.world_coordinate_z_entry.delete(0, tk.END)
        
        self.world_coordinate_x_entry.insert(0, self.data['world coordinates']['x'])
        self.world_coordinate_y_entry.insert(0, self.data['world coordinates']['y'])
        self.world_coordinate_z_entry.insert(0, self.data['world coordinates']['z'])
        
        # Camera coordinates
        self.camera_corrdinates_x_entry.delete(0, tk.END)
        self.camera_corrdinates_y_entry.delete(0, tk.END)
        self.camera_corrdinates_z_entry.delete(0, tk.END)
        
        self.camera_corrdinates_x_entry.insert(0, self.data['camera coordinates']['x'])
        self.camera_corrdinates_y_entry.insert(0, self.data['camera coordinates']['y'])
        self.camera_corrdinates_z_entry.insert(0, self.data['camera coordinates']['z'])

        # Pixel coordinates
        self.pixel_coordinate_x_entry.delete(0, tk.END)
        self.pixel_coordinate_y_entry.delete(0, tk.END)
        
        self.pixel_coordinate_x_entry.insert(0, self.data['pixel coordinates']['x'])
        self.pixel_coordinate_y_entry.insert(0, self.data['pixel coordinates']['y'])
        
        return

    def _onclick_button_save(self):
        self._save_data_from_entry_to_memory()
        if js.JsonStorage(self.config_filepath).save(self.data) is -1:
            sys.exit('Error: Unable to save data to file.')
        
        self._refresh_data_in_gui()
        
        return