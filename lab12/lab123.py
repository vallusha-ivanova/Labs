from tkinter import *
class IceCreamStand:
    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors

    def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

    def flavors_cream(self):
        print('Сорт мороженного:')
        print(*self.flavors)




s = IceCreamStand("BasketRobins", 'морожница', ['пломбир', 'клубника', 'шоколад'])

s.describe_restaurant()
s.flavors_cream()

root = Tk()
root.title("BasketRobins")
root.geometry('300x300')




title = Label(root, text="Available flavors", font=35)
title.pack()
for i in s.flavors:
    title = Label(root, text=i, font=35)
    title.pack()

root.mainloop()
