import math
import numpy as np
import tensorflow as tf

print('It\'s math!, It has the type {}'.format(type(math)))
print(dir(math))

# Accessing modules namespaces with dot syntax
print("The value of PI is {:.4}".format(math.pi))
print("Log function: {:.4}".format(math.log(5, 2)))

# Double dot calling
rolls = np.random.randint(low=2, high=50, size=15)
print(rolls, type(rolls))
print(rolls.mean(), rolls.tolist())

# Flattened array of type numpy.ndarray
print(rolls.ravel())

# Operator Overloading
print(rolls + 10)
print(rolls <= 3)

# 2D array
x_list = [[1, 2, 3], [4, 5, 6]]
x = np.asarray(x_list)
print("List : {} \n numpy array {}".format(x_list, x))
print(x[1, -1], x_list[1][2])  # Last element of the second row of our numpy array and List differ so much

# Tensorflow data types
# Create constants, each with value 1
a = tf.constant(1)
b = tf.constant(2)
c = a + b
print(a, b, c)
sess = tf.Session()
print(sess.run(c))
