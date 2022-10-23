# n = int(input()) 

while True:
    try:
        n = int(input('Введите размер массива: '))
        break
    except(ValueError, TypeError):
        print('Введите другое значение')
        
a = [float(x) for x in input('Введите элементы массива через пробел: ').split()]
max = a[0]

for i in range(1, n):
    if a[i] > max:
        max = a[i]
        ind = i

for i in range(ind + 1, n):
    a[i] = 0

print(a)