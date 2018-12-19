import os
import cv2
import numpy as np
import sys

if len(sys.argv)!=2:
	print('tips : python random_display.py img_list')
	exit()
img_label=sys.argv[1]


t=0

with open(img_label, 'r') as f:
	lines = f.readlines()
	for line in lines:
			t=t+1
			if t%1000 == 0:
					img_dir = line.strip().split()[0]

					#print(img_dir)
					lena = cv2.imread(img_dir) 
					#print(lena[:,:,0].shape)
					try:
						print(np.mean(lena[:,:,0]))
					except:
						continue
					cv2.imshow('img', lena)
					key=cv2.waitKey()
					if key == 27 or key == -1:
						sys.exit()
			if t==100000:
				sys.exit()


