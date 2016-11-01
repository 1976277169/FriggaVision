# rm -rf /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_train_lmdb
# rm -rf /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_train_lmdb
rm -rf ./webface/train_lmdb
rm -rf ./webface/test_lmdb

# mkdir ./webface/train_lmdb
# mkdir ./webface/test_lmdb


caffe_dir="/home/ch3n/caffe"
echo "Creating train lmdb..."
$caffe_dir/build/tools/convert_imageset --resize_height=64 --resize_width=64 --shuffle --backend="lmdb" ./webface/CASIA-WebFace-total-cropped/ ./webface/train_list.txt ./webface/train_lmdb 2>&1 |tee ./webface/create_train_lmdb.log 
# /media/ikode/Document/big_materials/document/deep_learning/caffe/face_datasets/webface/croped/ /home/ikode/caffe-master/examples/deepID/10000/deepID_train_10000.txt /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_train_lmdb 2>&1 |tee /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_create.log

# /home/ikode/caffe-master/build/tools/convert_imageset --resize_height=64 --resize_width=64 --shuffle --backend="lmdb" /media/ikode/Document/big_materials/document/deep_learning/caffe/face_datasets/webface/croped/ /home/ikode/caffe-master/examples/deepID/10000/deepID_train_10000.txt /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_train_lmdb 2>&1 |tee /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_create.log
echo "Creating test lmdb..."
$caffe_dir/build/tools/convert_imageset --resize_height=64 --resize_width=64 --shuffle --backend="lmdb" ./webface/CASIA-WebFace-total-cropped/ ./webface/test_list.txt ./webface/test_lmdb 2>&1 |tee ./webface/create_test_lmdb.log 

# /home/ikode/caffe-master/build/tools/convert_imageset --resize_height=64 --resize_width=64 --shuffle --backend="lmdb" /media/ikode/Document/big_materials/document/deep_learning/caffe/face_datasets/webface/croped/ /home/ikode/caffe-master/examples/deepID/10000/deepID_val_10000.txt /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_test_lmdb 2>&1 |tee -a /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_create.log
echo "Done"