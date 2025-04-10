# selection_window.py
# Template of selection window.

import tkinter as tk
from enum import Enum, auto

class SelectionWindow(tk.Toplevel):
    """ 
    Create a selection window with two buttons and a label.  
    The window is modal and will wait for user input before proceeding.  
    When user clicks a button, the window will close and return the button status.  
    class ButtonStatus(Enum):
        LEFT = auto()
        RIGHT = auto()
    """
    class ButtonStatus(Enum):
        LEFT = auto()
        RIGHT = auto()
    
    label_format_dict = { 'font' : ('consolas', 11), 'padx' : 5, 'pady' : 5, 'sticky' : 'ew', 'width' : 14 }
    entry_format_dict = { 'font' : ('consolas', 12), 'padx' : 5, 'pady' : 5, 'sticky' : 'ew', 'width' : 13 }
    button_format_dict = { 'bg' : 'lightblue', 'padx' : 5, 'pady' : 5, 'sticky' : 'ew', 'width' : 13 }

    label_widgets_position_dict = {
        'label' : { 'row' : 0, 'column' : 0 },
    }
    
    button_widgets_position_dict = {
        'button left' : { 'row' : 2, 'column' : 0 },
        'button right' : { 'row' : 2, 'column' : 1 },
    }
    
    def __init__(self, root):
        super().__init__(root)
        self.button_status = None
        self._init_gui()
    
    def _init_gui(self):
        self.title('Warning')
        self.geometry('300x100')
        
        self.label = tk.Label(self, text='label', font=self.label_format_dict['font'])
        self.label.grid(row=self.label_widgets_position_dict['label']['row'], column=self.label_widgets_position_dict['label']['column'], columnspan=2, padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.button_left = tk.Button(self, text='left button', bg=self.button_format_dict['bg'], width=self.button_format_dict['width'], command=self._onclick_button_left)
        self.button_left.grid(row=self.button_widgets_position_dict['button left']['row'], column=self.button_widgets_position_dict['button left']['column'], padx=self.button_format_dict['padx'], pady=self.button_format_dict['pady'], sticky=self.button_format_dict['sticky'])        
        
        self.button_right = tk.Button(self, text='right button', bg=self.button_format_dict['bg'], width=self.button_format_dict['width'], command=self._onclick_button_right)
        self.button_right.grid(row=self.button_widgets_position_dict['button right']['row'], column=self.button_widgets_position_dict['button right']['column'], padx=self.button_format_dict['padx'], pady=self.button_format_dict['pady'], sticky=self.button_format_dict['sticky'])        
        
        return
        
    def _onclick_button_left(self):
        self.button_status = self.ButtonStatus.LEFT
        self.destroy()
        return
    
    def _onclick_button_right(self):
        self.button_status = self.ButtonStatus.RIGHT
        self.destroy()
        return
    
    def set_label_text(self, input_text):
        self.label.config(text=input_text)
        return
    
    def set_button_left_text(self, input_text):
        self.button_left.config(text=input_text)
        return
    
    def set_button_right_text(self, input_text):
        self.button_right.config(text=input_text)
        return
    
    def get_button_status(self):
        if self.button_status == self.ButtonStatus.LEFT:
            return self.ButtonStatus.LEFT
        elif self.button_status == self.ButtonStatus.RIGHT:
            return self.ButtonStatus.RIGHT
        else:
            return None
        
    def set_modal(self):
        self.grab_set()
        self.wait_window()