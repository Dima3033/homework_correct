num1 = int(input('Введіть число -  '))
num2 = int(input('Введіть число -  '))
while num1 < num2:
    num1 += 1
    if num1 % 3 == 0:
        print('Fizz')
    elif num1 & 5 == 0:
        print('Buzz')
    elif num1 % 3 == 0:
        print('Fizz Buzz')
    if num1 % 5 == 0:
        print('Fizz Buzz')
    elif num1 % 3 == 1:
        print(f'{num1}')
    if num1 % 5 == 1:
         print(f'{num1}')
