from random import random

# число случайно
m1 = int(input('от: '))
m2 = int(input('до: '))
n = int(random() * (m2 - m1 + 1)) + m1
print(n)

# вещественное число
m1 = float(input('от: '))
m2 = float(input('до: '))
n = random() * (m2 - m1) + m1
print(round(n, 3))

# случайная буква
m1 = ord(input('от: '))
m2 = ord(input('до: '))
n = int(random() * (m2 - m1 + 1)) + m1
print(chr(n))