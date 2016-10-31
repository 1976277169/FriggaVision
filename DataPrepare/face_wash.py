#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2016 chenbingfeng
#

import os
import sys
import math


EYE_DISTANCE_MIN = 45.0
MOUTH_LENGTH_MIN = 25.0
EYE_MOUTH_LEN_MIN = 50.0

def dist(pa, pb):
    dx,dy = (pa[0] - pb[0]), (pa[1] - pb[1])
    return math.sqrt(dx*dx + dy*dy)

def mid(pa, pb):
    return [0.5*(pa[0] + pb[0]), 0.5*(pa[1] + pb[1])]


def isValidView(marks):

    return dist(marks[0], marks[1]) > EYE_DISTANCE_MIN and \
        dist(marks[3], marks[4]) > MOUTH_LENGTH_MIN and \
        dist(mid(marks[0], marks[1]), mid(marks[3], marks[4])) > EYE_MOUTH_LEN_MIN

    return dis < EYE_DISTANC_THRESHOLD

def main():

    f_result = open('align_result.txt', 'r')
    align_result = f_result.readlines()
    f_result.close()

    print "start washing ... "
    total = len(align_result)
    curr = 0
    cwash = 0

    f_washed = open('be_washed_images.txt', 'w')
    f_survivaled = open('washed_align_result.txt', 'w')

    for line in align_result:
        ww = line.split(' ')
        curr = curr + 1
        if len(ww) > 1:
            marks = [[float(ww[5]),float(ww[6])], \
                     [float(ww[7]),float(ww[8])], \
                     [float(ww[9]),float(ww[10])], \
                     [float(ww[11]),float(ww[12])], \
                     [float(ww[13]),float(ww[14])] ]
            if isValidView(marks):
                f_survivaled.write(line)
            else:
                f_washed.write(line )
                cwash = cwash + 1
        
        if curr % 7 == 0:
            sys.stdout.write("\rwashing(%d/%d/%d)  %f" % (cwash, curr, total,  curr * 1.0 / total))
            sys.stdout.flush()

    f_washed.close()
    f_survivaled.close()


if __name__ == "__main__":
    main()
