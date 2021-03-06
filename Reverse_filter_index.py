# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:32:37 2019

@author: Luke_Chang

#把通过csv筛选的测试点，从所有测试结果中找出来，并把s1p文件复制到制定路径。
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


   
def reverse_csv(data_raw):
    
    data_raw['Row_new']=-data_raw['Column']
    data_raw['Col_new']=data_raw['Row']
    
    data_raw.drop(columns=['Row','Column'],axis=1,inplace=True)
    
    data_raw.rename(columns={'Row_new':'Row'},inplace=True)
    data_raw.rename(columns={'Col_new':'Column'},inplace=True)
    
    return data_raw


def get_foldersname(path):
    foder_list=os.listdir(path)
    return foder_list



path='C:/1_WeiWei/8_Package_level_pick_map/HeraLow2.0_SST_MappingFile/1/'
'''
folders=get_foldersname(path)

for name in folders:
    check='.' in name
    
    if check== False:
        path_temp=path+name+'/'
        csvs=select_s1p_filename(path_temp,'.csv')
        
        for ii in range(len(csvs)):
            raw_index=pd.read_csv(path_temp+csvs[ii])
            rev_data=reverse_csv(raw_index)
            rev_data.to_csv(path+'Reverse_'+csvs[ii],index=False)


'''
csvs=select_s1p_filename(path,'.csv')

for ii in range(len(csvs)):
    raw_index=pd.read_csv(path+csvs[ii])
    rev_data=reverse_csv(raw_index)
    #rev_data.to_csv(path+'Reverse_'+WF+'_'+csvs[ii],index=False)
    rev_data.to_csv(path+'Reverse_'+csvs[ii],index=False)





