# MinMagFactorCalculatorGUI.py

import tkinter as tk

class MinMagFactorCalculatorGUI:
    
    def _init_(self, master='master'):
        self.master = master
        
    def init_gui(self):
        self.master = tk.Tk()
        self.master.title("Minimum Magnification Factor Calculator")
        
        