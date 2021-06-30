import cv2
import numpy as np

## main function

def dodgeV2(image, mask):
    return cv2.divide(image, 255-mask, scale=256)

## read image

imgpath = ''
img = cv2.imread('imagefilename.filetype')

## detect edges

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_inv = 255 - gray
img_blur = cv2.GaussianBlur(gray_inv, ksize=(25, 25),sigmaX=0, sigmaY=0)
img_blend = dodgeV2(gray, img_blur)
img_blend *= 12

## save image
  
outpath = ''
cv2.imwrite('newimagefilename.filetype',img_blend)
