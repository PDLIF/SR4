from random import randint

while True:
    try:
        n = int(input('Введите размер первого массива: '))
        e = int(input('Введите размер второго массива: '))
        break
    except(ValueError, TypeError):
        print('Введите другое значение')

a = [0] * n
b = [0] * e
c = []

for i in range(n):
    a[i] = randint(-10, 10)

for j in range(e):
    b[j] = randint(-5, 5)

print(a)
print(b)

for i in range(n):
    for j in range(e):
        if a[i] == b[j]:
            c.append(a[i])

if c:
    print(c)
else:
    print('Массив пустой')
