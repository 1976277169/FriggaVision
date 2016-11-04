#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Create on Tues 2015-11-24

@author: hqli
'''

#运行前,先将pycaffe安装好
#运行时在caffe主目录（一般为～/caffe-master）下执行python DeepIDTest.py

import os
import sys

print "start wash..."

f_in = open("lfw-deepf-selfalign-result.txt", 'r')
lines = f_in.readlines()
f_in.close()

image_name_dict = {}

for l in lines:
    ww = l.split(' ')
    if len(ww) > 1:
        fn = os.path.basename(ww[0])
        image_name_dict[fn] = 1


def get_file_list(fn):
    f = open(fn, 'r')
    ret = []
    for l in f.readlines():
        ww = l.split('\n')
        if len(ww) > 0:
            t = ww[0]
            ret.append(t)
    f.close()
    return ret

lefts = get_file_list("lfw-deepf-alignc/left.txt")
rights = get_file_list("lfw-deepf-alignc/right.txt")
labels = get_file_list("lfw-deepf-alignc/label.txt")

lefts_ret = []
rights_ret = []
labels_ret = []

num = len(lefts)
cnt_washed = 0
cnt_remain = 0
for i in xrange(num):
    lfn = os.path.basename(lefts[i])
    rfn = os.path.basename(rights[i])

    if image_name_dict.has_key(lfn) and image_name_dict.has_key(rfn):
        lefts_ret.append(lefts[i])
        rights_ret.append(rights[i])
        labels_ret.append(labels[i])
        cnt_remain = cnt_remain + 1
    else:
        cnt_washed = cnt_washed + 1
        print "wash", lfn, rfn

print "washed", cnt_washed, "remain", cnt_remain
def set_file_list(fn ,li):
    with open(fn, 'w') as f:
        for l in li:
            f.write(l + "\n")

set_file_list("lfw-deepf-alignc/left.txt", lefts_ret)
set_file_list("lfw-deepf-alignc/right.txt", rights_ret)
set_file_list("lfw-deepf-alignc/label.txt", labels_ret)

print "DONE"



