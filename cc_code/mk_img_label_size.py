import os
import cv2

i=0

pathDir=os.listdir('/home/chencheng/data/yingshi_include_xml/')
img_face=open('/home/chencheng/rfcn_from_hyy/jobs/pd/yingshi_task/train_img_label_size','w')
for allDir in pathDir:
    if allDir[-1]=='l':
        child_xml = os.path.join('%s%s' %('/home/chencheng/data/yingshi_include_xml/',allDir))
        child_img = child_xml[:-3]+'jpg'
	if os.path.exists(child_img)==False:
		print("{} not exist".format(child_img))
		continue

	i+=1
	print(i)
        h,w,c=cv2.imread(child_img).shape
        #print h,w,c
        img_face.write(child_img.decode('gbk')+'\t'+child_xml.decode('gbk')+'\t'+str(h)+'\t'+str(w)+'\n')

img_face.close()
print(0)
