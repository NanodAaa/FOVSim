# points_table_window.py

import tkinter as tk
from tkinter import ttk
from cores import calculate
from cores import JsonStorage as js

class PointsTableWindow(tk.Toplevel):
    """ 
    """
    config_filename = 'config.json'
    config_filepath = f'./{config_filename}'
    
    label_format_dict = { 'font' : ('consolas', 11), 'padx' : 5, 'pady' : 5, 'sticky' : 'w', 'width' : 14 }
    entry_format_dict = { 'font' : ('consolas', 12), 'padx' : 5, 'pady' : 5, 'sticky' : 'ew', 'width' : 13 }
    button_format_dict = { 'bg' : 'lightblue', 'padx' : 5, 'pady' : 5, 'sticky' : 'ewsn', 'width' : 13 }
    tree_format_dict = { 'column width' : 100, 'column anchor' : 'center', }
    
    tree_columns = ('World_mm', 'Sensor_Conv_mm', 'Sensor_Conv_pixel', 'Sensor_mm', 'Sensor_pixel', 'Monitor_mm', 'Monitor_pixel')
    
    def __init__(self, root):
        super().__init__(root)
        
        self._init_config_data()
        self._init_gui()
        self.grab_set()     # Set window to modal
        self.wait_window()
        
    def _init_config_data(self):
        self.data = calculate.data
        storage = js.JsonStorage(self.config_filepath)
        temp_data = storage.load()
        if temp_data != {}:
            self.data = temp_data
        else:
            storage.save(self.data)
            
        return
        
    def _init_gui(self):
        self.title('Points Table')
        self.geometry("1000x500")
        self.pack_propagate(True)
        
        # Treeview
        self.tree = ttk.Treeview(self, columns=self.tree_columns, show='headings')
        for tree_column in self.tree_columns:
            self.tree.heading(tree_column, text=tree_column)
        
        for tree_column in self.tree_columns:
            self.tree.column(tree_column, width=self.tree_format_dict['column width'], anchor=self.tree_format_dict['column anchor'])
            
        points_world_mm = self.data['points within ef']
        points_sensor_converted_mm = self.data['points within ef sensor converted mm']
        points_sensor_converted_pixel = self.data['points within ef sensor converted pixel']
        points_sensor_mm = self.data['points within ef sensor mm']
        points_sensor_pixel = self.data['points within ef sensor pixel']
        points_monitor_mm = self.data['points within ef monitor mm']
        points_monitor_pixel = self.data['points within ef monitor pixel']
            
        data = []
        for index in range(0, len(points_world_mm)):
            temp = (
                str(tuple(points_world_mm[index].values())), 
                str(tuple(points_sensor_converted_mm[index].values())), 
                str(tuple(points_sensor_converted_pixel[index].values())), 
                str(tuple(points_sensor_mm[index].values())), 
                str(tuple(points_sensor_pixel[index].values())), 
                str(tuple(points_monitor_mm[index].values())), 
                str(tuple(points_monitor_pixel[index].values())),
            )
            data.append(temp)
        
        for row in data:
            self.tree.insert("", tk.END, values=row)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        return