import os
import cv2

#num=10


pathDir=os.listdir('/home/chencheng/data/base_35000/')
img_face=open('/home/chencheng/data/img_label_face','w')
for allDir in pathDir:
#    num-=1
#    if num==0:
#	break
    if allDir[-1]!='5':
        child=os.path.join('%s%s' %('/home/chencheng/data/base_35000/',allDir))
        child_h5 = child[:-3]+'h5'
	h,w,c=cv2.imread(child).shape
	#print h,w,c
	img_face.write(child.decode('gbk')+'\t'+child_h5.decode('gbk')+'\t'+str(h)+'\t'+str(w)+'\n')

img_face.close()
print(0)
