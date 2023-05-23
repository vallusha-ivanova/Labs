from PIL import Image, ImageFilter
img = Image.open('бтс с днем рождения.jpg')
img.show()
width, height = img.size
format = img.format
mode = img.mode

print("Высота: ", height, " ", "Ширина: ", width)
print("Формат: ", format)
    