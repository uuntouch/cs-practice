import numpy as np

# Задание 1

hours = np.arange(0,21+1,3)
print(hours)
print(hours.shape)
print(hours.ndim)
print(hours.size)
print(hours.dtype)

line = np.linspace(0,1,5)
print(line)

zeros = np.zeros(6, dtype=int)
print(zeros)

uknown_table = np.full((2,3),-1)
print(uknown_table)

identity = np.ones((3,3), dtype=int)
print(identity)

# Задание 2

print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::-2])

# Задание 3

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)
print(temperatures[1,2])
print(temperatures[0,:])
print(temperatures[:,-1])
print(temperatures[:2,1:])
print(temperatures[:2,1:3])

# Задание 4

matrix = np.arange(1, 26).reshape(5, 5)
