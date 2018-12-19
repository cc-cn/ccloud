# Python
#这段代码给出了使用不同方式计算数组只和等效率
import time
import tensorflow as tf

num=5000000

x=tf.Variable(list(range(num)))
y=tf.Variable(list(range(num)))
z=x+y

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
t2=time.time()
w=sess.run(z)
t3=time.time()
print('gpu:',t3-t2)

x1=list(range(num))
y1=list(range(num))
t1=time.time()
z1=x1+y1
t2=time.time()
print('cpus:',t2-t1)
for i in range(num):
    z1[i]=x1[i]+y1[i]
t4=time.time()

print('cpu:',t4-t3)

print(z1[999])
