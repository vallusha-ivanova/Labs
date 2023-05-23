from PIL import Image, ImageFilter
f = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "sobaken.jpg"]
for f1 in f:
    f=Image.open(f1)
    f = f.filter(ImageFilter.CONTOUR)
    f.show()
    f.save("photo/1" + f1)

