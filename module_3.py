# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 03:10:10 2018

@author: Nishna
"""

class task3a :
    """Class to process task3 a """
    def __init__(self, datafile) :
        self.__datafile = datafile


    """ a. Find the most popular user_agent"""
    def view_by_user_agent(self, gui = None):
        import module_common as cf
        import plot_functions as pf
        
        """Generate data"""
        records = cf.common_functions.get_values(self.__datafile, 'visitor_useragent').to_frame()
        view_count = records.groupby(['visitor_useragent']).size()
        """Dictionary which has the data for views by user_agent of the document"""
        country_dict = {view_count.index[i] : view_count[i] for i in range(0,len(view_count))}
        """Plot histogram"""
        if(gui is None) :
            pf.plot_functions.plot_hist(country_dict,
                          xlab = "Country",
                          ylab = "Views",
                          title = "Views By User_Agent") 
        else:
            return pf.plot_functions.plot_hist_gui(country_dict,
                          xlab = "Country",
                          ylab = "Views",
                          title = "Views By User_Agent") 
    
class task3b :
    """Class to process task3 b """
    def __init__(self, datafile) :
        self.__datafile = datafile
        
    def view_by_browser(self, gui = None):
        """ a. Find the most popular browser"""
        import module_common as cf
        import plot_functions as pf
        
        """Generate data"""
        useragents = cf.common_functions.get_values(self.__datafile, 'visitor_useragent').tolist()
        browser_lists = map(self.browser,useragents) #Get the list from each user agent
        browser_flatlist = cf.common_functions.get_flat_list(browser_lists) #Flatten the above list
        
        """Dictionary which has the data for views by browser of the document"""
        country_dict = cf.common_functions.get_count_dictionary(browser_flatlist) 
                
        """Plot histogram"""
        if(gui is None) :
            pf.plot_functions.plot_hist(country_dict, xlab = "Browser", ylab = "Views", title = "Views By Browser") 
        else :
            return pf.plot_functions.plot_hist_gui(country_dict, xlab = "Browser", ylab = "Views", title = "Views By Browser") 
        
    #Function that retreives the browser names from user_agent using regular expression
    def browser(self,n):
        import re
        return re.findall(r'(\w+)/',n)
     