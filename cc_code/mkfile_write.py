import os

goal='/home/chencheng/data/deepv_car_person_voc_style/20161230/Annotations/10.209.4.147-3-161217_133715.xml'

os.mkdir('result')

goal_list=goal.split('/')

os.mkdir('result/'+goal_list[-3])

os.mkdir('result/'+goal_list[-3]+'/'+goal_list[-2])

f=open('result/20161230/hello.txt','w')

f.write('hahadahahada\n')

f.close()

