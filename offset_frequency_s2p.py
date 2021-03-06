# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:50:26 2021

@author: Wei_Wei
"""

import skrf as rf
import numpy as np
import os


path='C:/1_WeiWei/9_execise/picked_100_from_FA1/'
path_save='C:/1_WeiWei/9_execise/picked_100_from_FA1_freqoffset/'


def select_s1p_filename(path,suffix_name): #提取所有.s1p的文件名但不带路径
    allfile=(os.listdir(path))
    namelist=[]
    for name in allfile:  
        if os.path.splitext(name)[1]==suffix_name:
            namelist.append(name)
    return(namelist)

namelist=select_s1p_filename(path,'.s2p')

for name in namelist:
    
    Snn=rf.Network(path+name)
    S=(Snn.s)
    f=Snn.f
    
    data=[]
    for ii in range(len(f)):
        temp=[]
        freq=f[ii]+110000000
        
        Sii=S[ii][0][0]
        Z11=(Sii.real, Sii.imag)
        a=list(Z11)
        
        Sii=S[ii][0][1]
        Z22=(Sii.real, Sii.imag)
        b=list(Z22)
        
        Sii=S[ii][1][0]
        Z21=(Sii.real, Sii.imag)
        c=list(Z21)
        
        Sii=S[ii][1][1]
        Z12=(Sii.real, Sii.imag)
        d=list(Z12)
        
        temp.append(str(freq))
        temp.append(str(a[0]))
        temp.append(str(a[1]))
        temp.append(str(b[0]))
        temp.append(str(b[1]))
        temp.append(str(c[0]))
        temp.append(str(c[1]))
        temp.append(str(d[0]))
        temp.append(str(d[1]))
    
        data.append(temp)
    
      
    addition=[
                "!Keysight Technologies,P9375A,MY56901025,A.14.10.03",\
                "!Date: Tuesday, December 22, 2020 12:03:56",\
                "!Correction: S11(C  2-Port  )",\
                "!S21(C  2-Port  )",\
                "!S12(C  2-Port  )",\
                "!S22(C  2-Port  )",\
                "!S2P File: Measurement: :",\
                "# Hz S  RI   R 50",\
                 ]         
    
    with open(path_save+name,"a") as file:
        for ii in range(len(addition)):
            file.write(addition[ii]+"\n")
                
    with open(path_save+name,"a") as file:
        for ii in range(len(data)):
            c=','.join(data[ii])
            c = c.replace(',', ' ')
            file.write(c+"\n")     
            
            
            
            
 