# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 02:04:31 2018

@author: Nishna
"""

#GUI
import module_2 as m2
import module_3 as m3
import module_4 as m4
import module_6 as m6
import pandas as pd

df = pd.read_json('C:/Users/Nishna/Desktop/F21SC_Python/CW/Datasets/test/issuu_sample.json', lines = True, orient='columns')

sample_2a = m2.task2a('131203154832-9b8594b7ec211f7e1a0782fd9883b42c',df)
sample_2a.view_by_country()

sample_2b = m2.task2b('131203154832-9b8594b7ec211f7e1a0782fd9883b42c',df)
sample_2b.view_by_continent()

sample_3a = m3.task3a(df)
sample_3a.view_by_user_agent() 
sample_3b = m3.task3b(df)
sample_3b.view_by_browser()

sample_4 = m4.task4(df)
print("Generate readers list for the document")
print(sample_4.get_readers('131203154832-9b8594b7ec211f7e1a0782fd9883a42c'))
print("\nGenerate reading list for the readers")
print(sample_4.get_read_documents('9a83c97f415601a6'))
print("\nGenerate also_like list for the document")
print((sample_4.get_also_likes('131203154832-9b8594b7ec211f7e1a0782fd9883a42c')))


print("\nGenerate also_like top 10 list sorted based on number of readers for the document")
x = sample_4.get_also_likes_sorted_top10('131203154832-9b8594b7ec211f7e1a0782fd9883a42c', m4.task4.sort_no_of_readers)
print(x)
#print(sample_4.sort_no_of_readers(x))


sample_6 = m6.task6()




sample_5 = m4.task5(df)
sample_5.also_like_graph('131203154832-9b8594b7ec211f7e1a0782fd9883a42c','9a83c97f415601a6')
