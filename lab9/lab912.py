from PIL import Image, ImageFilter
from pathlib import Path

a = ''
file = Path(a).glob('*')
Path('photo9912').mkdir(parents=True, exist_ok=True)
for i in file:
       if i.suffix in ['.jpg', '.png']:
          with Image.open(i) as photo:
              photo.load()
              new_photo = photo.filter(ImageFilter.GaussianBlur(20))
              new_photo.show()
              new_photo.save(Path('photo9912', i))

