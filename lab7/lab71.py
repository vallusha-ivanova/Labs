from PIL import Image
filename = "3.jpg"
with Image.open(filename) as img:
    img.load()

    img.show()
    width, height = img.size
    format = img.format
    mode = img.mode

    print("Высота: ", height, " ", "Ширина: ", width)
    print("Формат: ", format)
    print("Цветовая модель: ", mode)
