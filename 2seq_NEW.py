str_cifra = input('Введите числа, разделенные запятой: ')
numbers = str_cifra.split(',')

print("Уникальные числа:", set(numbers))

result = []
for str_cifra in numbers:
    if numbers.count(str_cifra) == 1:
        result.append(str_cifra)

print("Числа, встречающиеся в списке только один раз:", result)

