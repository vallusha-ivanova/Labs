from random import randint
st = ['Воробьева', 'Коршунова', 'Шарипова', 'Соркина']
l = ['английский', 'китайский', 'немецкий']
s = {}
for i in st:
    c = randint(1, 2)
    s[i] = l[c]

print(s)
print(sorted(l))

for i in s:
    if s[i] == 'китайский':
        print(i)
