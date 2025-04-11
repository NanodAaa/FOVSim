import tkinter as tk
from controller.fov_sim_controller import FovSimController
from assets.styles.tkinter_style import TkinterStyle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from models.config_model import LOGGER
from gui.selection_window import SelectionWindow
from gui.setting_window import SettingWindow
from matplotlib.figure import Figure
from dataclasses import dataclass
from models.config_model import ConfigModel
from matplotlib.patches import Rectangle
from gui.edit_simulation_points_window import EditSimulationPointsWindow
from tkinter import ttk

class FOVSimWindow(tk.Tk):
    @dataclass
    class ShowCanvasParams:
        canvas0_title: str = None
        canvas0_x_label: str = None
        canvas0_y_label: str = None
        canvas0_x_data: list = None
        canvas0_y_data: list = None
        canvas0_data_label: str = None
        crop_region: list = None
        sensor_width: int = None
        sensor_height: int = None
        
        canvas1_title: str = None
        canvas1_x_label: str = None
        canvas1_y_label: str = None
        canvas1_x_data: list = None
        canvas1_y_data: list = None
        canvas1_data_label: str = None
        monitor_width: int = None
        monitor_height: int = None
    
    label_format_dict = TkinterStyle.label_format_dict
    entry_format_dict = TkinterStyle.entry_format_dict
    button_format_dict = TkinterStyle.button_format_dict
    
    canvas_widgets_dict = {
        'x label' : 'Width', 'y label' : 'Height',
    }
    
    canvas_position_dict = {
        'row' : 0, 'column' : 0,
    }
    
    result_table_position_dict = {
        'row' : 1, 'column' : 0,
    }
    
    def __init__(self, root: tk.Tk=None):
        super().__init__(root)
        self.root = root
        self.config_model = ConfigModel()
        self.controller = FovSimController()
        self.show_canvas_params = self.ShowCanvasParams()
        
        # Profile value & variable to transfer to setting window.
        self.profile_list = self.config_model.profile_selection_combobox_values
        self.profile_var = tk.StringVar(value=self.profile_list[0])

        self.setting_window = None
        self.edit_simulation_points_window = None

        self._init_setting_data()
        self._init_gui()
        self.protocol('WM_DELETE_WINDOW', self._onclose)
        
        self.mainloop()
        
    def _init_setting_data(self):
        if self.controller.init_setting_data() == self.controller.ReturnCode.FILE_NOT_FOUND:
            error_window = SelectionWindow(self)
            error_window.set_label_text('')
            
    def _init_gui(self):
        self.title('FOVSim')
        #self.geometry('400x400')
        
        # Menu
        self.menu = tk.Menu(self)
        self.menu.add_command(label='Run', command=self._onclick_menu_run)
        self.menu.add_command(label='Settings', command=self._onclick_menu_settings)
        self.menu.add_command(label='Edit Simulation Points (Incoming)', command=self._onclick_menu_edit_simulation_points)
        
        self.config(menu=self.menu)

        # Canvas
        # Create Matplotlib figure.
        self.show_canvas_params.canvas0_x_label = 'Width'
        self.show_canvas_params.canvas0_y_label = 'Height'
        self.show_canvas_params.canvas0_title = 'Sensor'

        self.show_canvas_params.canvas1_x_label = 'Width'
        self.show_canvas_params.canvas1_y_label = 'Height'
        self.show_canvas_params.canvas1_title = 'Monitor'
        self._show_canvas(self.show_canvas_params)
        
        self._init_result_table()
        
    def _init_result_table(self):
        self.result_table = ttk.Treeview(self, columns=self.config_model.result_table_column, show='headings')
        
        for column in self.config_model.result_table_column:
            self.result_table.heading(column, text=column)
            self.result_table.column(column, anchor=self.config_model.table_format_dict[self.config_model.TableFormatKeys.ANCHOR.value], width=self.config_model.table_format_dict[self.config_model.TableFormatKeys.WIDTH.value])
        
        self.result_table.grid(row=self.result_table_position_dict['row'], column=self.result_table_position_dict['column'], sticky=self.config_model.table_format_dict[self.config_model.TableFormatKeys.STICKY.value])
        
    def _onclick_menu_settings(self):
        if self.setting_window is None or not self.setting_window.winfo_exists():
            self.setting_window = SettingWindow(self, self.profile_list, self.profile_var)
    
    def _onclick_menu_edit_simulation_points(self):
        if self.edit_simulation_points_window is None or not self.edit_simulation_points_window.winfo_exists():
            self.edit_simulation_points_window = EditSimulationPointsWindow(self)
    
    def _onclick_menu_run(self):
        """
        Run Fov simulation. 
        """
        LOGGER.info('\nUser clicked menu-run.\n')
        
        data = self.controller.read_data_from_json(self.profile_var.get())
        if data is None or data == {}:
            LOGGER.error(f'\nError when getting data from json file! Data: {data}\n')
            error_window = SelectionWindow(self)
            error_window.set_label_text('Error when getting data from json file!')
            error_window.set_button_left_text('OK')
            error_window.set_button_right_text('Cancel')
            return
        
        LOGGER.debug(f'Done getting data. Data: {data}\n')
        
        # Getting regulation points coordinates relative to E.P.
        regulation_points = self.controller.get_regulation_points(data[self.config_model.Keys.CAMERA_POSITION.value], data[self.config_model.Keys.DISTANCE_CAM_CARBODY.value], data[self.config_model.Keys.DISTANCE_CAM_GROUND.value], self.profile_var.get())
        if regulation_points == self.controller.ReturnCode.DATA_TYPE_ERROR:
            LOGGER.error('\nError when getting regulation points!\n')
            error_window = SelectionWindow(self)
            error_window.set_label_text('Input data type error - camera_coordinates, distance_camera_carbody, distance_camera_ground.')
            return        
        elif regulation_points == self.controller.ReturnCode.DATA_VALUE_ERROR:
            LOGGER.error('\nError when getting regulation points!\n')
            error_window = SelectionWindow(self)
            error_window.set_label_text('Input data value error - camera_coordinates, distance_camera_carbody, distance_camera_ground.')
            return
        elif regulation_points is None or regulation_points == []:
            LOGGER.error(f'\nError when getting regulation points! Data: {regulation_points} \n')
            error_window = SelectionWindow(self)
            error_window.set_label_text('Error when getting regulation points!')
            error_window.set_button_left_text('OK')
            error_window.set_button_right_text('Cancel')
            return
        
        LOGGER.debug(f'Done getting regulation points. Points: {regulation_points}\n')
        
        # Transform regulation points from relative to EP into relative to camera.
        regulation_points_camera_coordinates = self.controller.transfrom_regulation_points_into_cam_coordinates(data[self.config_model.Keys.CAMERA_POSITION.value], regulation_points)
        if regulation_points_camera_coordinates == self.controller.ReturnCode.DATA_TYPE_ERROR:
            LOGGER.error('\nError when transforming regulation points!\n')
            error_window = SelectionWindow(self)
            error_window.set_label_text(f'Input data type error - camera_coordinates, regulation_points.')
            return   
        elif regulation_points_camera_coordinates == self.controller.ReturnCode.DATA_VALUE_ERROR:
            LOGGER.error('\nError when transforming regulation points!\n')
            error_window = SelectionWindow(self)
            error_window.set_label_text(f'Input data value error - camera_coordinates should be a list of 3 elements.')
            return
        
        LOGGER.debug(f'Done getting regulation points\' coordinates relative to camera. Data: {regulation_points_camera_coordinates}\n')
        
        # Applying World->Sensor transform to 'regulation_points_camera_coordinates'        
        regulation_points_sensor_coordinates = self.controller.regulation_points_world_sensor_transform(regulation_points_camera_coordinates, data[self.config_model.Keys.CAMERA_POSE.value], data[self.config_model.Keys.SENSOR_PARAMS.value], data[self.config_model.Keys.MONITOR_PARAMS.value], data[self.config_model.Keys.FITTING_FUNC_COEFS.value])
        LOGGER.debug(f'Done transforming regulation points from world into monitor coordinates. Data: {regulation_points_sensor_coordinates}\n')
        
        # Show canvas
        # Sensor canvas.
        self.show_canvas_params.sensor_width = data[self.config_model.Keys.SENSOR_PARAMS.value][0]
        self.show_canvas_params.sensor_height = data[self.config_model.Keys.SENSOR_PARAMS.value][1]
        self.show_canvas_params.crop_region = data[self.config_model.Keys.CROP_REGION.value]
        self.show_canvas_params.canvas0_x_data = [point[0] for point in regulation_points_sensor_coordinates]
        self.show_canvas_params.canvas0_y_data = [point[1] for point in regulation_points_sensor_coordinates]
        self.show_canvas_params.canvas0_data_label = 'Regulation points'
        
        # Get monitor params.
        # Getting coordinates after transforming original point into new original point.
        regulation_points_sensor_coordinates_converted = []
        for point in regulation_points_sensor_coordinates:
            point_converted = self.controller.coordinates_transform(point, [0, 0], [self.show_canvas_params.crop_region[0], self.show_canvas_params.crop_region[1]])
            if point_converted == self.controller.ReturnCode.DATA_TYPE_ERROR:
                LOGGER.error('\nError when transforming regulation points!\n')
                error_window = SelectionWindow(self)
                error_window.set_label_text(f'Input data type error - A, B.')
                return       
            elif point_converted == self.controller.ReturnCode.DATA_VALUE_ERROR:
                LOGGER.error('\nError when transforming regulation points!\n')
                error_window = SelectionWindow(self)
                error_window.set_label_text(f'Input data value error - length of A and B is not equal.')
                return
            
            regulation_points_sensor_coordinates_converted.append(point_converted)
        
        """ # Getting monitor params by converting coordinates from sensor size to monitor size.
        regulation_points_monitor_coordinates = []
        for point in regulation_points_sensor_coordinates_converted:
            point_converted = self.controller.sensor_monitor_transform(point, data[self.config_model.Keys.SENSOR_PARAMS.value], data[self.config_model.Keys.MONITOR_PARAMS.value])
            if point_converted == self.controller.ReturnCode.DATA_TYPE_ERROR:
                LOGGER.error('\nError when transforming regulation points!\n')
                error_window = SelectionWindow(self)
                error_window.set_label_text(f'Input data type error - A, B.')
                return
            
            elif point_converted == self.controller.ReturnCode.DATA_VALUE_ERROR:
                LOGGER.error('\nError when transforming regulation points!\n')
                error_window = SelectionWindow(self)
                error_window.set_label_text(f'Input data value error - length of A and B is not equal.')
                return
            
            regulation_points_monitor_coordinates.append(point_converted)
         """
         
        # Monitor canvas.
        self.show_canvas_params.monitor_width = data[self.config_model.Keys.MONITOR_PARAMS.value][0]
        self.show_canvas_params.monitor_height = data[self.config_model.Keys.MONITOR_PARAMS.value][1]
        self.show_canvas_params.canvas1_x_data = [point[0] for point in regulation_points_sensor_coordinates_converted]
        self.show_canvas_params.canvas1_y_data = [point[1] for point in regulation_points_sensor_coordinates_converted]
        self.show_canvas_params.canvas1_data_label = 'Regulation points'
        
        LOGGER.debug(f'Showing canvas. Data: {self.show_canvas_params}')
        
        self._show_canvas(self.show_canvas_params)
        
        # Update result table.
        self._clear_result_table()
        points_name = ['A', 'B', 'C', 'D', 'E']
        for index in range(0, len(regulation_points_camera_coordinates)):
            if regulation_points_sensor_coordinates[index][0] in range(data[self.config_model.Keys.CROP_REGION.value][0], data[self.config_model.Keys.CROP_REGION.value][0] + data[self.config_model.Keys.CROP_REGION.value][2]) and regulation_points_sensor_coordinates[index][1] in range(data[self.config_model.Keys.CROP_REGION.value][1], data[self.config_model.Keys.CROP_REGION.value][1] + data[self.config_model.Keys.CROP_REGION.value][3]):
                result = 'OK'
            else:
                result = 'NG'

            values = []
            values.append(regulation_points_camera_coordinates[index][0]) # X_mm
            values.append(regulation_points_camera_coordinates[index][1]) # Y_mm
            values.append(regulation_points_camera_coordinates[index][2]) # Z_mm
            values.append(regulation_points_sensor_coordinates[index][0]) # Sensor_x
            values.append(regulation_points_sensor_coordinates[index][1]) # Sensor_y
            values.append(regulation_points_sensor_coordinates_converted[index][0]) # Monitor_x
            values.append(regulation_points_sensor_coordinates_converted[index][1]) # Monitor_y
            values.append(points_name[index]) # Name
            values.append(result) # Result
            
            self.result_table.insert('', 'end', values=values)  
        
    def _onclose(self):
        self.destroy()
        
    def _show_canvas(self, params: ShowCanvasParams):
        """ 
        Show canvas
        """        
        # Create Matplotlib figure.
        fig = Figure(figsize=(10, 4), dpi=100)
        
        # Sensor canvas.
        if params.canvas0_title is None or params.canvas0_x_label is None or params.canvas0_y_label is None:
            error_window = SelectionWindow(self)
            error_window.set_label_text('Please set the canvas0 title, xlabel, ylabel, row, column')
            return
        
        axes_sensor = fig.add_subplot(1, 2, 1)
        axes_sensor.set_title(params.canvas0_title)
        axes_sensor.set_xlabel(params.canvas0_x_label)
        axes_sensor.set_ylabel(params.canvas0_y_label)
        axes_sensor.invert_yaxis()
        axes_sensor.grid(True, linestyle='--')  # Add grid lines

        # Set axis limits based on sensor size, if is set.
        if params.sensor_width and params.sensor_height:
            axes_sensor.set_xlim(0, params.sensor_width)
            axes_sensor.set_ylim(params.sensor_height, 0)
        else:
            LOGGER.debug('Canvas0 Width and height are not set.')
        
        # Draw crop region rectangle if crop region is set.
        if params.crop_region:
            rect = Rectangle((params.crop_region[0], params.crop_region[1]), params.crop_region[2], params.crop_region[3], linewidth=1, edgecolor='r', facecolor='none')
            axes_sensor.add_patch(rect)
        else:
            LOGGER.debug('Crop region is not set.')
        
        if params.canvas0_x_data and params.canvas0_y_data and params.canvas0_data_label:
            axes_sensor.scatter(params.canvas0_x_data, params.canvas0_y_data, label=params.canvas0_data_label)
            axes_sensor.legend()
        else:
            LOGGER.debug('Canvas0 X data, Y data or data label is not set.')
        
        # Monitor canvas.
        if params.canvas1_title is None or params.canvas1_x_label is None or params.canvas1_y_label is None:
            error_window = SelectionWindow(self)
            error_window.set_label_text('Please set the canvas1 title, xlabel, ylabel, row, column')
            return
        
        axes_monitor = fig.add_subplot(1, 2, 2)
        axes_monitor.set_title(params.canvas1_title)
        axes_monitor.set_xlabel(params.canvas1_x_label)
        axes_monitor.set_ylabel(params.canvas1_y_label)
        axes_monitor.invert_yaxis()
        axes_monitor.grid(True, linestyle='--')  # Add grid lines
        
        if params.monitor_width and params.monitor_height:
            axes_monitor.set_xlim(0, params.monitor_width)
            axes_monitor.set_ylim(params.monitor_height, 0)
        else:
            LOGGER.debug('Canvas1 Width and height are not set.')

        if params.canvas1_x_data and params.canvas1_y_data and params.canvas1_data_label:
            axes_monitor.scatter(params.canvas1_x_data, params.canvas1_y_data, label=params.canvas1_data_label)
            axes_monitor.legend()
        else:
            LOGGER.debug('Canvas1 X data, Y data or data label is not set.')
        
        # Bind figure to tkinter's canvas.
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=self.canvas_position_dict['row'], column=self.canvas_position_dict['column'])        

    def _clear_result_table(self):
        """ 
        Clear result table.
        """
        for item in self.result_table.get_children():
            self.result_table.delete(item)