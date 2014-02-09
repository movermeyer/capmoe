# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter


img = Image.open('caps.jpg')

# print(im.format, im.size, im.mode)
# im.show()

# 画像の輪郭抽出する
# img = ImageOps.grayscale(img)
(
img
    .convert('L')  # グレースケール
    .filter(ImageFilter.FIND_EDGES)  # エッジ検出
    .convert('1')  # 2値化

    .save('caps_edge_2v.jpg')
    # .show()
)


# ImageOps.grayscale(img1)
