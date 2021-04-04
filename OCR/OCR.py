# coding=UTF-8
from PIL import Image
import pytesseract as pt

#辨識圖片需放在該目錄
img = Image.open('chinese.jpg')
#
# #英文 'eng'、簡體中文 'chi_sim'、繁體中文 'chi_tra'
text = pt.image_to_string(img, lang='chi_tra')
print(text)