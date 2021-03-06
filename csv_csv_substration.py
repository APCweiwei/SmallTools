# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:49:46 2020

@author: Wei_Wei
"""

import os
import pandas as pd


def select_s1p_filename(path_only,suffix_name): #提取所有.s1p的文件名但不带路径
    allfile=(os.listdir(path_only))  
    s1pnamelist=[]
    for name in allfile:  
        if os.path.splitext(name)[1]==suffix_name:
            s1pnamelist.append(name)
    return(s1pnamelist)


def get_foldersname(path):
    foder_list=os.listdir(path)
    return foder_list


path='C:/1_WeiWei/9_execise/'
csv1='CBAW2B_300pitch_Filter_R0_R67000.csv'
csv2='Random5per_CBAW2B_300pitch_Filter_R0_R67000.csv'

df1=pd.read_csv(path+csv1)
df2=pd.read_csv(path+csv2)

df3 = df1.append(df2).drop_duplicates(keep=False)
df3.to_csv(path+'Delta_.csv')





