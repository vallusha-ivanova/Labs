class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

    def open_restaurant(self):
        print('Ресторан сейчас открыт)!')


newRestaurant = Restaurant('У хозяина болота', 'китайская')
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
Restaurant1 = Restaurant('Евро-кебаб', 'грузинская')
Restaurant2 = Restaurant('Найс-блюдо', 'фастфуд')
Restaurant3 = Restaurant('Вокзал', 'межнациональная')

Restaurant1.describe_restaurant()
Restaurant2.describe_restaurant()
Restaurant3.describe_restaurant()


