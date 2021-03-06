# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:43:54 2020

@author: Administrator
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
    print(foder_list)
    return foder_list

def path_convert(path):
    path_temp=path+'\\'
    path_new=path_temp.replace('\\','/')
    return path_new


class File_operate():
    def __init__ (self,):
        print('csv-snp and so on...')
        
    def csv_folders_to_folder(self,path):
        self.path=path
        self.folders=get_foldersname(self.path)
        
        for folder in self.folders:
            path_temp=self.path+folder+'/'
            csv_name=select_s1p_filename(path_temp,'.csv')
            print(''.join(csv_name))
            crr=pd.read_csv(path_temp+''.join(csv_name))
            crr.to_csv(self.path+''.join(csv_name),index=False,header=True)  #第一次的数据带列名

    def csv_in1folder_combine(self,path,save_name):
        self.path=path
        self.save_name=save_name
        self.csv_name=select_s1p_filename(path,'.csv')
        
        for ii in range(len(self.csv_name)):
            crr=pd.read_csv(self.path+self.csv_name[ii])
            print(len(crr))
            if ii==0:
                crr.to_csv(self.path+self.save_name,index=False,header=True)  #第一次的数据带列名
            else:
                crr.to_csv(self.path+self.save_name,mode='a',index=False,header=False)#后面的数据不带列名        
        
    def del_files_in_folders(self,path,suffix):
        self.path=path
        self.suffix=suffix
        
        f_list= get_foldersname(self.path)
        for name in f_list:
            path_temp=self.path+name+'/'
            csv_list=select_s1p_filename(path_temp,self.suffix)
            
            for ii in range(len(csv_list)):
                print(name)
                os.remove(path_temp+csv_list[ii])       
                
    def del_file(self,path,name):
        self.path=path
        self.name=name
        os.remove(self.path+self.name)       
                
    def copy_snp_by_filename(self,filename,path_save):
        pass

#添加方法，根据csv的行列索引来复制文件。

if __name__ in "__main__":
    
    #copy csvs in diff folders to 1 folder.
    path=path_convert('F:\HeraLow1_batch2\\batch1 vs batch2\\batch1')
    o=File_operate()
    #o.csv_folders_to_folder(path)
    
    #combine csvs in 
    #path=path_convert('F:\HeraHigh2\Batch3')
    #o=File_operate()
    o.csv_in1folder_combine(path,'batch1_AFilters.csv')
    #o.del_files_in_folders(path,'.csv')
    #o.del_file(path,'BD1AEL.csv')

       
        