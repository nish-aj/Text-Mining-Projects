# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:46:21 2018

@author: Nishna
"""




class plot_functions :
    """class with functions exclusively for plotting"""
    
    def plot_hist(dict, xlab, ylab, title): # plot histogram
        import matplotlib.pyplot as plt
        import numpy as np
        
        """extracting values"""
        y = dict.keys() 
        y_pos = np.arange(len(y))
        x = dict.values()
        
        """plotting"""
        plt.bar(y_pos, x, align='center', alpha=0.5)
        plt.xticks(y_pos, y, fontsize=8, rotation='vertical')
        #plt.xticks(y_pos, y, rotation='vertical')
        
        plt.ylabel(ylab) 
        plt.xlabel(xlab)
        plt.title(title)
        plt.show()
        
    def plot_hist_gui(dict, xlab, ylab, title) :
        return dict, xlab, ylab, title