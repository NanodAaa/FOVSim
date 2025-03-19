# MinMagFactorCalculatorGUI.py

import tkinter as tk
from gui import params_window as pw
from gui import selection_window as sw
from cores import JsonStorage as js
from cores import calculate

class MainWindow:
    label_format_dict = { 'font' : ('consolas', 11), 'padx' : 5, 'pady' : 5, 'sticky' : 'w', 'width' : 14 }
    entry_format_dict = { 'font' : ('consolas', 12), 'padx' : 5, 'pady' : 5, 'sticky' : 'ew', 'width' : 13 }
    button_format_dict = { 'bg' : 'lightblue', 'padx' : 5, 'pady' : 5, 'sticky' : 'ewsn', 'width' : 13 }
    
    monitor_point_a_widgets_position_dict = {
        'label' : {'row' : 0, 'column' : 0}, 'x entry' : {'row' : 0, 'column' : 1}, 
        'y entry' : {'row' : 0, 'column' : 2},
    }
    monitor_point_b_widgets_position_dict = {
        'label' : {'row' : 0, 'column' : 4}, 'x entry' : {'row' : 0, 'column' : 5}, 
        'y entry' : {'row' : 0, 'column' : 6},
    }
    
    sensor_point_c_widgets_position_dict = {
        'label' : {'row' : 1, 'column' : 0}, 'x entry' : {'row' : 1, 'column' : 1}, 
        'y entry' : {'row' : 1, 'column' : 2},
    }
    sensor_point_d_widgets_position_dict = {
        'label' : {'row' : 1, 'column' : 4}, 'x entry' : {'row' : 1, 'column' : 5}, 
        'y entry' : {'row' : 1, 'column' : 6},
    }
    
    sensor_point_c_mm_widgets_position_dict = {
        'label' : {'row' : 2, 'column' : 0}, 'x entry' : {'row' : 2, 'column' : 1}, 
        'y entry' : {'row' : 2, 'column' : 2},
    }
    sensor_point_d_mm_widgets_position_dict = {
        'label' : {'row' : 2, 'column' : 4}, 'x entry' : {'row' : 2, 'column' : 5}, 
        'y entry' : {'row' : 2, 'column' : 6},
    }
    
    sensor_point_c_converted_widgets_position_dict = {
        'label' : {'row' : 3, 'column' : 0}, 'x entry' : {'row' : 3, 'column' : 1}, 
        'y entry' : {'row' : 3, 'column' : 2},
    }
    sensor_point_d_converted_widgets_position_dict = {
        'label' : {'row' : 3, 'column' : 4}, 'x entry' : {'row' : 3, 'column' : 5}, 
        'y entry' : {'row' : 3, 'column' : 6},
    }
    
    sensor_point_c_mm_converted_widgets_position_dict = {
        'label' : {'row' : 4, 'column' : 0}, 'x entry' : {'row' : 4, 'column' : 1}, 
        'y entry' : {'row' : 4, 'column' : 2},
    } 
    sensor_point_d_mm_converted_widgets_position_dict = {
        'label' : {'row' : 4, 'column' : 4}, 'x entry' : {'row' : 4, 'column' : 5}, 
        'y entry' : {'row' : 4, 'column' : 6},
    }
    
    world_point_f_widgets_position_dict = {
        'label' : {'row' : 5, 'column' : 0}, 'x entry' : {'row' : 5, 'column' : 1}, 
        'y entry' : {'row' : 5, 'column' : 2}, 'z entry' : {'row' : 5, 'column' : 3},
    }
    world_point_e_widgets_position_dict = {
        'label' : {'row' : 5, 'column' : 4}, 'x entry' : {'row' : 5, 'column' : 5}, 
        'y entry' : {'row' : 5, 'column' : 6}, 'z entry' : {'row' : 5, 'column' : 7},
    }
    
    button_widgets_position_dict = {
    }
    
    config_filename = 'config.json'
    config_filepath = f'./{config_filename}'
    
    def __init__(self, root):
        self.root = root
        self._init_config_data()
        self._init_gui()
        self.root.mainloop()
        
        return
        
    def _init_config_data(self):
        self.data = calculate.data
        storage = js.JsonStorage(self.config_filepath)
        temp_data = storage.load()
        if temp_data != {}:
            self.data = temp_data
        else:
            storage.save(self.data)
        
    def _init_gui(self):
        self.root = tk.Tk()
        self.root.title("Minimum Magnification Factor Calculator")
        
        # Menu
        self.menu = tk.Menu(self.root)
        
        # Menu - Help
        self.help_menu = tk.Menu(self.menu, tearoff=False)
        self.help_menu.add_command(label='About', command=self._onclick_menu_help_about)
        self.menu.add_cascade(label='Help', menu=self.help_menu)
        
        # Menu - Tools
        self.tools_menu = tk.Menu(self.menu, tearoff=False)
        self.tools_menu.add_command(label='Run', command=self._onclick_menu_tools_run)
        self.tools_menu.add_command(label='Refresh', command=self._onclick_menu_tools_refresh)
        self.menu.add_cascade(label='Tools', menu=self.tools_menu)
        
        # Menu - Options
        self.options_menu = tk.Menu(self.menu, tearoff=False)
        self.options_menu.add_command(label="Params", command=self._onclick_menu_options_params)    # Params Setting
        self.options_menu.add_command(label='Reset', command=self._onclick_menu_options_reset)      # Reset
        self.menu.add_cascade(label='Options', menu=self.options_menu)
        
        self.root.config(menu=self.menu)
        
        # Monitor Point A
        self.monitor_point_a_label = tk.Label(self.root, text='MP_A', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.monitor_point_a_label.grid(row=self.monitor_point_a_widgets_position_dict['label']['row'], column=self.monitor_point_a_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.monitor_point_a_x_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_point_a_x_entry.grid(row=self.monitor_point_a_widgets_position_dict['x entry']['row'], column=self.monitor_point_a_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_point_a_x_entry.insert(0, self.data['monitor point a']['x'])
        
        self.monitor_point_a_y_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_point_a_y_entry.grid(row=self.monitor_point_a_widgets_position_dict['y entry']['row'],column=self.monitor_point_a_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_point_a_y_entry.insert(0, self.data['monitor point a']['y'])
        
        # Monitor Point B
        self.monitor_point_b_label = tk.Label(self.root, text='MP_B', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.monitor_point_b_label.grid(row=self.monitor_point_b_widgets_position_dict['label']['row'], column=self.monitor_point_b_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.monitor_point_b_x_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_point_b_x_entry.grid(row=self.monitor_point_b_widgets_position_dict['x entry']['row'], column=self.monitor_point_b_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_point_b_x_entry.insert(0, self.data['monitor point b']['x'])
        
        self.monitor_point_b_y_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.monitor_point_b_y_entry.grid(row=self.monitor_point_b_widgets_position_dict['y entry']['row'], column=self.monitor_point_b_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.monitor_point_b_y_entry.insert(0, self.data['monitor point b']['y'])
        
        # Sensor Point C
        self.sensor_point_c_label = tk.Label(self.root, text='SP_C', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.sensor_point_c_label.grid(row=self.sensor_point_c_widgets_position_dict['label']['row'], column=self.sensor_point_c_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.sensor_point_c_x_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_c_x_entry.grid(row=self.sensor_point_c_widgets_position_dict['x entry']['row'], column=self.sensor_point_c_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_c_x_entry.insert(0, self.data['sensor point c']['x'])
        
        self.sensor_point_c_y_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_c_y_entry.grid(row=self.sensor_point_c_widgets_position_dict['y entry']['row'], column=self.sensor_point_c_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_c_y_entry.insert(0, self.data['sensor point c']['y'])
        
        # Sensor Point D
        self.sensor_point_d_label = tk.Label(self.root, text='SP_D', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.sensor_point_d_label.grid(row=self.sensor_point_d_widgets_position_dict['label']['row'], column=self.sensor_point_d_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.sensor_point_d_x_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_d_x_entry.grid(row=self.sensor_point_d_widgets_position_dict['x entry']['row'], column=self.sensor_point_d_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_d_x_entry.insert(0, self.data['sensor point d']['x'])
        
        self.sensor_point_d_y_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_d_y_entry.grid(row=self.sensor_point_d_widgets_position_dict['y entry']['row'], column=self.sensor_point_d_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_d_y_entry.insert(0, self.data['sensor point d']['y'])
        
        # Sensor Point C (mm)
        self.sensor_point_c_mm_label = tk.Label(self.root, text='SP_C (mm)', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.sensor_point_c_mm_label.grid(row=self.sensor_point_c_mm_widgets_position_dict['label']['row'], column=self.sensor_point_c_mm_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.sensor_point_c_mm_x_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_c_mm_x_entry.grid(row=self.sensor_point_c_mm_widgets_position_dict['x entry']['row'], column=self.sensor_point_c_mm_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_c_mm_x_entry.insert(0, self.data['sensor point c mm']['x'])
        
        self.sensor_point_c_mm_y_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_c_mm_y_entry.grid(row=self.sensor_point_c_mm_widgets_position_dict['y entry']['row'], column=self.sensor_point_c_mm_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_c_mm_y_entry.insert(0, self.data['sensor point c mm']['y'])
        
        # Sensor Point D (mm)
        self.sensor_point_d_mm_label = tk.Label(self.root, text='SP_D (mm)', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.sensor_point_d_mm_label.grid(row=self.sensor_point_d_mm_widgets_position_dict['label']['row'], column=self.sensor_point_d_mm_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.sensor_point_d_mm_x_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_d_mm_x_entry.grid(row=self.sensor_point_d_mm_widgets_position_dict['x entry']['row'], column=self.sensor_point_d_mm_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_d_mm_x_entry.insert(0, self.data['sensor point d mm']['x'])
        
        self.sensor_point_d_mm_y_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_d_mm_y_entry.grid(row=self.sensor_point_d_mm_widgets_position_dict['y entry']['row'], column=self.sensor_point_d_mm_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_d_mm_y_entry.insert(0, self.data['sensor point d mm']['y'])
        
        # Senssor Point C Converted
        self.sensor_point_c_converted_label = tk.Label(self.root, text='SP_C_Conv', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.sensor_point_c_converted_label.grid(row=self.sensor_point_c_converted_widgets_position_dict['label']['row'], column=self.sensor_point_c_converted_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.sensor_point_c_converted_x_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_c_converted_x_entry.grid(row=self.sensor_point_c_converted_widgets_position_dict['x entry']['row'], column=self.sensor_point_c_converted_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_c_converted_x_entry.insert(0, self.data['sensor point c converted']['x'])
        
        self.sensor_point_c_converted_y_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_c_converted_y_entry.grid(row=self.sensor_point_c_converted_widgets_position_dict['y entry']['row'], column=self.sensor_point_c_converted_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_c_converted_y_entry.insert(0, self.data['sensor point c converted']['y'])
        
        # Sensor Point D Converted
        self.sensor_point_d_converted_label = tk.Label(self.root, text='SP_D_Conv', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.sensor_point_d_converted_label.grid(row=self.sensor_point_d_converted_widgets_position_dict['label']['row'], column=self.sensor_point_d_converted_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.sensor_point_d_converted_x_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_d_converted_x_entry.grid(row=self.sensor_point_d_converted_widgets_position_dict['x entry']['row'], column=self.sensor_point_d_converted_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_d_converted_x_entry.insert(0, self.data['sensor point d converted']['x'])
        
        self.sensor_point_d_converted_y_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_d_converted_y_entry.grid(row=self.sensor_point_d_converted_widgets_position_dict['y entry']['row'], column=self.sensor_point_d_converted_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_d_converted_y_entry.insert(0, self.data['sensor point d converted']['y'])
        
        # Senssor Point C Converted (mm)
        self.sensor_point_c_mm_converted_label = tk.Label(self.root, text='SP_C_Conv (mm)', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.sensor_point_c_mm_converted_label.grid(row=self.sensor_point_c_mm_converted_widgets_position_dict['label']['row'], column=self.sensor_point_c_mm_converted_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.sensor_point_c_mm_converted_x_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_c_mm_converted_x_entry.grid(row=self.sensor_point_c_mm_converted_widgets_position_dict['x entry']['row'], column=self.sensor_point_c_mm_converted_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_c_mm_converted_x_entry.insert(0, self.data['sensor point c mm converted']['x'])
        
        self.sensor_point_c_mm_converted_y_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_c_mm_converted_y_entry.grid(row=self.sensor_point_c_mm_converted_widgets_position_dict['y entry']['row'], column=self.sensor_point_c_mm_converted_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_c_mm_converted_y_entry.insert(0, self.data['sensor point c mm converted']['y'])
        
        # Sensor Point D Converted (mm)
        self.sensor_point_d_mm_converted_label = tk.Label(self.root, text='SP_D_Conv (mm)', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.sensor_point_d_mm_converted_label.grid(row=self.sensor_point_d_mm_converted_widgets_position_dict['label']['row'], column=self.sensor_point_d_mm_converted_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.sensor_point_d_mm_converted_x_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_d_mm_converted_x_entry.grid(row=self.sensor_point_d_mm_converted_widgets_position_dict['x entry']['row'], column=self.sensor_point_d_mm_converted_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_d_mm_converted_x_entry.insert(0, self.data['sensor point d mm converted']['x'])
        
        self.sensor_point_d_mm_converted_y_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_point_d_mm_converted_y_entry.grid(row=self.sensor_point_d_mm_converted_widgets_position_dict['y entry']['row'], column=self.sensor_point_d_mm_converted_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_point_d_mm_converted_y_entry.insert(0, self.data['sensor point d mm converted']['y'])
        
        # World Point F
        self.world_point_f_label = tk.Label(self.root, text='WP_F', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.world_point_f_label.grid(row=self.world_point_f_widgets_position_dict['label']['row'], column=self.world_point_f_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.world_point_f_x_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_point_f_x_entry.grid(row=self.world_point_f_widgets_position_dict['x entry']['row'], column=self.world_point_f_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_point_f_x_entry.insert(0, self.data['world point f']['x'])
        
        self.world_point_f_y_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_point_f_y_entry.grid(row=self.world_point_f_widgets_position_dict['y entry']['row'], column=self.world_point_f_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_point_f_y_entry.insert(0, self.data['world point f']['y'])
        
        self.world_point_f_z_entry  = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_point_f_z_entry.grid(row=self.world_point_f_widgets_position_dict['z entry']['row'], column=self.world_point_f_widgets_position_dict['z entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_point_f_z_entry.insert(0, self.data['world point f']['z'])
        
        # World Point E
        self.world_point_e_label = tk.Label(self.root, text='WP_E', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.world_point_e_label.grid(row=self.world_point_e_widgets_position_dict['label']['row'], column=self.world_point_e_widgets_position_dict['label']['column'], padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.world_point_e_x_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_point_e_x_entry.grid(row=self.world_point_e_widgets_position_dict['x entry']['row'], column=self.world_point_e_widgets_position_dict['x entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_point_e_x_entry.insert(0, self.data['world point e']['x'])
        
        self.world_point_e_y_entry = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_point_e_y_entry.grid(row=self.world_point_e_widgets_position_dict['y entry']['row'], column=self.world_point_e_widgets_position_dict['y entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_point_e_y_entry.insert(0, self.data['world point e']['y'])
        
        self.world_point_e_z_entry  = tk.Entry(self.root, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_point_e_z_entry.grid(row=self.world_point_e_widgets_position_dict['z entry']['row'], column=self.world_point_e_widgets_position_dict['z entry']['column'], padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_point_e_z_entry.insert(0, self.data['world point e']['z'])
    
    def _refresh_data_in_gui(self):
        """ 
        Refresh data in GUI.
        """
        # Monitor Point A Coordinates
        self.monitor_point_a_x_entry.delete(0, tk.END)
        self.monitor_point_a_y_entry.delete(0, tk.END)
        self.monitor_point_a_x_entry.insert(0, self.data['monitor point a']['x'])
        self.monitor_point_a_y_entry.insert(0, self.data['monitor point a']['y'])
        
        # Monitor Point B Coordinates
        self.monitor_point_b_x_entry.delete(0, tk.END)
        self.monitor_point_b_y_entry.delete(0, tk.END)
        self.monitor_point_b_x_entry.insert(0, self.data['monitor point b']['x'])
        self.monitor_point_b_y_entry.insert(0, self.data['monitor point b']['y'])
        
        # Sensor Point C Coordinates
        self.sensor_point_c_x_entry.delete(0, tk.END)
        self.sensor_point_c_y_entry.delete(0, tk.END)
        self.sensor_point_c_x_entry.insert(0, self.data['sensor point c']['x'])
        self.sensor_point_c_y_entry.insert(0, self.data['sensor point c']['y'])
        
        # Sensor Point C (mm) Coordinates
        self.sensor_point_c_mm_x_entry.delete(0, tk.END)
        self.sensor_point_c_mm_y_entry.delete(0, tk.END)
        self.sensor_point_c_mm_x_entry.insert(0, self.data['sensor point c mm']['x'])
        self.sensor_point_c_mm_y_entry.insert(0, self.data['sensor point c mm']['y'])
        
        # Sensor Point D Coordinates
        self.sensor_point_d_x_entry.delete(0, tk.END)
        self.sensor_point_d_y_entry.delete(0, tk.END)
        self.sensor_point_d_x_entry.insert(0, self.data['sensor point d']['x'])
        self.sensor_point_d_y_entry.insert(0, self.data['sensor point d']['y'])
        
        # Sensor Point D (mm) Coordinates
        self.sensor_point_d_mm_x_entry.delete(0, tk.END)
        self.sensor_point_d_mm_y_entry.delete(0, tk.END)
        self.sensor_point_d_mm_x_entry.insert(0, self.data['sensor point d mm']['x'])
        self.sensor_point_d_mm_y_entry.insert(0, self.data['sensor point d mm']['y'])
        
        # Sensor Point C Converted Coordinates
        self.sensor_point_c_converted_x_entry.delete(0, tk.END)
        self.sensor_point_c_converted_y_entry.delete(0, tk.END)
        self.sensor_point_c_converted_x_entry.insert(0, self.data['sensor point c converted']['x'])
        self.sensor_point_c_converted_y_entry.insert(0, self.data['sensor point c converted']['y'])
        
        # Sensor Point C (mm) Converted Coordinates
        self.sensor_point_c_mm_converted_x_entry.delete(0, tk.END)
        self.sensor_point_c_mm_converted_y_entry.delete(0, tk.END)
        self.sensor_point_c_mm_converted_x_entry.insert(0, self.data['sensor point c mm converted']['x'])
        self.sensor_point_c_mm_converted_y_entry.insert(0, self.data['sensor point c mm converted']['y'])
        
        # Sensor Point D Converted Coordinates
        self.sensor_point_d_converted_x_entry.delete(0, tk.END)
        self.sensor_point_d_converted_y_entry.delete(0, tk.END)
        self.sensor_point_d_converted_x_entry.insert(0, self.data['sensor point d converted']['x'])
        self.sensor_point_d_converted_y_entry.insert(0, self.data['sensor point d converted']['y'])
        
        # Sensor Point D (mm) Converted Coordinates
        self.sensor_point_d_mm_converted_x_entry.delete(0, tk.END)
        self.sensor_point_d_mm_converted_y_entry.delete(0, tk.END)
        self.sensor_point_d_mm_converted_x_entry.insert(0, self.data['sensor point d mm converted']['x'])
        self.sensor_point_d_mm_converted_y_entry.insert(0, self.data['sensor point d mm converted']['y'])
        
        # World Point E Coordinates
        self.world_point_e_x_entry.delete(0, tk.END)
        self.world_point_e_y_entry.delete(0, tk.END)
        self.world_point_e_z_entry.delete(0, tk.END)
        self.world_point_e_x_entry.insert(0, self.data['world point e']['x'])
        self.world_point_e_y_entry.insert(0, self.data['world point e']['y'])
        self.world_point_e_z_entry.insert(0, self.data['world point e']['z'])
        
        # World Point F Coordinates
        self.world_point_f_x_entry.delete(0, tk.END)
        self.world_point_f_y_entry.delete(0, tk.END)
        self.world_point_f_z_entry.delete(0, tk.END)
        self.world_point_f_x_entry.insert(0, self.data['world point f']['x'])
        self.world_point_f_y_entry.insert(0, self.data['world point f']['y'])
        self.world_point_f_z_entry.insert(0, self.data['world point f']['z'])
        
    def _onclick_menu_tools_run(self):
        """
        Calculate Horizontal Minimum Magnification Factor.
        """
        self.data = calculate.calculate_hor_min_mag_factor(self.data)
        
        js.JsonStorage(self.config_filepath).save(self.data)
        self._refresh_data_in_gui()
        
        return
    
    def _onclick_menu_tools_refresh(self):
        """ 
        """
        self.data = js.JsonStorage(self.config_filepath).load()
        self._refresh_data_in_gui()
        
        return
        
    def _onclick_menu_help_about(self):
        return    
    
    def _onclick_menu_options_params(self):
        params_window = pw.ParamsWindow(self.root)
        self._onclick_menu_tools_refresh()
        return
    
    def _onclick_menu_options_reset(self):
        """ 
        Reset data in memory & config file.
        """
        # Show message box
        selection_window = sw.SelectionWindow(self.root)
        
        label_text = 'Are you sure to reset data?'
        selection_window.set_label_text(label_text)
        selection_window.set_button_left_text('OK')
        selection_window.set_button_right_text('Cancel')
        selection_window.set_modal()
        
        button_status = selection_window.get_button_status()
        
        if button_status == selection_window.ButtonStatus.LEFT:
            self.data = calculate.data
            js.JsonStorage(self.config_filepath).save(self.data)
            self.data = js.JsonStorage(self.config_filepath).load()
            self._refresh_data_in_gui()
        
        elif button_status == selection_window.ButtonStatus.RIGHT:
            return
        
        else:
            return
        
        return