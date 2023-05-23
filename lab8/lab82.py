from PIL import Image, ImageFont
albom={"Новый год" : "новый год.jpg", "8 марта" : "с 8 марта.jpg", "Пасха": " пасха.jpg"}

i = input('К какому празднику нужна открытка?')
k = Image.open(albom[i])
k.show()