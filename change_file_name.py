# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:22:23 2020

@author: Wei_Wei
"""
import os ,os.path 

def select_s1p_filename(path,suffix_name): #提取所有.s1p的文件名但不带路径
    allfile=(os.listdir(path))  
    s1pnamelist=[]
    for name in allfile:  
        if os.path.splitext(name)[1]==suffix_name:
            s1pnamelist.append(name)
    return(s1pnamelist)


path='C:/20200827_Athena1/Before trimming/WF_18/1_Raw_data_filters/'
      
namelist=select_s1p_filename(path,'.s2p')

for name in namelist:

    
    
    new_name = name.replace('HL1','Athena1')
    
    os.renames(path+name,path+new_name)
    
    print(new_name)