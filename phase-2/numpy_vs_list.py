# This script compares multiplication behavior between Python lists and NumPy arrays.

import numpy as np

py_list = [1, 2, 3]
np_array = np.array([1, 2, 3])
res_py_list = py_list * 3
res_np_array = np_array * 3
print("Python list result:", res_py_list)
print("NumPy array result:", res_np_array)
print("Type of Python list:", type(py_list))
print("Type of NumPy array:", type(np_array))
