import tesserocr
from PIL import Image

image = Image.open('code.jpg')
result = tesserocr.image_to_text(image)
print(result)

# tesserocr 还有一个更加简单的方法，不过该方法识别效果不如上面的方法。
print(tesserocr.file_to_text('image.png'))
