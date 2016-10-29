mkdir $1
for f in testimages/*; do
fn=$(basename "$f")
time ./build/facedet_test model/seeta_fd_frontal_v1.0.bin "$f"  "$1/$fn"
done