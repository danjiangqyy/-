import cv2
import numpy as np
import matplotlib.pyplot as plt



def _add(img1,img2):
    result=cv2.addWeighted(img1,0.2,img2,0.8,0)
    cv2.imshow('result',result)
    cv2.waitKey(0)


def _resize(img1,img2):
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)
    w,h=img1.shape[:2]

    resize_img2=cv2.resize(img2,(h,w))
    return resize_img2

def _compress(img1):
    img=cv2.imread(img1)
    cv2.imwrite(r'C:\Users\little\Desktop\mysave_1.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,0])
    cv2.imwrite(r'C:\Users\little\Desktop\mysave_2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])


if __name__ == '__main__':
    img1 = r'C:\Users\little\Desktop\1.png'
    img2 = r'C:\Users\little\Desktop\9.png'
    _compress(img1)
    # result_2=_resize(img1,img2)
    # result_1 = cv2.imread(img1)
    # _add(result_1,result_2)
