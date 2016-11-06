
#(c) 2016 chenbingfeng

echo "stat webface multi train..."
caffe_dir="/home/ch3n/caffe"

for scale in {0..2}
do 
    for pos in {0..5}
    do
        patch_name="s${scale}p$pos"
        echo "Start training...$patch_name"

        #generate network and solver file
        ./webface_gen_net.py "$patch_name"

        #caffe train
        time $caffe_dir/build/tools/caffe train --solver=./webface_solver_$patch_name.prototxt  2>&1 |tee ./webface_${patch_name}_train.log

        echo "$patch_name...DONE"
    done
done

echo "ALL DONE"