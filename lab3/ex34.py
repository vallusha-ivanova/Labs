from random import randint
k = 0
d = 0
while k < 3:
    a = randint(0, 10)
    b = randint(0, 10)
    print("Решите пример: ", a, '+', b)
    s = int(input("Ответ: "))
    sum = a+b
    if s == sum:
       print('Правильно!')
       d = d+1
    else:
        print("Ответ неверный")
        k = k+1

print("Игра окончена")
print("Правильных ответов: ", d )
