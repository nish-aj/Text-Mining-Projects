# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 22:07:52 2018

@author: Nishna
"""
import sys as s
import getopt
import module_2 as m2
import module_3 as m3
import module_4 as m4

def main(argv) :
    user_id = None
    document_id = None
    datafile = None
    task_id = 0    
    try :
        options, arguments = getopt.getopt(s.argv[1:], "v:d:t:h:f", ["user_id=", "document_id=", "task_id=", "help=", "datafile = "])
    except s.getopt.GetoptError as err:
        print(err)
        s.exit(2)
    
    for o,a in options:
        if o == '-h':
            print('Please follow the format below for CLI')
            print('cw2 -u user_uuid -d doc_uuid -t task_id -f file_name')
            print('2.Views by Geo')
            print('3.Views by Browsers')
            print('4a.Readers List')
            print('4c.Also Like')
            s.exit(2)
        elif o == '-v' :
            user_id = a
        elif o == '-d' :
            document_id = a
        elif o == '-t' :
            task_id = a
        elif o == '-f' :
            datafile = a
            
        else :
            print("Invalid Command Format")
        if task_id == '2a':
            if document_id is None:
                print('Please enter the document id')
            else :
                sample_2a = m2.task2a(document_id,datafile)
                sample_2a.view_by_country()
                

main(s.argv[1:])
                
            
            
            
            
