# -*- coding:utf-8 -*-
import tensorflow as tf
# create graph
a = tf.constant(2)
b = tf.constant(3)
c = tf.add(a,b)


# writer = tf.summary.FileWriter('./graphs', tf.get_default_graph())

with tf.Session() as sess:
    writer = tf.summary.FileWriter('./graphs', sess.graph)
    print(sess.run(c))
    writer.close()

