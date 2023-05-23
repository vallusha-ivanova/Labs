class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')


class IceCreamStand(Restaurant):
      def __init__(self, restaurant_name, cuisine_type, flavors):
          super().__init__(restaurant_name, cuisine_type)
          self.flavors = flavors

      def flavors_icecream(self):
          print(f'Виды мороженного:{self.flavors}')


s = IceCreamStand("Отмороженные", 'кафешка', ['ваниль', 'пломбир', 'шоколад'])
s.flavors_icecream()
