n1 = int(input('введи число 1 - '))
n2 = int(input('введи число 2 - '))
if n1 < 7:
    n1 += (7 % n1)
elif n1 > 7:
    n1 =(n1-(n1%7))+7
number = n1
while number <= n2:
    print(f'{number}')
    number +=7