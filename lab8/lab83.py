from PIL import Image, ImageFont, ImageDraw
i = Image.open('бтс с днем рождения.jpg')
n = input('Имя, кого вы хотите поздравить?')
font = ImageFont.truetype("arial_bold.ttf", 35)
d = ImageDraw.Draw(i)
d.text((30, 60), n + ", поздравляю!", font = font, fill = 'blue')

i.show()
i.save('pozdrav bts.jpg')