# samples example
# the [image] sections indicate the network inputs
# format should be gray images with any bit depth.
#
# [image1]
# fnames =  path/of/image1.tif/h5,
#           path/of/image2.tif/h5
# pp_types = standard2D, none
# is_auto_crop = yes
#
# the [label] sections indicate ground truth of network outputs
# format could be 24bit RGB or gray image with any bit depth.
# the mask images should be binary image with any bit depth.
# only the voxels with gray value greater than 0 is effective for training.
#
# [label1]
# fnames = path/of/image3.tif/h5,
#          path/of/image4.tif/h5
# preprocessing type: one_class, binary_class, none, affinity
# pp_types = binary_class, binary_class
# fmasks = path/of/mask1.tif/h5,
#      path/of/mask2.tif/h5
#
# [sample] section indicates the group of the corresponding input and output labels
# the name should be the same with the one in the network config file
#
# [sample1]
# input1 = 1
# input2 = 2
# output1 = 1
# output2 = 2

# DENOISED MICROSCOPE STACKS
[image1]
fnames =../../vesselNN_dataset/denoised/burgess2014_bbbDisruption_BM4D_denoised.tif
pp_types = standard2D
is_auto_crop = yes

[image2]
fnames =../../vesselNN_dataset/denoised/burgess2014_lowerRes_hiSNR_BM4D_denoised.tif
pp_types = standard2D
is_auto_crop = yes

[image3]
fnames =../../vesselNN_dataset/denoised/burgess2014_noisySparseVessels_BM4D_denoised.tif
pp_types = standard2D
is_auto_crop = yes

[image4]
fnames =../../vesselNN_dataset/denoised/burgess2014_tgMouse_BM4D_denoised.tif
pp_types = standard2D
is_auto_crop = yes

[image5]
fnames =../../vesselNN_dataset/denoised/poon2015_BBB_Leakage_BM4D_denoised.tif
pp_types = standard2D
is_auto_crop = yes

[image6]
fnames =../../vesselNN_dataset/denoised/poon2015_BBB_noLeakage_BM4D_denoised.tif
pp_types = standard2D
is_auto_crop = yes

[image7]
fnames =../../vesselNN_dataset/denoised/poon2015_mixedSize1_BM4D_denoised.tif
pp_types = standard2D
is_auto_crop = yes

[image8]
fnames =../../vesselNN_dataset/denoised/poon2015_mixedSize2_BM4D_denoised.tif
pp_types = standard2D
is_auto_crop = yes

[image9]
fnames =../../vesselNN_dataset/denoised/poon2015_plaqueVessels_BM4D_denoised.tif
pp_types = standard2D
is_auto_crop = yes

[image10]
fnames =../../vesselNN_dataset/denoised/santos2015_lowContrastVessels_BM4D_denoised.tif
pp_types = standard2D
is_auto_crop = yes

[image11]
fnames =../../vesselNN_dataset/denoised/santos2015_mixedSizelowContrastVessels_BM4D_denoised.tif
pp_types = standard2D
is_auto_crop = yes

[image12]
fnames =../../vesselNN_dataset/denoised/santos2015_tumor_BM4D_denoised.tif
pp_types = standard2D
is_auto_crop = yes

# LABELS
[label1]
fnames =../../vesselNN_dataset/labels/burgess2014_bbbDisruption_labels_v1.tif
pp_types = binary_class
is_auto_crop = yes
fmasks =

[label2]
fnames =../../vesselNN_dataset/labels/burgess2014_lowerRes_hiSNR_labels_v1.tif
pp_types = binary_class
is_auto_crop = yes
fmasks =

[label3]
fnames =../../vesselNN_dataset/labels/burgess2014_noisySparseVessels_labels_v1.tif
pp_types = binary_class
is_auto_crop = yes
fmasks =

[label4]
fnames =../../vesselNN_dataset/labels/burgess2014_tgMouse_labels_v1.tif
pp_types = binary_class
is_auto_crop = yes
fmasks =

[label5]
fnames =../../vesselNN_dataset/labels/poon2015_BBB_Leakage_manualLabels_v2.tif
pp_types = binary_class
is_auto_crop = yes
fmasks =

[label6]
fnames =../../vesselNN_dataset/labels/poon2015_BBB_noLeakage_manualLabel_v2.tif
pp_types = binary_class
is_auto_crop = yes
fmasks =

[label7]
fnames =../../vesselNN_dataset/labels/poon2015_mixedSize1_manualLabel_v2.tif
pp_types = binary_class
is_auto_crop = yes
fmasks =

[label8]
fnames =../../vesselNN_dataset/labels/poon2015_mixedSize2_labels_v1.tif
pp_types = binary_class
is_auto_crop = yes
fmasks =

[label9]
fnames =../../vesselNN_dataset/labels/poon2015_plaqueVessels_label_underSegmented.tif
pp_types = binary_class
is_auto_crop = yes
fmasks =

[label10]
fnames =../../vesselNN_dataset/labels/santos2015_lowContrastVessels_labelsMarc.tif
pp_types = binary_class
is_auto_crop = yes
fmasks =

[label11]
fnames =../../vesselNN_dataset/labels/santos2015_mixedSizelowContrastVessels_labelsMarc.tif
pp_types = binary_class
is_auto_crop = yes
fmasks =

[label12]
fnames =../../vesselNN_dataset/labels/santos2015_tumor_initLabel_v1.tif
pp_types = binary_class
is_auto_crop = yes
fmasks =

# INPUT-OUTPUT DEFINITIONS
[sample1]
input = 1
output = 1

[sample2]
input = 2
output = 2

[sample3]
input = 3
output = 3

[sample4]
input = 4
output = 4

[sample5]
input = 5
output = 5

[sample6]
input = 6
output = 6

[sample7]
input = 7
output = 7

[sample8]
input = 8
output = 8

[sample9]
input = 9
output = 9

[sample10]
input = 10
output = 10

[sample11]
input = 11
output = 11

[sample12]
input = 12
output = 12
