a = float(input('Введите 1 число: '))
b = float(input('Введите 2 число: '))
c = float(input('Введите 3 число: '))

m = a
if m > b:
    m = b
if m < c:
    m = c
print(m)