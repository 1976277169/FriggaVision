#(c) 2016 chenbingfeng
if [ $# -ne 1 ]; then
echo "USAGE $0 be_aligned_dir"
exit
fi
target_dir="$1"
echo "generate image list"
find "$target_dir" -name "*.jpg" > "$1"_image_list.txt

../FaceAlignment/build/fa_test ../FaceDetection/model/seeta_fd_frontal_v1.0.bin \
 ../FaceAlignment/model/seeta_fa_v1.1.bin "$1"_image_list.txt "$1"_align_result.txt
