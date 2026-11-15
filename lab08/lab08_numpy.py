import numpy as np

# Задание 1

print('Задание 1\n')
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

print('\nЗадание 2\n')
print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::-2])

# Задание 3

print('\nЗадание 3\n')
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

print('\nЗадание 4\n')
matrix = np.arange(1, 26).reshape(5, 5)

print(matrix[:4,:])
print(matrix[:4,:].shape)

print(matrix[-2:,:])
print(matrix[-2:,:].shape)

print(matrix[:,:2])
print(matrix[:,:2].shape)

print(matrix[1:4,2:5])
print(matrix[1:4,2:5].shape)

print(matrix[-2:,-2:])
print(matrix[-2:,-2:].shape)

# Задание 5

print('\nЗадание 5\n')

changed_hours = hours.copy()

changed_hours[2:5] = 99
changed_hours[::2] = -1
print(changed_hours)
print(hours)
# .copy() - создаем именно копию массива так что все 
# изменения в changed_hours не будут менять исходную hours

changed_matrix = matrix.copy()
changed_matrix[1,:] = 0
changed_matrix[:,-1] = -1
changed_matrix[1:4,1:4] = 100
print(changed_matrix)
print(matrix)

# Задание 6

print('\nЗадание 6\n')

numbers = np.arange(0,12)
table = numbers.reshape(3,4)
transposed = table.T
print(numbers.shape)
print(table.shape)
print(transposed.shape)
# reshape(3, 4) работает, а reshape(5, 3) вызовет ошибку 
# потому что для (3,4) нужно 12 элементов а для (5,3) 15, т.к reshape 
# не изменяет кол-во элеменетов