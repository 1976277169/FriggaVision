#!/usr/bin/env python
#-*- coding:utf-8 -*-
#(C) 2016 chenbingfeng

import os
import sys

def div_data(datapath, people_num, train_fn, test_fn, jbtrain_fn):
        #train_fn  deepID training , test_fn deepID validation , jbtrain_fn joint bayesian training
        ratio = 11 #  0,1 >> jbtrain, 2 >> test fn 3-10 >> train
        dirlists=os.listdir(datapath)
        dict_id_num={}
        for subdir in dirlists:
            dict_id_num[subdir]=len(os.listdir(os.path.join(datapath,subdir)))
        #sorted(dict_id_num.items, key=lambda dict_id_num:dict_id_num[1])
        sorted_num_id=[(v, k) for k, v in dict_id_num.items()]
        select_ids=sorted_num_id[0:people_num]
        
        fid_train=open(train_fn,'w')
        fid_test=open(test_fn,'w')
        fid_jbtrain = open(jbtrain_fn, 'w')
        train_cnt = 0
        test_cnt = 0
        jbtrain_cnt = 0
        
        for pid,  select_id in enumerate(select_ids):
            subdir=select_id[1]
            filenamelist=os.listdir(os.path.join(datapath,subdir)) 

            for num, filename in enumerate(filenamelist):
                mdr = num % ratio
                if mdr < 2:
                    fid_jbtrain.write(os.path.join(subdir,filename)+' '+str(pid)+'\n')
                    jbtrain_cnt = jbtrain_cnt + 1
                elif mdr > 2:
                    fid_train.write(os.path.join(subdir,filename)+' '+str(pid)+'\n')
                    #https://github.com/BVLC/caffe/blob/master/tools/convert_imageset.cpp split with ' ' not \t
                    train_cnt = train_cnt + 1
                else:
                    fid_test.write(os.path.join(subdir,filename)+' '+str(pid)+'\n')
                    test_cnt = test_cnt + 1
        print "total people", len(sorted_num_id), "select-people", people_num, "total", train_cnt+test_cnt+jbtrain_cnt, "train", train_cnt, "test", test_cnt, "jbtrain", jbtrain_cnt


        fid_train.close()
        fid_test.close()   
        fid_jbtrain.close()

if __name__=='__main__':
    if len(sys.argv) == 5:
        # div_data("webface/CASIA-WebFace-total-cropped", 10500, "webface/train_list.txt", "webface/test_list.txt", "webface/jbtrain_list.txt")
        div_data(sys.argv[1], 10500, sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print "USAGE %s webface_image_dir fn_train_list fn_validation_list fn_jbtrain_list"

