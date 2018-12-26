# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 04:01:41 2018

@author: Nishna
"""

import tkinter as tk
class task6:
    """Class to process task6 GUI """
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Python Data Analysis")
        self.__root.configure(background = "black")
        
        tk.Label(self.__root, text="Data Analysis of Document Tracker!",bg = "black", fg = "white", font = "none 12 bold").grid(row = 0, column = 1)     
        
        tk.Label(self.__root, text="Enter the filename!",bg = "black", fg = "white", font = "none 8 bold").grid(row = 3, column = 0)     
        self.datafile_entry = tk.Entry(self.__root, width=80, bg = "white") #text box for entering the filename
        self.datafile_entry.grid(row = 3, column = 1)
        
        tk.Label(self.__root, text="Enter the document id!",bg = "black", fg = "white", font = "none 8 bold").grid(row = 5, column = 0)     
        self.doc_id_entry = tk.Entry(self.__root, width=80, bg = "white") #text box for entering the document id
        self.doc_id_entry.grid(row = 5, column = 1)
        
        tk.Label(self.__root, text="Enter the visitor id!",bg = "black", fg = "white", font = "none 8 bold").grid(row = 7, column = 0)     
        self.user_id_entry = tk.Entry(self.__root, width=80, bg = "white") #text box for entering the visitor id
        self.user_id_entry.grid(row = 7, column = 1)
        
        tk.Button(self.__root,text = "Views_By_Country", command = self.fn_2a).grid(row = 12, column = 0) #invoke fn_2a on clicking button
        tk.Button(self.__root,text = "Views_By_Continent", command = self.fn_2b).grid(row = 12, column = 1) #invoke fn_2b on clicking button
        
        
        tk.Button(self.__root,text = "Views_By_Useragent", command = self.fn_3a).grid(row = 18, column = 0)
        tk.Button(self.__root,text = "Views_By_Browsers", command = self.fn_3b).grid(row = 18, column = 1)
        
        tk.Button(self.__root,text = "View_Readers", command = self.fn_4a).grid(row = 20, column = 0) 
        """"
        tk.Button(self.__root,text = "View_ReadingList", command = self.fn_4b).grid(row = 20, column = 1) 
        tk.Button(self.__root,text = "View_Also_Like_Documents", command = self.fn_4c).grid(row = 22, column = 0) 
        tk.Button(self.__root,text = "View_Top10_Popular_Docs", command = self.fn_4d).grid(row = 22, column = 1) 
        tk.Button(self.__root,text = "View_Also_Like_Graph", command = self.fn_5).grid(row = 25, column = 0) 
        """
        self.__root.mainloop()
    
    def fn_2a(self):
        """Actions to perform on clicking the button Views by country """
        import pandas as pd
        import module_2 as m2
        import matplotlib
        import numpy as np
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
        
        entered_datafile = self.datafile_entry.get()
        df = pd.read_json(entered_datafile, lines = True, orient='columns')# read json datafaile
        sample_2a = m2.task2a(self.doc_id_entry.get(),df) #instantiate respective class
        dict, xlab, ylab, title = sample_2a.view_by_country(gui = 'true') #get the details to plot
        
        """extracting values"""
        y = dict.keys() 
        y_pos = np.arange(len(y))
        x = dict.values()
        print(x)
        print(y)
        """plotting"""
        f = matplotlib.pyplot.Figure(figsize=(5,4), dpi=100)
        ax = f.add_subplot(111)
        ax.bar(y_pos, x)
        ax.set_xticklabels(labels = y)
        canvas = FigureCanvasTkAgg(f)
        canvas.get_tk_widget().grid(row=3, column=3, rowspan=6)
        canvas.show()
        
    def fn_2b(self):
        """Actions to perform on clicking the button Views by continent"""
        import pandas as pd
        import module_2 as m2
        import matplotlib
        import numpy as np
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
        
        entered_datafile = self.datafile_entry.get()
        df = pd.read_json(entered_datafile, lines = True, orient='columns')# read json datafaile
        sample_2b = m2.task2b(self.doc_id_entry.get(),df) #instantiate respective class
        dict, xlab, ylab, title = sample_2b.view_by_continent(gui = 'true') #get the details to plot
        
        """extracting values"""
        y = dict.keys() 
        y_pos = np.arange(len(y))
        x = dict.values()
        print(x)
        print(y)
        """plotting"""
        f = matplotlib.pyplot.Figure(figsize=(5,4), dpi=100)
        ax = f.add_subplot(111)
        ax.bar(y_pos, x)
        ax.set_xticklabels(labels = y)
        canvas = FigureCanvasTkAgg(f)
        canvas.get_tk_widget().grid(row=3, column=3, rowspan=6)
        canvas.show()
        
    def fn_3a(self):
        """Actions to perform on clicking the button Views by user agent """
        import pandas as pd
        import module_3 as m3
        import matplotlib
        import numpy as np
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
        
        entered_datafile = self.datafile_entry.get()
        df = pd.read_json(entered_datafile, lines = True, orient='columns')# read json datafaile
        sample_3a = m3.task3a(df) #instantiate respective class
        dict, xlab, ylab, title = sample_3a.view_by_user_agent(gui = 'true') #get the details to plot
        
        """extracting values"""
        y = dict.keys() 
        y_pos = np.arange(len(y))
        x = dict.values()
        print(x)
        print(y)
        """plotting"""
        f = matplotlib.pyplot.Figure(figsize=(5,7), dpi=100)
        ax = f.add_subplot(111)
        ax.bar(y_pos, x)
        ax.set_xticklabels(labels = y)
        canvas = FigureCanvasTkAgg(f)
        canvas.get_tk_widget().grid(row=3, column=3, rowspan=6)
        canvas.show()

    def fn_3b(self):
        """Actions to perform on clicking the button Views by browser """
        import pandas as pd
        import module_3 as m3
        import matplotlib
        import numpy as np
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
        
        entered_datafile = self.datafile_entry.get()
        df = pd.read_json(entered_datafile, lines = True, orient='columns')# read json datafaile
        sample_3b = m3.task3b(df) #instantiate respective class
        dict, xlab, ylab, title = sample_3b.view_by_browser(gui = 'true') #get the details to plot
        
        """extracting values"""
        y = dict.keys() 
        y_pos = np.arange(len(y))
        x = dict.values()
        print(x)
        print(y)
        """plotting"""
        f = matplotlib.pyplot.Figure(figsize=(5,4), dpi=100)
        ax = f.add_subplot(111)
        ax.bar(y_pos, x)
        ax.set_xticklabels(labels = y)
        canvas = FigureCanvasTkAgg(f)
        canvas.get_tk_widget().grid(row=3, column=3, rowspan=6)
        canvas.show()

    def fn_4a(self):
        """Actions to perform on clicking the button Views Readers """
        import pandas as pd
        import module_4 as m4
        
        """output the list"""
        output = tk.Text(self.__root, width = 75, height = 6,wrap = tk.WORD, background = 'white')
        output.grid(row = 28, column = 1)
        output.delete(0.0,tk.END)
        try :
            entered_datafile = self.datafile_entry.get()
            datafile = pd.read_json(entered_datafile, lines = True, orient='columns')# read json datafaile
            sample_4 = m4.task4(datafile) #instantiate respective class
            readers_list = sample_4.get_readers(self.doc_id_entry.get()) #get the readers list to display
            print(readers_list)
        except :
            readers_list = "Please check the entered details"
        output.insert(tk.END,readers_list)
            

        
    

        
    