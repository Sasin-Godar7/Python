import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

print(a)
print(b)

zeros_arr = np.zeros((2,3))
print(zeros_arr)

ones_arr = np.ones((2,3))
print(ones_arr)

twos_arr = np.ones((2,3))*2
print(twos_arr)

#Random  
random_arr = np.random.random((2,3))      # random vani aauta module ho tyo bata we need only random values
print("Random Array :\n",random_arr)

random_int = np.random.randint(1,10,(2,3))     # random vani aauta module ho tyo bata we need only random integer values
print("Random integer\n",random_int)
print("\n")

#1D
arr_1d = np.array([1,2,3,4])
print(arr_1d)
print("shape ",arr_1d.shape)

#2D
arr_2d = np.array(([1,3,6],[9,3,5]))
print(arr_2d)
print("shape",arr_2d.shape)

print("number of dimension:",arr_2d.ndim)
print('size',arr_2d.size)
print("date type :",arr_2d.dtype)
print("item size:",arr_2d.itemsize)

print("\n")

#3D
arr_3d = np.array([[[1,2,3],[3,4,5],[5,6,7]]])
print(arr_3d)
print("shape",arr_3d.shape)

print("number of dimension:",arr_3d.ndim)
print('size',arr_3d.size)
print("date type :",arr_3d.dtype)
print("item size:",arr_3d.itemsize)
