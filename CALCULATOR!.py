from tkinter import *

root = Tk()
root.title("Калькулятор")
root['bg'] = '#ffb700'
root.geometry('500x500')

spec_symbols = '+-*/'


def is_operation_yet():
    text = entry.get()
    for symb in spec_symbols:
        if text.find(symb, 1, len(text)) >= 0:
            return True
    return False


def input_into_entry(symbol):  # добавляет новый символ на экран
    if symbol not in spec_symbols:
        entry.insert(END, symbol)
    elif is_operation_yet() == False:
        entry.insert(END, symbol)


def clear():
    entry.delete(0, END)


def count_result():
    text = entry.get()
    result = 0
    if "+" in text:
        splitted_text = text.split('+')
        a = float(splitted_text[0])
        b = float(splitted_text[1])
        result = a + b

    if '-' in text:
        splitted_text = text.split('-')
        a = float(splitted_text[0])
        b = float(splitted_text[1])
        result = a - b

    if '*' in text:
        splitted_text = text.split('*')
        a = float(splitted_text[0])
        b = float(splitted_text[1])
        result = a * b

    if '/' in text:
        splitted_text = text.split('/')
        a = float(splitted_text[0])
        b = float(splitted_text[1])
        if b == 0:
            result = 'error'
        else:
            result = a / b
    clear()
    if result == 'error':
        entry.insert(0, result)
    else:
        if result == int(result):  # проверка на целочисленность результата
            result = int(result)
        entry.insert(0, result)


entry = Entry(root, width=15, font=(" ", 20)) # поле для ввода
entry.place(x=100, y=50)

b1 = Button(root, bg='white', fg='black', text='1', command=lambda: input_into_entry('1'))
b1.place(x=100, y=100, width=50, height=50)

b2 = Button(root, bg='white', fg='black', text='2', command=lambda: input_into_entry('2'))
b2.place(x=150, y=100, width=50, height=50)

b3 = Button(root, bg='white', fg='black', text='3', command=lambda: input_into_entry('3'))
b3.place(x=200, y=100, width=50, height=50)

b_plus = Button(root, bg='white', fg='black', text='+', command=lambda: input_into_entry('+'))
b_plus.place(x=250, y=100, width=50, height=50)

b4 = Button(root, bg='white', fg='black', text='4', command=lambda: input_into_entry('4'))
b4.place(x=100, y=150, width=50, height=50)

b5 = Button(root, bg='white', fg='black', text='5', command=lambda: input_into_entry('5'))
b5.place(x=150, y=150, width=50, height=50)

b6 = Button(root, bg='white', fg='black', text='6', command=lambda: input_into_entry('6'))
b6.place(x=200, y=150, width=50, height=50)

b_minus = Button(root, bg='white', fg='black', text='-', command=lambda: input_into_entry('-'))
b_minus.place(x=250, y=150, width=50, height=50)

b7 = Button(root, bg='white', fg='black', text='7', command=lambda: input_into_entry('7'))
b7.place(x=100, y=200, width=50, height=50)

b8 = Button(root, bg='white', fg='black', text='8', command=lambda: input_into_entry('8'))
b8.place(x=150, y=200, width=50, height=50)

b9 = Button(root, bg='white', fg='black', text='9', command=lambda: input_into_entry('9'))
b9.place(x=200, y=200, width=50, height=50)

b_um = Button(root, bg='white', fg='black', text='*', command=lambda: input_into_entry('*'))
b_um.place(x=250, y=200, width=50, height=50)

b_del = Button(root, bg='white', fg='black', text='/', command=lambda: input_into_entry('/'))
b_del.place(x=250, y=250, width=50, height=50)

b_res = Button(root, bg='white', fg='black', text='=', command=count_result)
b_res.place(x=200, y=250, width=50, height=50)

b_clear = Button(root, bg='red', fg='black', text='CE', command=clear)
b_clear.place(x=300, y=250, width=50, height=50)

b0 = Button(root, bg='white', fg='black', text='0', command=lambda: input_into_entry('0'))
b0.place(x=150, y=250, width=50, height=50)

b_tochka = Button(root, bg="white", fg='black', text=",", command=lambda: input_into_entry('.'))
b_tochka.place(x=100, y=250, width=50, height=50)

root.bind()

root.mainloop()