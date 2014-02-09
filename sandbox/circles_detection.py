# -*- coding: utf-8 -*-
''' file name : houghcircles.py

Description : This sample shows how to detect circles in image with Hough Transform

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/imgtrans/hough_circle/hough_circle.html

Level : Beginner

Benefits : Learn to find circles in the image and draw them

Usage : python houghcircles.py

Written by : Abid K. (abidrahman2@gmail.com) , Visit opencvpython.blogspot.com for more tutorials '''

import cv2
import numpy as np
import sys
from random import randint


if __name__ == '__main__':
    if len(sys.argv)>1:
        filename = sys.argv[1]
    else:
        filename = 'board.jpg'

    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    if img==None:
        print "cannot open ",filename
        sys.exit(1)

    img_height, img_width = img.shape[0:2]

    # 本流の処理
    # img = cv2.medianBlur(img,5)
    img = cv2.GaussianBlur(img,
                           (5,5),  # param
                           0       # param
    )

    circles = cv2.HoughCircles(  # 返り値には確度の大きいもの順に入ってるらしい
        img, cv2.cv.CV_HOUGH_GRADIENT,
        dp=1,
        minDist=1,
        # minDist=int(min(img_width, img_height) * 0.2),
        param1=85, param2=40,
        minRadius=int(min(img_width, img_height) * 0.2),  # なるべく大きく欲しい王冠写してよ
        maxRadius=int(min(img_width, img_height) * 0.6),  # 画像はみ出す円はいらない
    )
    circles = np.uint16(np.around(circles))

    max_candidates = 5
    i_candidate = 0
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    for x, y, r in circles[0,:]:
        # 画像をはみ出す円はいらない
        # if x - r < 0 or x + r > img_width or y - r < 0 or y + r > img_height:
        #     continue

        # 写真中心に近い円だけが欲しい
        img_center_x, img_center_y = (img_width / 2, img_height / 2)
        threshold_r = min(img_width, img_height) * 0.2
        if (x - img_center_x) ** 2 + (y - img_center_y) ** 2 > threshold_r ** 2:
            continue

        rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
        cv2.circle(cimg,(x, y), r, rgb, 1)   # draw the outer circle
        cv2.putText(cimg, str(i_candidate), (x, y), cv2.FONT_HERSHEY_PLAIN, fontScale=2.0, color=rgb)
        # cv2.circle(cimg,(x, y), 2, (0, 255, 0), 3) # draw the center of the circle
        i_candidate += 1
        if i_candidate == max_candidates:
            break

    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
