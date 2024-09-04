import cv2
import numpy
import numpy as np
# 이미지 가져오기
img = cv2.imread('data/lena.png')
# 5X5 크기의 1로 채워진 배열을 생성 (5X5필터생성)
kernel = np.ones((5,5),numpy.uint8) # unit8: 0~255까지 정수표현

# opencv는 RGB가 아닌 BGR  순서 (R:red, G: green, B:blue)-> (B,G,R)
# 이미지를 흑백(grascale)으로 3(BGR)채널(-> 1채널(Grayscale)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# 이미지 블러링()
# 커널사이즈: 블러링 처리할 크기(커널) 크기가 크면 더 흐림
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# 경계면(밝기가 급격하게 변하는 부분)

imgCanny = cv2.Canny(img,100,100)

#경계면 침식
imgDialation = cv2.dilate(imgCanny,kernel, iterations=1) # iterations 반복횟수가 커질수록 더욱 경계면이 커짐

# 경계면 수축
imgEroded = cv2.erode(imgDialation,kernel, iterations=1)

cv2.imshow("img",img)
cv2.imshow("gray",imgGray)
cv2.imshow("blur",imgBlur)
cv2.imshow("canny",imgCanny)
cv2.imshow("imgDialation",imgDialation)
cv2.imshow("imgEroded",imgEroded)
cv2.waitKey(0)

