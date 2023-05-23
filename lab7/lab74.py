from PIL import Image
f = Image.open("3.jpg")
watermark = Image.open("watermark.png")
f.paste(watermark, (50,50), watermark)
f.save("3water.jpg")
f.show()