# -*- coding: utf-8 -*-
"""
Created on Thu May 31 22:15:54 2018

@author: sgmih
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:47:39 2018

@author: sgmih
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
#        self.grabimage = self.w.grab_image()
        self.avg_intensity= []
        self.images = [] 
        self.filt_list = []
        self.f,self.ax = plt.subplots(1,1)
        self.day = []
        
        
    def average_intensity(self):

        pix_val = list(self.im.getdata())
        pixel_intensity = []
        for x in pix_val:
            avg = sum(x)/len(x)
            pixel_intensity.append(avg)
        self.avg_pixel = np.average(pixel_intensity)
        self.avg_intensity.append(self.avg_pixel)
        return self.avg_intensity
#        avg  = np.mean(np.mean(image,axis=1))
#        self.avg_list.append(avg)
        
    def average_intensity_filtered(self):
        width = 3
#        i=0
        
        if len(self.avg_intensity) >= 5:
            for x in range(len(self.avg_intensity)-2):
                self.filt_list.append((self.avg_intensity[x]+self.avg_intensity[x+1]+self.avg_intensity[x+2])/width)
            return self.filt_list
        else:
            return self.filt_list 
#        while i+width <= len(self.filt_list):            
#            y = self.filt_list[i:i+width]
#            total_sum=sum(y)/width
#            self.filt_list.append(total_sum)
#            i+=1

        
        
#    def stop(self):
#        self.w.stop()
#        self.average_intensity_mean_plot()
#        self.average_intensity_filtered_plot()
#        
#    def average_intensity_mean_plot(self):
#        self.ax.plot(self.avg_intensity, 'C1')
#        self.ax.set_xlabel('Image Number')
#        self.ax.set_ylabel('Intensity')
#        self.ax.set_title('Image Intensity')
##        
#    def average_intensity_filtered_plot(self):
#        self.average_intensity_filtered()
#        self.ax.plot(self.filt_list, 'C2')
#        
    def daytime(self):
        self.average = np.mean(np.mean(self.im,axis = 1))
        if self.average >= 95:
#            self.i.append(self.i)
            return print("True")
        else:
            return print("False")
##        
    def most_common_color(self):
        w,h = self.im.size
        pixels = self.im.getcolors(w*h)
        print(len(pixels))
        most_frequent_pixel = pixels[0]
        for count, color in pixels:
            if count > most_frequent_pixel[0]:
                most_frequent_pixel = (count,color)
                    
    #        compare("Most Common", image, most_frequent_pixel[1])
    #    print(self.most_frequent_pixel)
        return print(most_frequent_pixel[0]/len(pixels),most_frequent_pixel)
    
    def stop(self):
        self.w.stop()
        self.daytime()
        self.most_common_color()
        self.average_intensity_mean_plot()
        self.average_intensity_filtered_plot()
        
    def average_intensity_mean_plot(self):
        self.average_intensity()
        self.ax.plot(self.avg_intensity, 'C1')
        self.ax.set_xlabel('Image Number')
        self.ax.set_ylabel('Intensity')
        self.ax.set_title('Image Intensity')
#        
    def average_intensity_filtered_plot(self):
        self.average_intensity_filtered()
        self.ax.plot(self.filt_list, 'C2')
        
        
#    w = Webcam()
#    w.register_callback(callback, 1)
#    w.start()
#    
#    im = w.grab_image()
#    pix_val = list(im.getdata())
##    print(pix_val)
#    pixel_intensity = []
#    avg_intensity = []
#    
#    for x in pix_val:
#        avg = sum(x)/len(x)
#        pixel_intensity.append(avg) 
#        
##    print(pixel_intensity)
#    avg_pixel = np.average(pixel_intensity)
#    avg_intensity.append(avg_pixel)
#    print(avg_intensity)
#
#    input('Hit Enter to Stop')
#    
#    w.stop()
    
    
if __name__ == '__main__':
    a = MUcamera()
    input('Hit Enter to Stop')
    a.stop()
    
#    print(a)
    
    
#    url = 'http://webcam.oregonstate.edu/cam/mu/live/live.jpg'
#     w = Webcam()
#     callback = None
#     w.register_callback(callback,1)
#     w.start()
#    w = Webcam()
#    callback = None
#    w.register_callback(callback,1)
#    w.start()


#    
#   
#    
#    input('Hit Enter to Stop')
#    
#    w.stop()

    
