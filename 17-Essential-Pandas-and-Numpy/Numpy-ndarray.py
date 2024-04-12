# Creating an n-dimensional array
# 1 row = 1 list

# Example: Creating an n-dimensional array
# Importing the NUMPY library is the very first thing to do

import numpy as np

height = [159., 163., 158., 170., 169., 168., 162., 167., 160.]
h_arr = np.array(height)
print(h_arr)
h_arr_shape = h_arr.shape
print(h_arr_shape)

# Example: N-dimensional array from standard functions
# Create a 1-dimensional array containing 10 consecutive zeros
arr_of_ten_zeros = np.zeros(10)
print(arr_of_ten_zeros)

# Create a 1-dimensional array containing 10 consecutive ones as the element and dtype of int instead of float.
arr_of_ten_ones = np.ones(shape=(1,10), dtype = 'int')
print(arr_of_ten_ones)

# Check dtype
print(arr_of_ten_ones.dtype)

# Creating a 1-dimensional array with elements starting from 0,1,2,...,10.
print(np.arange(11))

# Creating a 1-dimensional array with elements starting from 0.1, 0.3, 0.5, ..., 0.9.
print(np.arange(0.1, 1.0, 0.2))