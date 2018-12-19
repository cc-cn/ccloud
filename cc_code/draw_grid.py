import numpy as np
import copy
import os
import cv2
import sys



def draw_dashed_grid(im, new_name, height, width):
    img_new = im.copy()
    for start_x in range(10, width, 10):
        end_x = start_x
        for y in range(10, height, 10):
            cv2.line(img_new, (start_x, y-1), (end_x, y), (0, 0, 255), 1)
  
    cv2.imwrite('result/{}'.format(new_name), img_new)


if __name__ == '__main__':
    if len(sys.argv)!=2:
        print('tips : python draw_grid.py img_list')  
        print('the result is saved in result/img and result/anno , need not mkdir by myself' )
        sys.exit()
    img_list=sys.argv[1]
    with open(img_list, 'r') as f:
        lines = f.readlines()

    id = 0

    if not os.path.exists('result/'):
        os.makedirs('result')

    process_num = 0
    for line in lines:
        img_name = line.strip().split()[0]
        im = cv2.imread(img_name)  #numpy (h x w x c)
        height, width, channel = im.shape
        #print(height, width, channel)
        #sys.exit()
        new_name=img_name.split('/')[-1]

        draw_dashed_grid(im, new_name, height, width)


        process_num +=1
        if process_num%100 == 0:
            print('processing:{}'.format(process_num))

