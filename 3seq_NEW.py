str_cifra = input('Введите числа, разделенные запятой: ')
numbers = str_cifra.split(',')

str_num = input('Введите числа, разделенные запятой: ')
numbers2 = str_num.split(',')

print(numbers,numbers2)

print(set(numbers) - set(numbers2))
