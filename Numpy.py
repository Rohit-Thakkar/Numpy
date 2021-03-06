# This is the standard abbreviation for importing NumPy.
import numpy as np

# This adds dimensions to arrays (see the end of lesson two).
from numpy import newaxis as nax

# Matplotlib is a plotting library, as you saw in pset 7 with plot_demo.py .
# This is a standard abbreviation too.
import matplotlib.pyplot as plt

# A numpy array is a data structure with a fixed size and the ability to do
# very fast operations over the entire array. If you've used MATLAB before,
# they're similar to MATLAB arrays. The first big difference is that they're
# indexed from 0 instead of 1; we'll see a few more as we go.

# When working with NumPy and matplotlib, it's often helpful to use IPython, a
# more convenient interface to the python interpreter.

# Try starting it from the terminal with
#      $ ipython --pylab
# This automatically performs the two imports listed above, as well as some
# others. You can easily access function help with the question mark:
#      In [1]: np.arange?
# (you can scroll with arrows or vim/emacs hotkeys, and quit the help with 'q')
# IPython also has features like tab completion, easy access to timing and
# performance measurement (try 'timeit' and see lesson four below), and more!

# SciPy is a huge library with all kinds of useful functions; for now we just
# want it so we can read image files
import scipy.misc as misc


#def lesson_one():
# np.arange is like range(), but as an array
x = np.arange(10)
print(x)

# Performing math operations on every element of an array is easy:
print(x + 100)
print(x * 3)
print(x ** 2) # MATLAB users: note that the behavior here is different!
print(x < 8)
print(np.sin(x * 36))

# pause
raw_input('Press enter to continue')
# Let's generate sequences by specifying the step size:
q1 = np.arange(0, 1, .2)

# ...or by specifying the number of elements
q2 = np.linspace(0, 1, 9)

print(q1)
print(q2)

# Computing functions over every value of an array is a cinch:
binary_entropy = - (q2*np.log(q2) + (1-q2)*np.log(1-q2))
print(binary_entropy)

##############################################################
#def lesson_two():
# Arrays can be two-dimensional (e.g. to represent matrices):
a = np.ones([7,4])
print(a)

# an array has several attributes:
print(a.shape)
print(a.size)
print(a.dtype) # usually float64 (double), or int64 (long)

raw_input('Press enter to continue')
# We can turn one-dimensional arrays into two-dimensional ones (and
# vice-versa):
b = np.arange(28).reshape([7,4])
print(b) # notice that numbers increase by row first and then by column
print(b.dtype) # arange with integers creates arrays of integers

# Accessing array elements:
print(b[0,0])
print(b[6,1])
print(b[2,3])
print(b[(0,6,2), (0,1,3)])

# We can access an entire row or column using colon:
print(b[5,:])
print(b[:,2])
# These are called "slices", and this operation is called "slicing".

raw_input('Press enter to continue')
# We can add arrays:
print(a+b)

# We can also subtract, multiply, divide, and more. Unlike MATLAB,
# multiplying two arrays together with * performs elementwise
# multiplication:
print((a+1)*b)

raw_input('Press enter to continue')

# We can also sum across all rows or all columns:
print(np.sum(b, 1))
print(np.prod(b, 0))

# What if we want all the rows to sum to one? We can divide every row by 
# its sum by using *broadcasting*:
row_sums = np.sum(b,1)
print(row_sums.shape)
row_sums = row_sums[:, nax] # This 'adds' a dimension of size 1 to the end
print(row_sums.shape)
print(b / row_sums)

# For more info on broadcasting, see
# http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html

# We can also represent higher-dimensional arrays:
c = np.arange(24).reshape([2,3,4])

# Since we can't actually display a 3d object on a 2d screen, these are 
# printed as a series of two-dimensional slices
print(c)
print(np.sum(c,1))

# Last but not least, we can specify arrays manually:
d = np.array([1,2,3])
print(d)
e = np.array([[4,8,12],[20,40,60]])
print(e)

##############################################################
#def lesson_three():
# We can also use numpy to easily generate random numbers: Try
# np.random.randint?
f = np.random.randint(5)
print(f)
g = np.random.randint(10, 20, [8,2])
print(g)
