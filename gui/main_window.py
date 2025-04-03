# main_windows.py

from tools.MinMagFactor.gui import min_mag_factor_window as mafw
from tools.W2CTransform.gui import w2ctransform_window as w2cw
from tools.FOV_Sim.gui import fov_sim_window as fsw
import tkinter as tk
from assets.styles.tkinter_style import TkinterStyle

class MainWindow(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self._init_gui()
        self._start()
        
    def _init_gui(self):
        label_format_dict = TkinterStyle.label_format_dict
        button_format_dict = TkinterStyle.button_format_dict
        
        self.geometry('300x300')
        self.title('CMSSim')
        
        # Menu
        self.menu = tk.Menu(self)
        
        """ # Menu-Tools
        self.tools_menu = tk.Menu(self.menu, tearoff=False)
        self.tools_menu.add_command(label='FOV Sim', command=self._onclick_menu_tools_fov_sim)
        self.tools_menu.add_command(label='MinMagFactor Calculator', command=self._onclick_menu_tools_min_mag_factor_calculator)
        self.tools_menu.add_command(label='W2CTransformer', command=self._onclick_menu_tools_w2ctransformer)
        self.menu.add_cascade(label='Tools', menu=self.tools_menu) """
        
        # Menu - Help
        self.help_menu = tk.Menu(self.menu, tearoff=False)
        self.help_menu.add_command(label='About', command=self._onclick_menu_help_about)
        self.menu.add_cascade(label='Help', menu=self.help_menu)
        
        self.config(menu=self.menu)
        
        self.label = tk.Label(self, text='CMSSim', font=label_format_dict['font'], padx=label_format_dict['padx'], pady=label_format_dict['pady'], width=label_format_dict['width'])
        self.label.pack(pady=20)
        
        self.fov_sim_button = tk.Button(self, text='FOV Sim', command=self._onclick_menu_tools_fov_sim, padx=button_format_dict['padx'], pady=button_format_dict['pady'], width=20)
        self.fov_sim_button.pack(pady=5)
        
        self.min_mag_factor_button = tk.Button(self, text='MinMagFactor Calculator', command=self._onclick_menu_tools_min_mag_factor_calculator, padx=button_format_dict['padx'], pady=button_format_dict['pady'], width=20)
        self.min_mag_factor_button.pack(pady=5)
        
        self.w2ctransformer_button = tk.Button(self, text='W2CTransformer', command=self._onclick_menu_tools_w2ctransformer, padx=button_format_dict['padx'], pady=button_format_dict['pady'], width=20)
        self.w2ctransformer_button.pack(pady=5)
        
    def _start(self):
        self.mainloop()
        return
    
    def _hide(self):
        self.withdraw()
      
    def _onclick_menu_tools_min_mag_factor_calculator(self):
        self._hide()
        min_mag_factor_window = mafw.MinMagFactorWindow(self)
        return
    
    def _onclick_menu_tools_w2ctransformer(self):
        self._hide()
        w2ctransformer_window = w2cw.W2CTransform(self)
        return
    
    def _onclick_menu_tools_fov_sim(self):
        self._hide()
        fov_sim_window = fsw.FOVSimWindow(self)
        return
    
    def _onclick_menu_help_about(self):
        return
    