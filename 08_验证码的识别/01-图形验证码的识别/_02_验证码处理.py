import tesserocr
from PIL import Image

"""为处理前识别为 'PFRT.' """
image = Image.open('code2.jpg')

image = image.convert('L')  # 转化为灰度图像
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')  # 将图片进行二值化处理
image.show()

result = tesserocr.image_to_text(image)
print(result)
