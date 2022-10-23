from random import randint

while True:
    try:
        length = int(input('Введите размер первого массива: '))
        delta = int(input('Введите delta: '))
        break
    except(ValueError, TypeError):
        print('Введите другое значение')

a = [0] * length
count = 0
mini = a[0]

for i in range(length):
    a[i] = randint(-10, 10)

print(a)

for i in range(length):
    if a[i] < mini:
        mini = a[i]

for i in range(length):
    if mini + delta == a[i]:
        count += 1

print(count)