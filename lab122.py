class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')


class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, place, time):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.place = place
            self.time = time

        def flavors_cream(self):
            print('Сорт мороженного:')
            print(*self.flavors)

        def add_flavor(self):
            self.flavors.append(input('Какой сорт мороженого хотите добавить? '))

        def min_flavor(self):
            self.flavors.remove(input('Какой сорт хотите удалить? '))

        def poisk(self):
            if input('Какой вкус хотите найти? ') in self.flavors:
                print('Такой есть)')
            else:
                print('К сожалению, такого нет(')

class Nano(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, place, time, sale):
            super().__init__(restaurant_name, cuisine_type, flavors, place, time)
            self.sale = sale

        def price(self):
            print('Цена: ', self.sale)

class Glisse(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, place, time, shariki):
            super().__init__(restaurant_name, cuisine_type, flavors, place, time)
            self.shariki = shariki

        def count(self):
            print('Кол-во шариков:', self.shariki)



s = IceCreamStand("BasketRobins", 'морожница', ['пломбир', 'клубника', 'шоколад'], 'ул. Пражская', '6:00-18:00')
s.describe_restaurant()
s.add_flavor()
s.flavors_cream()
s.min_flavor()
s.flavors_cream()
s.poisk()

s = Glisse('Морожка', 'кафе', ['пломбир', 'клубника', 'шоколад'], 'ул. Пражская', '8:00-22:00', '3')
s.count()

s = Nano('Морожка', 'кафе', ['пломбир', 'клубника', 'шоколад'], 'ул. Пражская', '8:00-22:00', '50')
s.price()




