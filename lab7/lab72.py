from PIL import Image, ImageOps
f = Image.open("3.jpg")

f.show()
f1 = f. reduce(3)

f1.save("31.jpg")


f1 = ImageOps.mirror(f1)
f1.save("32.jpg")
f1.show("32.jpg")

f1 = f1.transpose(Image.FLIP_TOP_BOTTOM)
f1.save("33.jpg")
f1.show("33.jpg")