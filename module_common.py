# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:00:46 2018

@author: Nishna

Contains functions common for modules 1 , 2 & 3
"""
import pandas as pd
import functools as ft

class common_functions :
    """Class which has the functions commonly used in two or more classes"""           
    def read_data(filepath):
        """ A function to read the json data as pandas dataframe """
        return pd.read_json(filepath, lines = True, orient='columns')
    
    def get_values(data, output_attribute, input_attribute= None, value = None):
        """Method overloading"""
        if(input_attribute is not None and value is not None) :
            """Function that returns a filtered list of values from specified column
            input 1. Variable which has the column to be matched with value
            2. Value of the selection criteria
            3. Dataframe
            4. Name of the attribute whose values are to be returned
            output - values of attribute in parameter 4, for the records that matches the selection criteria """
            return (data[data[input_attribute] == value][output_attribute])
        else:
            """Overloaded Function that returns a filtered list of values from specified column
            input 1. Dataframe
                  2. Name of the attribute whose values are to be returned
            output - values of attribute in parameter 2, for the records that matches the selection criteria """
            return (data[output_attribute])
    
    def get_records(input_attribute, value, data):
         """ Function that returns a filtered set of records
         input 1. Variable which has the column to be matched with value
               2. Value of the selection criteria
               3. Dataframe
         output - the records that matches the selection criteria """
         return data[data[input_attribute] == value]    
     
    def get_count_dictionary(input_list) :
        """ Function that returns a dictionary with item as keys and the no of occurances in the list as values"""
        return {x : input_list.count(x) for x in input_list}
    
    def get_flat_list(input_list) :
        """ Function that returns the flattened list"""
        return ft.reduce(lambda x,y: x + y,input_list)
    
    