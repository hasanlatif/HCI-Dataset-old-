# -*- coding: utf-8 -*-
# Created by: 
#Author :Hasan Latif
#Email :hasanlatif.pk@gmail.com
# WARNING! All changes made in this file will be lost!
# for using this code you need opencv,h5py.
# for installing just use the pip



import cv2
import numpy as np
import h5py
import time

path='blender/stillLife/lf.h5'
def read_dataset(path, flag):
    print("[Info]>>Starts at",time.ctime())
    hf = h5py.File(path, 'r')
    if(flag=='LF'):
        get_flag = hf.get('LF')
        np_array=np.array(get_flag)
        for row in range(0, 9):
            for col in range(0, 9):
                n1 = np_array[:, :, :][:, :, :][row][col]
                n1=cv2.cvtColor(n1,cv2.COLOR_RGB2BGR)
                print("[info]>> Writing stillLife-{}-{} .jpg".format(str(row), str(col)))
                cv2.imwrite('blender/stillLife/jpgs/papillon-'+str(row)+'-'+str(col)+'.jpg',n1)

        print("[Info]>>Ends at", time.ctime())




if __name__ == '__main__':

    read_dataset(path,'LF')


