a1=int(input("Введите номер места"))
if a1 % 2 ==0 and a1 in range(1,37):
    print("Вверх")
if a1 % 2 != 0 and a1 in range(1,37):
    print("Низ")
if a1 % 2 == 0 and a1 in range(37,55):
    print("Вверх боковушки")
if a1 % 2 != 0 and a1 in range(37,55):
    print("Низ боковушки")
if a1>54:
    print("Неправильный номер")