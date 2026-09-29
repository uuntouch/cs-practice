limit = float(input('Введите порог в градусах: '))
n = int(input('Введите количество записей: '))

error_counter = 0
excess_limits = 0
max_v = -100000000
number_counter = 0
numbers_sum = 0

for _ in range(n):
    val = input()
    if val=='error': error_counter += 1
    else: 
        current_num = float(val)

        number_counter += 1
        numbers_sum += current_num

        if current_num > limit: excess_limits += 1
        if current_num > max_v: max_v = float(val)
    
    

print(f'Количество записей, которые пришли: {n}')
print(f'Количество ошибок: {error_counter}')
print(f'Количество превышений порога: {excess_limits}')
print(f'Максимальное показание: {max_v:.1f}')
print(f'Среднее показание: {(numbers_sum/number_counter):.1f}')