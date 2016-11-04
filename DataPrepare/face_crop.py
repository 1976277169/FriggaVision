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

def affineTrans(img_src, img_des, rect, marks):
    des_path = os.path.dirname(img_des)
    if not os.path.exists(des_path):
        os.system("mkdir -p '%s'" % des_path )

    ''' two eye centers and the mid-point of the two mouth corners.'''
    right_eye = marks[0]
    left_eye = marks[1]
    mouth_center = [(marks[3][0] + marks[4][0])*0.5, (marks[3][1] + marks[4][1])*0.5]
    global ALIGN_TARGET, CROP_SCALER
    srcarr = np.array([ right_eye, left_eye, mouth_center ])
    tform = skimage.transform.estimate_transform('affine', ALIGN_TARGET, srcarr)
    # print tform
    img_obj = skimage.io.imread(img_src)
    img_traned = skimage.transform.warp(img_obj, tform)
    # img_scaled = skimage.transform.rescale(img_traned, CROP_SCALER)
    # img_croped = img_scaled[9:73, 9:73]
    skimage.io.imsave(img_des, img_traned)

def align_crop():
    #depreted

    f_result = open('align_result.txt', 'r')
    align_result = f_result.readlines()
    f_result.close()

    dir_prefix = "cropped"
    os.system("rm -rf '%s'" % dir_prefix)
    os.mkdir(dir_prefix)
    print "start cropping ... "
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


def align_save():
    '''产生最初的aligned的图片，为后来的切分做准备'''
    f_result = open('washed_align_result.txt', 'r')
    align_result = f_result.readlines()
    f_result.close()

    dir_prefix = "aligned"
    os.system("rm -rf '%s'" % dir_prefix)
    os.mkdir(dir_prefix)
    print "start cropping ... "
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
            affineTrans(img_src, img_des, rect, marks)
        if curr % 7 == 0:
            sys.stdout.write("\rcropping(%d/%d) %f" % (curr, total, curr * 1.0 / total))
            sys.stdout.flush()


if __name__ == "__main__":
    align_crop()
