import csv
with open('3.csv') as f:
    rdr = csv.reader(f, delimiter=";")
    c = 0
    kol = 0
    print("Нужно купить:")
    for k in rdr:
        if c > 0:
            print(f'    {k[0]} - {k[1]} шт. за {k[2]} руб.')
            c += 1
            kol += int(k[2])
        c += 1
    print('Итоговая сумма:', kol, 'руб.')