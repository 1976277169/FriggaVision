#(c) 2016 chenbingfeng
target_dir=webface-tiny
echo "generate image list"
find "$target_dir" -name "*.jpg" > image_list.txt

../FaceAlignment/build/fa_test ../FaceDetection/model/seeta_fd_frontal_v1.0.bin \
 ../FaceAlignment/model/seeta_fa_v1.1.bin image_list.txt align_result.txt
