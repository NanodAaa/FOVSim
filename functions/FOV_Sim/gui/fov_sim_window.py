import tkinter as tk
from assets.styles.tkinter_style import TkinterStyle

class FOVSimWindow(tk.Toplevel):
    label_format_dict = TkinterStyle.label_format_dict
    entry_format_dict = TkinterStyle.entry_format_dict
    button_format_dict = TkinterStyle.button_format_dict
    
    def __init__(self, root):
        self.root = root
        super().__init__(root)
        self._init_gui()
        self.protocol('WM_DELETE_WINDOW', self._onclose)
        
    def _init_gui(self):
        self.title('FOVSim')
        
        return
    
    def _onclose(self):
        self.destroy()
        self.root.deiconify()
        return
