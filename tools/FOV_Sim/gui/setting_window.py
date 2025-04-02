# setting_window.py
import tkinter as tk
from assets.styles.tkinter_style import TkinterStyle
from ..controller.setting_window_controller import SettingWindowController
from gui.selection_window import SelectionWindow
from enum import Enum

class SettingWindow(tk.Toplevel):
    class _Keys(Enum):
        CAMERA_POSITION = 'camera position'
        DISTANCE_CAM_CARBODY = 'distance cam carbody'
    
    label_format_dict = TkinterStyle.label_format_dict
    entry_format_dict = TkinterStyle.entry_format_dict
    button_format_dict = TkinterStyle.button_format_dict
    
    camera_position_widgets_position_dict = {
        'label' : { 'row' : 0, 'column' : 0 }, 'x entry' : { 'row' : 0, 'column' : 1 }, 'y entry' : { 'row' : 0, 'column' : 2 }, 'z entry' : { 'row' : 0, 'column' : 3 },
    }
    distance_cam_carbody_position_dict = {
        'label' : { 'row' : 1, 'column' : 0 }, 'y entry' : { 'row' : 1, 'column' : 1 },
    }
    
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.swc = SettingWindowController()
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

        self._refresh_entrys()
        
    def _onclick_menu_save(self):
        data = {}
        data[self._Keys.CAMERA_POSITION.value] = float(self.camera_position_x_entry.get().replace('E', 'e')), float(self.camera_position_y_entry.get().replace('E', 'e')), float(self.camera_position_z_entry.get().replace('E', 'e'))
        data[self._Keys.DISTANCE_CAM_CARBODY.value] = float(self.distance_cam_carbody_y_entry.get().replace('E', 'e'))
        
        result = self.swc.save_data_to_json(data)
        if result == self.swc.ReturnCode.FILE_NOT_FOUND:
            error_window = SelectionWindow()
            error_window.set_label_text('File not found!')
            error_window.set_button_left_text('OK')
            error_window.set_button_right_text('Cancel')
        
        self._refresh_entrys()
         
    """
    """    
    def _refresh_entrys(self):
        data = self.swc.read_data_from_json()
        keys = data.keys()
        
        key = self._Keys.CAMERA_POSITION.value
        if key in keys:
            self.camera_position_x_entry.delete(0, tk.END)
            self.camera_position_y_entry.delete(0, tk.END)
            self.camera_position_z_entry.delete(0, tk.END)
            self.camera_position_x_entry.insert(0, data[key][0])
            self.camera_position_y_entry.insert(0, data[key][1])
            self.camera_position_z_entry.insert(0, data[key][2])
        
        key = self._Keys.DISTANCE_CAM_CARBODY.value
        if key in keys:
            self.distance_cam_carbody_y_entry.delete(0, tk.END)
            self.distance_cam_carbody_y_entry.insert(0, data[key])