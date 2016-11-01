#!/usr/bin/env python
#-*- coding:utf-8 -*-
#(C) 2016 chenbingfeng

import os

def div_data(datapath, people_num, train_fn, test_fn):
        ratio = 9 # 1/9 as test
        dirlists=os.listdir(datapath)
        dict_id_num={}
        for subdir in dirlists:
            dict_id_num[subdir]=len(os.listdir(os.path.join(datapath,subdir)))
        #sorted(dict_id_num.items, key=lambda dict_id_num:dict_id_num[1])
        sorted_num_id=[(v, k) for k, v in dict_id_num.items()]
        select_ids=sorted_num_id[0:people_num]
        
        fid_train=open(train_fn,'w')
        fid_test=open(test_fn,'w')
        train_cnt = 0
        test_cnt = 0
        
        for pid,  select_id in enumerate(select_ids):
            subdir=select_id[1]
            filenamelist=os.listdir(os.path.join(datapath,subdir)) 

            for num, filename in enumerate(filenamelist):
                if num%ratio!=0:
                    fid_train.write(os.path.join(subdir,filename)+'\t'+str(pid)+'\n')
                    train_cnt = train_cnt + 1
                else:
                    fid_test.write(os.path.join(subdir,filename)+'\t'+str(pid)+'\n')
                    test_cnt = test_cnt + 1
        print "total people", len(sorted_num_id), "select-people", people_num, "total-image", train_cnt+test_cnt, "train-image", train_cnt, "test-image", test_cnt 


        fid_train.close()
        fid_test.close()   

if __name__=='__main__':

    div_data("webface/CASIA-WebFace-total-cropped", 10000, "webface/train_list.txt", "webface/test_list.txt")

