import tkinter as tk
from tkinter import ttk

class EditSimulationPointsWindow(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        
        self._init_gui()
        
    def _init_gui(self):
        self.title("Edit Simulation Points")
        self.geometry("400x300")
        
        # Menu
        self.menu = tk.Menu(self)
        
        self.menu.add_command(label='Add Point', command=self._add_point)
        self.menu.add_command(label='Delete Point', command=self._delete_point)
        
        self.config(menu=self.menu)
        
        self._init_table()
        
    def _init_table(self):
        columns = ['Point Name', 'Coordinates', 'Color']
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        
    def _add_point(self):
        # Logic to add a point
        pass
    
    def _delete_point(self):
        # Logic to delete a point
        pass