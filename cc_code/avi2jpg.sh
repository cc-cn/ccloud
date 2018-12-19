#!/bin/bash  


  
for i in `ls data_avi`;  
do

pre=${i%.*}
dst=data_img\/$pre\/
mkdir $dst
src=data_avi\/$i

#0.2 fps
avconv -i $src -r 0.2 -q:v 2 -f image2 $dst%6d.jpg

done
