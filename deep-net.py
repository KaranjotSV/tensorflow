import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

# Here we define our computation graph
result = tf.multiply(x1, x2)

print(result)

# Here we define a session to run our graph
with tf.Session() as sess:
	output = sess.run(result)
	print(output)
