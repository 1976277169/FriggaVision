##DataPrepare

Scripts to prepare face data for CNN training.

###Steps:

- 1) build ../FaceAlignment;
- 2) put webface dataset at ./webface;
- 3) run face_align.sh to generate align_result.txt(will take several hours);
- 4) run face_wash.py to remove face profile with align_result.txt, and the results lay in washed_align_result.txt;
- 5) run face_crop.py to generate cropped dataset;
- 6) go to train ../FaceIdentification;

###Result:

![origin](_res/020-origin.jpg) ==>
![after](_res/020-cropped.jpg)(64x64)

![washed](_res/014-washed.jpg) <== profile view will be  washed away

###Liscense
MIT