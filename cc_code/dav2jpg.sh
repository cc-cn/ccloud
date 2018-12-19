#!/bin/bash  


for i in `ls /media/chencheng/bab1c43f-8e0f-47dd-8ab7-a6a7a5586ec1/personreidnight/`;
do

pre=${i%.*}
dst=/media/chencheng/bab1c43f-8e0f-47dd-8ab7-a6a7a5586ec1/personreidnight_img/$pre

if [ ! -d $dst ]
then
 mkdir $dst
else
 continue
fi
src=/media/chencheng/bab1c43f-8e0f-47dd-8ab7-a6a7a5586ec1/personreidnight/$i

ffmpeg -i $src -r 0.4 $dst/%3d.jpg

done
