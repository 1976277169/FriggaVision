for f in ../../test/*.png; do
time ./build/facedet_test model/seeta_fd_frontal_v1.0.bin "$f"  "$f.dt.png"
done