#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import multiprocessing
import shutil





if __name__ == '__main__':
    pool = multiprocessing.Pool(processes = 120)
    for img_path in os.listdir('/media/chencheng/bab1c43f-8e0f-47dd-8ab7-a6a7a5586ec1/personreidnight_img/'):
        pool.apply_async(shutil.copytree,('/media/chencheng/bab1c43f-8e0f-47dd-8ab7-a6a7a5586ec1/personreidnight_img/{}'.format(img_path),'new/{}'.format(img_path)))
        print(img_path)
    pool.close()
    pool.join()
