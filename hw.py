num1 = int(input('Введіть число 1 -'))
num2 = int(input('Введіть число 2 -'))
print('Усі числа діапазону')
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
number = num1
while number < num2:
    print(f'number = {number}')
    number += 1
else:
    print(f'number = {num1}')
print('Усі числа діапазону за спаданням')
number = num2
while number > num1:
    print(f'{number}')
    number -= 1
else:
    print(f'{number}')
print('Числа кратні 7')
if num1 < 7:
    num1 += (7 % num1)
elif num1 > 7:
    num1 = (num1 - (num1 % 7))+7
number = num1
while number <= num2:
    print(f'{number}')
    number += 7
print(' Числа кратні 5')
if num1 < 5:
    num1 += (5 % num1)
elif num1 > 5:
    num1 = (num1 - (num1 % 5))+5
number = num1
while number <= num2:
    print(f'{number}')
    number += 5