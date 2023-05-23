from PIL import Image, ImageFont, ImageDraw
i = Image.open('бтс с днем рождения.jpg')
i.show()
print('Размер:', i.size, 'Формат:', i.format , 'Цветовая модель:', i.mode)
i = i.crop((100, 75, 300, 150))
i.show()
i.save('бтс обрезка.jpg')