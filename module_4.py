# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 14:24:17 2018

@author: Nishna
"""
import module_common as cf

class task4 :
    """Class to process task4  """
    def __init__(self, datafile) :
        self.__datafile= datafile
    
    def get_readers(self, document_id):
        """ a.  Function that returns all visitor UUIDs of readers of a document
            input : document id
            output : list of visitors that read the document"""
        records = cf.common_functions.get_records('subject_doc_id', document_id, self.__datafile) #Get records for sub_doc_id = 'aaaaa' 
        readers_list = cf.common_functions.get_values(records, 'visitor_uuid', 'event_type', 'read').tolist() #Get visitor_uuid for event_type = read from previous step
        return readers_list

    def get_read_documents(self, user_id):
        """ a.  Function that returns all document UUIDs read by a visitor
            input : visitor_uuid
            output : list of documents read by the visitor"""
        records = cf.common_functions.get_records('visitor_uuid', user_id,  self.__datafile) #Get records for visitor_uuid = 'aaaaa' 
        docs = cf.common_functions.get_values(records, 'subject_doc_id', 'event_type', 'read').tolist()    #Get document_id for event_type = read from previous step
        return docs

    def get_also_likes(self, document_id, user_id = None) :
        """ a.  Function that returns all document UUIDs read by a visitor
            input : visitor_uuid
            output : list of documents read by the visitor"""
        readers = self.get_readers(document_id) # Get the readers of the document
        dict_reading = {x : list(set(self.get_read_documents(x))) for x in readers} #Create dictionary of the form reader: readinglist (contains only unique values of the document ids)
        return (dict_reading)
    
    def sort_no_of_readers(self,dict_reading) :
        """ Function to create dictionary of the form doc_id : no_of_readers
        step 1 : create a flat list of the dict values
        step 2 : count the number of occurances of each unique values """
        doc_list = cf.common_functions.get_flat_list(dict_reading.values())
        dict_reading_count = cf.common_functions.get_count_dictionary(doc_list)
        dict_reading_count_desc = sorted(dict_reading_count, key=dict_reading_count.__getitem__, reverse=True) # sort the dictionary based on descending order of values
        return dict_reading_count_desc
    
    def get_also_likes_sorted(self, document_id, decorator, user_id = None) :
        """ a.  Function that returns all document UUIDs read by a visitor
            input : visitor_uuid
            output : list of documents read by the visitor"""
        return decorator(self,self.get_also_likes(document_id))
    
    def get_also_likes_sorted_top10(self, document_id, decorator, user_id = None) :
        """ a.  Function that returns all document UUIDs read by a visitor
            input : visitor_uuid
            output : list of documents read by the visitor"""
        return decorator(self,self.get_also_likes(document_id))[0:10]
    
class task5:
    """Class to process task5  """
    def __init__(self, datafile) :
        self.__datafile= datafile
        
        
            
    def also_like_graph(self,document_id, user_id):
        """" Function to generate the digraph of also_likes documents"""
        sample_4 = task4(self.__datafile)
        dict_also_like = sample_4.get_also_likes(document_id, user_id)
        from graphviz import Digraph
        graph = Digraph('G', filename = 'SpyderGraph.gv')
        for k in dict_also_like.keys() :
            if(k == user_id) :
                graph.node(user_id[-4:], style = 'filled', fillcolor = 'red', shape = 'square')
            else :
                graph.node(k[-4:],shape = 'square')
            for edge in task5.edge_dict(self,k,dict_also_like)  :
                graph.edge(edge[0],edge[1], shape = 'square')
        for v in dict_also_like.values() :
            for v_node in v :
                if(v_node == document_id) :
                    graph.node(document_id[-4:], style = 'filled', fillcolor = 'red', shape = 'circle')
                else :
                    graph.node(v_node[-4:],shape = 'circle')
        graph.view()   
        
    def edge_dict(self,key,dict_also_like) :
        return [(key[-4:],v[-4:]) for v in dict_also_like[key]] 

        
        
       
    
        