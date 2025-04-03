import tkinter as tk
from ..controller.fov_sim_controller import FovSimController
from assets.styles.tkinter_style import TkinterStyle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ..models.config_model import LOGGER
from gui.selection_window import SelectionWindow
from ..gui.setting_window import SettingWindow
from matplotlib.figure import Figure
from dataclasses import dataclass
from ..models.config_model import ConfigModel
from matplotlib.patches import Rectangle

class FOVSimWindow(tk.Toplevel):
    @dataclass
    class ShowCanvasParams:
        title: str = None
        x_label: str = None
        y_label: str = None
        row: int = None
        column: int = None
        x_data: list = None
        y_data: list = None
        data_label: str = None
        crop_region: list = None
        width: int = None
        height: int = None
    
    label_format_dict = TkinterStyle.label_format_dict
    entry_format_dict = TkinterStyle.entry_format_dict
    button_format_dict = TkinterStyle.button_format_dict
    
    canvas_widgets_dict = {
        'x label' : 'Width', 'y label' : 'Height',
    }
    
    canvas_position_dict = {
        'row' : 0, 'column' : 0,
    }
    
    def __init__(self, root: tk.Tk):
        super().__init__(root)
        self.root = root
        self.config_model = ConfigModel()
        self.controller = FovSimController()
        self.show_canvas_params = self.ShowCanvasParams()
        self.show_canvas_params.x_label = 'Width'
        self.show_canvas_params.y_label = 'Height'
        self.show_canvas_params.title = 'Fov Sim'
        self.show_canvas_params.row = 0
        self.show_canvas_params.column = 0
        
        self._init_setting_data()
        self._init_gui()
        self.protocol('WM_DELETE_WINDOW', self._onclose)
        
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
        
        # Menu - Tools
        self.tools_menu = tk.Menu(self.menu, tearoff=0)
        self.tools_menu.add_command(label='Settings', command=self._onclick_menu_tools_settings)
        self.menu.add_cascade(label='Tools', menu=self.tools_menu)
        
        self.config(menu=self.menu)

        # Canvas
        # Create Matplotlib figure.
        self._show_canvas(self.show_canvas_params)
        
    def _onclick_menu_tools_settings(self):
        setting_window = SettingWindow(self)
    
    def _onclick_menu_run(self):
        """
        Run Fov simulation. 
        """
        LOGGER.info('User clicked menu-run.')
        
        # Get regulation points.
        data = self.controller.read_data_from_json()
        LOGGER.debug(f'Done getting data. Data: {data}')
        
        # Getting regulation points coordinates relative to E.P.
        regulation_points = self.controller.get_regulation_points_II_ep(data[self.config_model.Keys.CAMERA_POSITION.value], data[self.config_model.Keys.DISTANCE_CAM_CARBODY.value], data[self.config_model.Keys.DISTANCE_CAM_GROUND.value])
        LOGGER.debug(f'Done getting regulation points. Points: {regulation_points}')
        
        # Transform regulation points from EP coordinates to Camera coordinates.
        regulation_points_camera_coordinates = self.controller.transfrom_regulation_points_into_cam_coordinates(data[self.config_model.Keys.CAMERA_POSITION.value], regulation_points)
        LOGGER.debug(f'Done gettingb regulation points\' coordinates relative to camera. Data: {regulation_points_camera_coordinates}')
        
        # Applying World->Sensor transform to 'regulation_points_camera_coordinates'
        data = self.controller.read_data_from_json()
        regulation_points_sensor_coordinates = self.controller.regulation_points_world_sensor_transform(regulation_points_camera_coordinates, data[self.config_model.Keys.CAMERA_POSE.value], data[self.config_model.Keys.SENSOR_PARAMS.value], data[self.config_model.Keys.MONITOR_PARAMS.value], data[self.config_model.Keys.FITTING_FUNC_COEFS.value])
        LOGGER.debug(f'Done transforming regulation points from world into monitor coordinates. Data: {regulation_points_sensor_coordinates}')
        
        # Show canvas
        self.show_canvas_params.width = data[self.config_model.Keys.SENSOR_PARAMS.value][0]
        self.show_canvas_params.height = data[self.config_model.Keys.SENSOR_PARAMS.value][1]
        self.show_canvas_params.crop_region = data[self.config_model.Keys.CROP_REGION.value]
        self.show_canvas_params.x_data = [point[0] for point in regulation_points_sensor_coordinates]
        self.show_canvas_params.y_data = [point[1] for point in regulation_points_sensor_coordinates]
        self.show_canvas_params.data_label = 'Regulation points'
        
        self._show_canvas(self.show_canvas_params)
        
    def _onclose(self):
        self.destroy()
        self.root.deiconify()
        
    def _show_canvas(self, params: ShowCanvasParams):
        """ 
        Show canvas
        """        
        if params.title is None or params.x_label is None or params.y_label is None or params.row is None or params.column is None:
            error_window = SelectionWindow(self)
            error_window.set_label_text('Please set the title, xlabel, ylabel, row, column')
            return
        
        # Create Matplotlib figure.
        fig = Figure()
        axes = fig.add_subplot(1, 1, 1)
        axes.set_title(params.title)
        axes.set_xlabel(params.x_label)
        axes.set_ylabel(params.y_label)
        axes.invert_yaxis()

        if params.width and params.height:
            axes.set_xlim(0, params.width)
            axes.set_ylim(params.height, 0)
        else:
            LOGGER.debug('Width and height are not set.')
        
        if params.crop_region:
            rect = Rectangle((params.crop_region[0], params.crop_region[1]), params.crop_region[2], params.crop_region[3], linewidth=1, edgecolor='r', facecolor='none')
            axes.add_patch(rect)
        else:
            LOGGER.debug('Crop region is not set.')
        
        if params.x_data and params.y_data and params.data_label:
            axes.scatter(params.x_data, params.y_data, label=params.data_label)
            axes.legend()
        else:
            LOGGER.debug('X data, Y data or data label is not set.')
        
        # Bind figure to tkinter's canvas.
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=self.canvas_position_dict['row'], column=self.canvas_position_dict['column'])        
