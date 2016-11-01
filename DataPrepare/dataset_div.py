#!/usr/bin/env python
#-*- coding:utf-8 -*-
#(C) 2016 chenbingfeng


def div_data(datapath, people_num, train_fn, test_fn):
        ratio = 9 # 1/9 as test
        dirlists=os.listdir(datapath)
        dict_id_num={}
        for subdir in dirlists:
            dict_id_num[subdir]=len(os.listdir(os.path.join(datapath,subdir)))
        #sorted(dict_id_num.items, key=lambda dict_id_num:dict_id_num[1])
        sorted_num_id=sorted([(v, k) for k, v in dict_id_num.items()], reverse=True)
        select_ids=sorted_num_id[0:self.num]
        
        fid_train=open(train_fn,'w')
        fid_test=open(test_fn,'w')
        
        pid=0
        for  select_id in select_ids:
            subdir=select_id[1]
            filenamelist=os.listdir(os.path.join(datapath,subdir)) 
            num=1
            for filename in filenamelist :
                #print select_ids[top_num-1]
                if num>select_ids[self.num-1][0]:
                    break
                if num%ratio!=0:
                    fid_train.write(os.path.join(subdir,filename)+'\t'+str(pid)+'\n')
                else:
                    fid_test.write(os.path.join(subdir,filename)+'\t'+str(pid)+'\n')
                num=num+1
            pid=pid+1

        fid_train.close()
        fid_test.close()   

if __name__=='__main__':

    div_data("webface/CASIA-WebFace-total-cropped", 8000, "webface/train_list.txt", "webface/test_list.txt")

