import numpy as np
import cv2
import sys
import os



with open('result_list', 'r') as f:
	lines = f.readlines()

for line in lines:
	img = line.strip().split()[0]
        #img_gt=os.path.join('%s%s' %('/Users/ccmac/compare_preds/result/',img))
        img_gt=os.path.join('%s%s' %('result/',img))
        im = cv2.imread(img_gt)
        #print(im[...])
        window = "gt"
        cv2.namedWindow(window)
	cv2.imshow(window, im)
	key = cv2.waitKey()
        if key == 27 or key== -1:
                sys.exit(0)
	
        
