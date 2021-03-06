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


path='C:/20200827_Athena1/Before trimming/Resonator/WF_05/2/WF_05/'
      
namelist=select_s1p_filename(path,'.s1p')

for name in namelist:

    portion = os.path.splitext(name)#将文件名拆成名字和后缀

    newname = portion[0] + ".s2p"

    os.rename(path+name, path+newname)#修改