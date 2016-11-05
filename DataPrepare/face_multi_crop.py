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

'''
face_multi_crop  根据align_result结果，对face进行多片切分。
每一个切片都是方的，width根据alignment的眼间距离归一，同时有多个scale。

每个片的中心，鼻尖，左眼，右眼，左嘴角，右嘴角，眼中间，嘴中心。7个(p0-p6)
scale s0-s2
3 x 7 = 21
'''

ALIGN_Y_OFF = 0
ALIGN_TARGET = np.array([[93.0, 109.0 + ALIGN_Y_OFF],[157.0, 109.0 + ALIGN_Y_OFF],[125.0, 172.0 + ALIGN_Y_OFF]])
CROP_SCALER = 0.333

import math
def distance(pa, pb):
    dx = pa[0] - pb[0]
    dy = pa[1] - pb[1]
    return math.sqrt(dx*dx + dy*dy)

def center(pa, pb):
    return ((pa[0] + pb[0])/2.0, (pa[1] + pb[1])/2.0)

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

def ir(f):
    return int(round(f))

def crop(img_src, img_des, position, width):
    des_path = os.path.dirname(img_des)
    if not os.path.exists(des_path):
        os.system("mkdir -p '%s'" % des_path )

    hw = width / 2.0
    img_obj = skimage.io.imread(img_src)
    y0, y1, x0, x1 = ir(position[1]-hw), ir(position[1]+hw), ir(position[0]-hw), ir(position[0]+hw)
    if x0 < 0 or y0 < 0:
        print "minus0"
    if x1 >249 or y1 > 249:
        print "bigger249", img_des
    img_crop = img_obj[y0:y1, x0:x1]# 注意网上很多都把x放在前面，实际是错的
    skimage.io.imsave(img_des, img_crop)


SCALEs = [0.7, 1.1, 1.8]

def face_multi_crop(align_result_fn, result_dir):

    f_result = open(align_result_fn, 'r')
    align_result = f_result.readlines()
    f_result.close()

    dir_prefix = result_dir
    os.system("rm -rf '%s'" % dir_prefix)
    os.mkdir(dir_prefix)

    print "start face_multi_crop ... "
    total = len(align_result)
    curr = 0
    for line in align_result:
        ww = line.split(' ')
        curr = curr + 1
        if len(ww) > 1:
            img_src = ww[0]
            # img_des = dir_prefix + "/" + img_src
            rect = (int(ww[1]), int(ww[2]),int(ww[3]),int(ww[4]))
            marks = [[float(ww[5]),float(ww[6])], \
                     [float(ww[7]),float(ww[8])], \
                     [float(ww[9]),float(ww[10])], \
                     [float(ww[11]),float(ww[12])], \
                     [float(ww[13]),float(ww[14])] ]
            marks.append(center(marks[0], marks[1])) #eye center
            marks.append(center(marks[3], marks[4])) #mouth center


            uniform_width = (distance(marks[0], marks[1]) + distance(marks[0], marks[4]) + distance(marks[1], marks[3])) / 3.0
            widths = [uniform_width * s for s in SCALEs]

            for scaleId, width in enumerate(widths):
                for posId, position in enumerate(marks):
                    img_des = dir_prefix + "/" + ("s%dp%d"%(scaleId, posId)) + "/" + img_src
                    crop(img_src, img_des, position, width)
            
        if curr % 7 == 0:
            sys.stdout.write("\rcropping(%d/%d) %f" % (curr, total, curr * 1.0 / total))
            sys.stdout.flush()


if __name__ == "__main__":
    if len(sys.argv) == 3:
        face_multi_crop(sys.argv[1], sys.argv[2])
    else:
        print "USAGE %s align_result_fn, result_dir" % sys.argv[0]
    
