class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, reiting):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.reiting = reiting

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print('Открыто!')

        def write_reiting(self):
            print(f'Бывший рейтинг: {self.cuisine_type}')
            self.cuisine_type = input('Новая кухня: ')
            print(f'Обновлено: {self.cuisine_type}')

newRestaurant = Restaurant('У хозяина болота', 'китайская', '5')
newRestaurant.write_reiting()


