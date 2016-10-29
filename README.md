# FriggaVision
Our face identification develop toolkit.

FaceDetection is from SeetaFace mainly. We add feature of angle selection, which can help us wash the train data, e.g., rejecting all face > 45 degree. But the model provided by SeetaFace has different structure from which they have descriped in the FuSt paper. So the angle selection can not work, because there are only 3 LAB cascaded unit here. What a pity. So we have a TODO to build our own Detection system.

FaceAlignment is from SeetaFace too. We fix some build errors under macOS, and add some webface sample image for testing. The model is working, but not working well in difficult situation. One TODO is to find more accurate Alignment tool even taking more time, for we use it as data preprocessing not real-time applicaton.

The target:
We use FaceDetection/FaceAlignment to preprocess image data for training of DeepID.