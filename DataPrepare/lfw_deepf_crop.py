#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2016 chenbingfeng
#

import os
import sys
import skimage.transform
import skimage.io
import numpy as np


ALIGN_Y_OFF = 0
ALIGN_TARGET = np.array([[93.0, 109.0 + ALIGN_Y_OFF],[157.0, 109.0 + ALIGN_Y_OFF],[125.0, 172.0 + ALIGN_Y_OFF]])
CROP_SCALER = 0.333

def simiTransCrop(img_src, img_des, rect, marks, des_size):
    des_path = os.path.dirname(img_des)
    if not os.path.exists(des_path):
        os.system("mkdir -p '%s'" % des_path )

    ''' two eye centers and the mid-point of the two mouth corners.'''
    right_eye = marks[0]
    left_eye = marks[1]
    mouth_center = [(marks[3][0] + marks[4][0])*0.5, (marks[3][1] + marks[4][1])*0.5]
    global ALIGN_TARGET, CROP_SCALER
    srcarr = np.array([ right_eye, left_eye, mouth_center ])
    tform = skimage.transform.estimate_transform('similarity', ALIGN_TARGET, srcarr)
    # print tform
    img_obj = skimage.io.imread(img_src)
    img_traned = skimage.transform.warp(img_obj, tform)
    img_scaled = skimage.transform.rescale(img_traned, CROP_SCALER)
    img_croped = img_scaled[9:73, 9:73]
    
    skimage.io.imsave(img_des, img_croped)

def main():

    f_result = open('lfw_deepf_list.txt', 'r')
    align_result = f_result.readlines()
    f_result.close()

    print "start cropping ... "
    total = len(align_result)
    curr = 0
    for line in align_result:
        print line[:-1]
        img_obj = skimage.io.imread(line[:-1])
        # img_scaled = skimage.transform.rescale(img_obj, CROP_SCALER)
        HW = 60
        img_croped = img_obj[125-HW:125+HW, 125-HW:125+HW]
        img_des = skimage.transform.resize(img_croped, (64, 64))

        skimage.io.imsave("lfw-deepf-cropped/" + os.path.basename(line[:-1]), img_des)






if __name__ == "__main__":
    main()
