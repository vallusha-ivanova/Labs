a = int(input('Введите номер билета'))
a1 = int(len(a))
b = int(a1/2)
sum1 = 0
sum2 = 0

if a1 % 2 == 0:
    for i in range(b):
        sum1 += int(a[i])
     for j in range(b, a1):
         sum2 += int(a[j])
    if sum1 == sum2:
     print('Ваш билет счастливый')
     else:
     print('Ваш билет обычный')
else:
    print('Ваш билет нечетный')
print(sum1,sum2)