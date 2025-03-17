# MinMagFactorCalculatorGUI.py

import tkinter as tk
from gui import params_window as pw

class MainWindow:
    def __init__(self, root):
        self.root = root
        self._init_gui()
        self.root.mainloop()
        
        return
        
    def _init_gui(self):
        self.root = tk.Tk()
        self.root.title("Minimum Magnification Factor Calculator")
        
        # Menu
        self.menu = tk.Menu(self.root)
        
        # Menu - Help
        self.help_menu = tk.Menu(self.menu, tearoff=False)
        self.help_menu.add_command(label='About', command=self._onclick_menu_help_about)
        self.menu.add_cascade(label='Help', menu=self.help_menu)
        
        # Menu - Options
        self.options_menu = tk.Menu(self.menu, tearoff=False)
        self.options_menu.add_command(label="Params", command=self._onclick_menu_options_params)
        self.menu.add_cascade(label='Options', menu=self.options_menu)
        
        self.root.config(menu=self.menu)
        
    def _onclick_menu_help_about(self):
        return    
    
    def _onclick_menu_options_params(self):
        params_window = pw.ParamsWindow(self.root)
        return