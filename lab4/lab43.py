a = input('Впишите дату в виде 02.11.2022 ').split('.')
b = int(a[0])
c = int(a[1])
if b * c == int(a[2][2:]):
    print('Mагия')
else:
    print('НЕ МАГИЯ')