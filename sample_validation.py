# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 01:51:20 2020

@author: Haijie
"""

import shutil, random, os
import glob


data_len = 0

# change the ratio to any number between 0-1, 0.2 is recommended
val_ratio = 0.2

path = "OID/Dataset/train"
desPath = path[:-5]
desPath = desPath+"validation"

if not os.path.isdir(desPath):
    os.mkdir(desPath)

randomlist = []

dir_list = os.listdir(path)
print(dir_list)



for CateDir in dir_list:
    cur_path = path+"/"+CateDir
    print(cur_path)
    des_cur_path = desPath+"/"+CateDir
    print(des_cur_path)
    
    # Make the folders for images and labels
    if not os.path.isdir(des_cur_path):
        os.mkdir(des_cur_path)
    des_cur_path_label = des_cur_path+"/"+"Label"
    if not os.path.isdir(des_cur_path_label):
        os.mkdir(des_cur_path_label)
        
        
    #generate random selections form total dataset
    data_len = len(glob.glob1(cur_path,"*.jpg"))
    if not randomlist:
        randomlist = random.sample(range(data_len), int(data_len*val_ratio))
        randomlist.sort()
    # print(randomlist)
    
    # move the images and txt files
    # images = glob.glob(cur_path+"/"+"*.jpg")
    # labels = glob.glob(cur_path+"/"+"Label"+"*.txt")
    images = glob.glob1(cur_path,"*.jpg")
    labels = glob.glob1(cur_path+"/Label", "*.txt")
    i = 0
    for image, label in zip(images, labels):
        if i in randomlist:
            shutil.move(cur_path+"/"+image, des_cur_path)
            shutil.move(cur_path+"/Label/"+label, des_cur_path_label)
        i = i+1