import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


#build a graph
x1 =tf.constant(5)
x2 =tf.constant(6)

result = tf.multiply(x1,x2)  #use multiply() instead of mul()

print(result)

##sess=tf.Session()
##print(sess.run(result))
##sess.close()


#do what will happen in the session
with tf.Session() as sess:
    output = sess.run(result)
    print(output)
