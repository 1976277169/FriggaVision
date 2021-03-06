# FriggaVision
Our face identification develop toolkit.

##Intro
###FaceDetection 
Which is from [SeetaFace](https://github.com/seetaface/SeetaFaceEngine) mainly. We add feature of angle selection, which can help us wash the train data, e.g., rejecting all face > 45 degree. But the model provided by SeetaFace has different structure from which they have descriped in the FuSt paper. So the angle selection can not work, because there are only 3 LAB cascaded unit there. What a pity. We need to build an cascaded Face Detection tool  with more accurate performance in profile view situation later.

###FaceAlignment

Which is from SeetaFace too. We fix some build errors under macOS and ubuntu 1604. And add some webface sample image for testing. The model is working, but bad in difficult situation. When time is on our side, we will find an accurate Alignment tool even with bad speed performance(e.g, CNN based), because we use it at data preprocessing not in real-time applicaton.

###DataPrepare
Here contains some tools  to preprocess image data for training of DeepID using above staff. The main target is [Webface dataset](http://www.cbsr.ia.ac.cn/english/CASIA-WebFace-Database.html). The dataset has 5% super profile view image, which is bad for training an network to fetch feature out of mainly frontal faces. For that, we take a wash step there.

###FaceIdentification
Finlly the simple caffe [DeepId(1st gen)](http://mmlab.ie.cuhk.edu.hk/pdf/YiSun_CVPR14.pdf) code. The network is somehow outdated(still use LRN), but it should works. Fresh meat is welcome!

##Build Guide
Follow DataPrepare/readme.md

##Results
###test1
Network and solver is at FaceIdentification/test1/.Only one pitch and one network is used, the pitch is generally cover the total face. 

We use 10000people, and SGD optimization with 500k interation, the training validation accuracy is at 65.5%, which is the same as the paper told.

Use lfwcrop_color, cosine distance. The result ROC is below, it's bad but working.

<img src="FaceIdentification/test1_roc_crop_lfw_cosine.png" width="300" />

###test2
In test1, the testing dataset's face image only contain the face, not as our training cropping, which has a more margin. In test2, we use the [lfw-deepfunneled.tgz](http://vis-www.cs.umass.edu/lfw/lfw-deepfunneled.tgz) dataset, and crop by ourself with DataPrepare's lfw_deepf_crop.py. We got a better ROC.

accr = 0.78

<img src="FaceIdentification/test2_roc_deepf_selfcrop_cosine.png" width="300" />

When using Joint Bayesian, the result is worse...

accr = 0.74

<img src="FaceIdentification/test2_jb_roc.png" width="300" />

In paper, the No.patch == 1, accr will got 89%.

When apply LFW with the same align-crop routine as we did to the webface training data:

With cosine accr =  0.837065508021

<img src="FaceIdentification/test2_3_with_webface_aligncrop_cosine_roc.png" width="300" />

With jb accr = 0.795788770053

<img src="FaceIdentification/test2_3_jb_roc.png" width="300" />

###test3
TODO
N pitch + Joint Bayesian >> 
hope 90%+


##LISCENSE

MIT
