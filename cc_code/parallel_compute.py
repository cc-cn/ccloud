#!/usr/bin/env python
#-*- coding:utf-8 -*-
#折腾了很久发现,全局变量的修改不适用多线程,对于有返回值的多线程问题,目前来看还是不好处理.将结果写入本地是一个办法.


import os
import numpy as np
import multiprocessing
import time

num_proc=8
ans=np.zeros(num_proc)

def f(i,num_proc):
    sum=0
    size=1000000
    id=i
    
    while i<size:
        if i%2==1:
            sum+=1.0/(2*i-1)
        else:
            sum-=1.0/(2*i-1)
        i+=num_proc
    #global ans
    #print(id,sum)
    ans[id-1]=4*sum




if __name__ == '__main__':
    begin=time.time()
    '''
    #ans=np.zeros(num_proc)
    pool = multiprocessing.Pool(processes = num_proc)
    for i in range(1,1+num_proc):
        pool.apply_async(f, (i,num_proc,))
    pool.close()
    pool.join()
    '''
    f(1,8)
    f(2,8)
    f(3,8)
    f(4,8)
    f(5,8)
    f(6,8)
    f(7,8)
    f(8,8)



    pi=np.sum(ans)

    end=time.time()

    print('pi=%.8f'%pi)
    print('time:%.4fs '%(end-begin))