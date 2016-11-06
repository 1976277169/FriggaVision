#(c) 2016 chenbingfeng
for scale in {0..2}
do 
    for pos in {0..5}
    do
        patch_dir="s${scale}p$pos"
        echo ">>>>>>>>>>>>>>>>>>$patch_dir"

        data_dir="webface_multi_cropped/$patch_dir/webface_aligned/CASIA-WebFace-total"
        output_base="webface_multi_cropped/$patch_dir"
        fn_train="$output_base/train_list.txt"
        fn_validation="$output_base/validation_list.txt"
        fn_jbtrain="$output_base/jbtrain_list.txt"

        ./dataset_div.py "$data_dir" "$fn_train" "$fn_validation" "$fn_jbtrain"
        ./gen_lmdb_imgmean.sh "$output_base" "$data_dir/"
    done
done
