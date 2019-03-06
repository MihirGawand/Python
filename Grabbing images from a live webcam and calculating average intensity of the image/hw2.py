# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:47:39 2018

@author: Mihir Gawand
"""
#import requests
from webcam import Webcam
#from PIL import Image
#from io import StringIO, BytesIO
import numpy as np
from filters import mean_filter
import matplotlib.pyplot as plt



class MUcamera:
    
    def __init__(self):
        self.w = Webcam()
        self.start = self.w.start()
        self.im = self.w.grab_image()
        self.w.register_callback(self.average_intensity,1)
        self.avg_intensity= []
        self.images = [] 
        self.filtered = []
        self.f,self.ax = plt.subplots(1,1)
        
#To find the average intensity       
    def average_intensity(self,image):
        pix_val = list(image.getdata())
        pixel_intensity = []
        for x in pix_val:
            avg = sum(x)/len(x)
            pixel_intensity.append(avg)
        self.avg_pixel = np.average(pixel_intensity)
        self.avg_intensity.append(self.avg_pixel)
        return self.avg_intensity

#To find the average filtered intensity using width as 3        
    def average_intensity_filtered(self):
        
        width = 3
        if len(self.avg_intensity) >= 5:
            for x in range(len(self.avg_intensity)-2):
                self.filtered.append((self.avg_intensity[x]+self.avg_intensity[x+1]+self.avg_intensity[x+2])/width)
            return self.filtered
        else:
            self.filtered = self.avg_intensity
            return self.filtered 
        
#To stop the execution of webcam.py   
    def stop(self):
        self.w.stop()
        self.average_intensity_mean_plot()
        self.average_intensity_filtered_plot()
        self.daytime()
        self.most_common_color()
        
    #To plot the average intensity        
    def average_intensity_mean_plot(self):

        self.ax.plot(self.avg_intensity, 'C1', label = 'Average')
        self.ax.legend()
        self.ax.set_xlabel('Image Number')
        self.ax.set_ylabel('Intensity')
        self.ax.set_title('Image Intensity')
        
#To plot the average filtered intensity        
    def average_intensity_filtered_plot(self):
        self.average_intensity_filtered()
        self.ax.plot(self.filtered, 'C2', label = 'Filtered')
        self.ax.legend()


#To check if it is daytime or nighttime        
    def daytime(self):
        self.average = np.mean(np.mean(self.im,axis = 1))
        if self.average >= 95:
            return print("True")
        else:
            return print("False")

#To check the most common color       
    def most_common_color(self):
        w,h = self.im.size
        pixels = self.im.getcolors(w*h)
        most_frequent_pixel = pixels[0]
        for count, color in pixels:
            if count > most_frequent_pixel[0]:
                most_frequent_pixel = (count,color)
        proportion = most_frequent_pixel[0]/len(pixels)
        return print('The most common color is {}'. format(most_frequent_pixel[1]), 'with a count of {}'.format(most_frequent_pixel[0]), 'and the proportion of pixels is {}'. format(proportion))

        
    
    
if __name__ == '__main__':
    a = MUcamera()
    input('Hit Enter to Stop')
    a.stop()
    


    
