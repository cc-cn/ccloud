#!/bin/bash  


  
for i in `ls ../videos`;  
do

pre=${i%.*}
dst=data_avi\/$pre.avi
src=..\/videos\/$i
avconv -y -i $src -vcodec libx264 -crf 24 -filter:v "setpts=1*PTS" $dst
#echo $src ;  

done
