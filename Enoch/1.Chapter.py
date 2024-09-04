# 이미지 불러오기
# import cv2
# img = cv2.imread("data/lena.png")
# cv2.imshow("Output",img)
# cv2.waitKey(0)

# 동영상 불러오기
# import cv2
# frameWidth =640 # 동영상 창 크기 설정(가로 사이즈)
# frameHeight = 480 # 동영상 창크기 설정(세로 사이즈)
# cap = cv2.VideoCapture("data/test.mp4")
#
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img,(frameWidth,frameHeight))
#     cv2.imshow("Video",img)
#     if cv2.waitKey(50) & 0xFF == ord('q'): #영상이 실행중에 'q'를 누르면
#         # waitKey(1) -> 0.001초
#         # 0xFF 아스키 키값
#         break # 종료하겠습니다.

# 웹캠 불러오기
# webcam: 0 , 내장카메라: 1
import cv2
frameWidth =640 # 동영상 창 크기 설정(가로 사이즈)
frameHeight = 480 # 동영상 창크기 설정(세로 사이즈)

cap = cv2.VideoCapture(0)
# 동영상이나 웹캠이 정상적으로 열리지 않았을때
if not cap.isOpened():
    print('Error: Cannot open Camera!!')
    exit()

while True:
    success,img = cap.read()
    if not success:
        print("영상을 불러오는데 실패했습니다.")
        break
    img = cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


 # 루프를 종료할 때 사용한 리소스를 정리해 주세요.
cap.release()
cv2.destroyAllWindows()