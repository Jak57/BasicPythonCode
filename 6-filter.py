# From PILO library import Image and ImageFilter functions
from PIL import Image, ImageFilter

# In python structure can contain not only data but also functions
before = Image.open("tower.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("output.bmp")
