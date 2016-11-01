# cp /home/ikode/caffe-master/examples/deepID/deepID_train_test.prototxt /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_train_test.prototxt
# cp /home/ikode/caffe-master/examples/deepID/deepID_solver.prototxt /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_solver.prototxt
# sed -i -e "9c\    source: \"\/home\/ikode\/caffe-master\/examples\/deepID\/10000\/deepID_10000_train_lmdb\"" /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_train_test.prototxt
# sed -i -e "14c\    mean_file: \"\/home\/ikode\/caffe-master\/examples\/deepID\/10000\/deepID_10000_mean.binaryproto\"" /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_train_test.prototxt
# sed -i -e "26c\    source: \"\/home\/ikode\/caffe-master\/examples\/deepID\/10000\/deepID_10000_test_lmdb\"" /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_train_test.prototxt
# sed -i -e "31c\    mean_file: \"\/home\/ikode\/caffe-master\/examples\/deepID\/10000\/deepID_10000_mean.binaryproto\"" /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_train_test.prototxt
# sed -i -e "1c\net: \"\/home\/ikode\/caffe-master\/examples\/deepID\/10000\/deepID_10000_train_test.prototxt\"" /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_solver.prototxt
# sed -i -e "15c\snapshot_prefix: \"\/home\/ikode\/caffe-master\/examples\/deepID\/10000\/deepID_10000\"" /home/ikode/caffe-master/examples/deepID/10000/deepID_10000_solver.prototxt

echo "Start training..."
caffe_dir="/home/ch3n/caffe"

time $caffe_dir/build/tools/caffe train --solver=./deepID_solver.prototxt  2>&1 |tee ./train.log

echo "DONE"