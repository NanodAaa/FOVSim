import tkinter as tk
from assets.styles.tkinter_style import TkinterStyle

class HelpWindow(tk.Toplevel):
    _label_format_dict = TkinterStyle.label_format_dict
    
    def __init__(self, root:tk.Tk):
        super().__init__(root)
        self.root = root
        
        self._init_gui()
        
    def _init_gui(self):
        self.title('Help')
        self.geometry('600x400')
        
        self.camera_position_label = self._create_insturctions_label('Camera Position: 摄像机位置 (x, y, z)')
        self.distance_cam_carbody_label = self._create_insturctions_label('Distance E.P. Carbody: 眼点到车身的距离 (m)')
        self.distance_cam_ground_label = self._create_insturctions_label('Distance Cam Ground: 摄像机到地面的距离 (m)')
        self.fitting_func_coefs_label = self._create_insturctions_label('Fitting Func Coefs: 拟合函数系数 (a, b, c, d, e, f)')
        self.fitting_func_coefs_reverse_label = self._create_insturctions_label('Fitting Func Coefs Reverse: 拟合函数反转系数 (a, b, c, d, e, f)')
        self.camera_pose_label = self._create_insturctions_label('Camera Pose: 摄像机姿态 (roll, pitch, yaw)')
        self.sensor_params_label = self._create_insturctions_label('Sensor Params: 传感器参数 (width, height, pixel size)')
        self.monitor_params_label = self._create_insturctions_label('Monitor Params: 显示器参数 (width, height, pixel size)')
        self.crop_region_label = self._create_insturctions_label('Crop Region: 裁剪区域 (x1, y1, x2, y2)')
        
    def _create_insturctions_label(self, text: str, **kwargs) -> tk.Label:
        label = tk.Label(self, text=text, font=self._label_format_dict['font'])
        label.pack(anchor='w')
        return label
   
        