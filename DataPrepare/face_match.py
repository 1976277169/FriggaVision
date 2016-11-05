#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2016 chenbingfeng
#

import os
import sys
import math

'''
washed_webface_align_result 是在原始的webface的align的结果上，通过face_wash，根据align marks去除profile view之后的条目。
我们用face_align_save.py直接在原来webface的align_result的基础上，对webface进行了归一化保存成了图片。
然后再用face_align 形成了webface_aligned_align_result。而实际上再align_result上就应该进行wash了。本脚本就是去删除webface_aligned_align_result中本该被wash的内容。

'''

def main():
    cnt_deleted = 0
    with open("washed_webface_align_result.txt", 'r') as f_origin:
        with open("webface_aligned_align_result.txt", 'r') as f_content:
            with open("matched_webface_aligned_align_result.txt", 'w') as f_out:
                origins = f_origin.readlines()
                tdict = {}
                for l in origins:
                    ww =  l.split(' ')
                    if len(ww) > 2:
                        ffn = ww[0][-15:]
                        tdict[ffn] = 1
                
                contents = f_content.readlines()
                for l in contents:
                    ww = l.split(' ')
                    if len(ww) > 2:
                        ffn = ww[0][-15:]
                        if tdict.has_key(ffn):
                            f_out.write(l)
                        else:
                            cnt_deleted = cnt_deleted + 1
    print len(origins), len(tdict), len(contents), "deleted ", cnt_deleted
    print "DONE"

if __name__ == "__main__":
    main()
