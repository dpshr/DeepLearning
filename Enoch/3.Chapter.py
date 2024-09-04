import cv2
import numpy as np

# img = cv2.imread("data/lambo.png")
img = cv2.imread("data/son.jpg")
# 크기 확인(세로,가로,채널수)
print(img.shape) # (462,623,3)


#이미지 리사이즈
imgResize = cv2.resize(img,(800,600))

# 특정위치 이미지 자르기
# crop은 opencv를 사용하지 않고 배열로 시작과 끝을 배열로 끝점 크기를 정해서 자르기만 하면 됨
imgCropped = img[100:201,100:250] # img[y:y2,x:x2] # 이미지 자르기

# img = cv2.imread("img",img)
print(imgResize.shape) # (200,300,3)
cv2.imshow("Output",img)
cv2.imshow("Resize",imgResize)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)

