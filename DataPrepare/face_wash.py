#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2016 chenbingfeng
#

import os
import sys
import math


EYE_DISTANC_THRESHOLD = 45.0

def isProfileView(marks):
    global EYE_DISTANC_THRESHOLD
    le, re  = marks[0], marks[1]

    dx,dy = (le[0] - re[0]), (le[1] - re[1])
    dis = math.sqrt(dx*dx + dy*dy)
    return dis < EYE_DISTANC_THRESHOLD

def main():

    f_result = open('align_result.txt', 'r')
    align_result = f_result.readlines()
    f_result.close()

    print "starting wash ... "
    total = len(align_result)
    curr = 0

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
            if isProfileView(marks):
                f_washed.write(line)
            else:
                f_survivaled.write(line )
        
        if curr % 7 == 0:
            sys.stdout.write("\rwashing(%d/%d) %f" % (curr, total, curr * 1.0 / total))
            sys.stdout.flush()

    f_washed.close()
    f_survivaled.close()


if __name__ == "__main__":
    main()
