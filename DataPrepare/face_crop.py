#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2016 chenbingfeng
#

import os
import sys
import skimage.transform
import skimage.io
# from skimage import transform as tf
import numpy as np


#use webface-tiny/6549862/016.jpg as target
#94.3201 109.413 157.943 109.31 125.96 146.295 94.5787 172.477 153.157 172.157
ALIGN_Y_OFF = 0
ALIGN_TARGET = np.array([[93.0, 109.0 + ALIGN_Y_OFF],[157.0, 109.0 + ALIGN_Y_OFF],[125.0, 172.0 + ALIGN_Y_OFF]])
# ALIGN_TARGET = np.array([[94, 158, 124],[109, 109, 172]])
CROP_SCALER = 1.0

def simiTransCrop(img_src, img_des, rect, marks, des_size):
    print img_src
    des_path = os.path.dirname(img_des)
    if not os.path.exists(des_path):
        os.system("mkdir -p '%s'" % des_path )

    ''' two eye centers and the mid-point of the two mouth corners.'''
    right_eye = marks[0]
    left_eye = marks[1]
    mouth_center = [(marks[3][0] + marks[4][0])*0.5, (marks[3][1] + marks[4][1])*0.5]
    global ALIGN_TARGET, CROP_SCALER
    print marks
    srcarr = np.array([ right_eye, left_eye, mouth_center ])
    # srcarr = np.array([ [right_eye[0], left_eye[0], mouth_center[0] ],  \
                        #  [right_eye[1], left_eye[1], mouth_center[1] ] ])
    print srcarr, ALIGN_TARGET
    # trans = cv2.estimateRigidTransform(srcarr, ALIGN_TARGET, False)
    tform = skimage.transform.estimate_transform('similarity', ALIGN_TARGET, srcarr)
    print tform
    img_obj = skimage.io.imread(img_src)
    img_traned = skimage.transform.warp(img_obj, tform)
    img_scaled = skimage.transform.rescale(img_traned, CROP_SCALER)
    img_croped = img_scaled[37:213, 37:213]
    
    skimage.io.imsave(img_des, img_croped)

def main():

    f_result = open('align_result.txt', 'r')
    align_result = f_result.readlines()
    f_result.close()

    dir_prefix = "cropped"
    os.system("rm -rf '%s'" % dir_prefix)
    os.mkdir(dir_prefix)
    print "starting croping ... "
    total = len(align_result)
    curr = 0
    for line in align_result:
        ww = line.split(' ')
        curr = curr + 1
        if len(ww) > 1:
            img_src = ww[0]
            img_des = dir_prefix + "/" + img_src
            rect = (int(ww[1]), int(ww[2]),int(ww[3]),int(ww[4]))
            marks = [[float(ww[5]),float(ww[6])], \
                     [float(ww[7]),float(ww[8])], \
                     [float(ww[9]),float(ww[10])], \
                     [float(ww[11]),float(ww[12])], \
                     [float(ww[13]),float(ww[14])] ]
            des_size = (64,64)
            simiTransCrop(img_src, img_des, rect, marks, des_size)
        if curr % 7 == 0:
            sys.stdout.write("\rcropping(%d/%d) %f" % (curr, total, curr * 1.0 / total))
            sys.stdout.flush()




if __name__ == "__main__":
    main()
