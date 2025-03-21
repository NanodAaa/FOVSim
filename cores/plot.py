# plot.py

import matplotlib.pyplot as plt

class Plot:
    def __init__(self):
        return
    
    def plot_points_in_pixel_area(self, area_size: tuple, points_x: tuple, points_y: tuple):
        """ 
        Plot points in an area.  
        area_size: (width, height) in pixel.  
        points_list: ( (x1, y1), (x2, y2) ... (xn, yn) )  
        """   
        width = area_size[0]
        height = area_size[1]
        
        plt.scatter(points_x, points_y)
        plt.xlim(0, width)
        plt.ylim(height, 0)
        
        plt.xlabel('Width')
        plt.ylabel('Height')
        plt.title('Plot')
        
        plt.show()
        
        return