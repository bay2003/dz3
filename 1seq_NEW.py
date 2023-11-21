cifra = int(input('элементы'))
result = []

for i in range (cifra):
    number = int (input('Введите число'))
    result.append(number)
result.sort()
print(result)