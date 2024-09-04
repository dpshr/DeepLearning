import cv2

# 웹캠 객체 생성
cap= cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

while True:
    ref,frame = cap.read()
    if not ref:
        print("카메라 구동실패")
        break
    frame = cv2.flip(frame,1) #좌우반전, 상하반전
    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # 흑백으로 전환
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

 # 루프를 종료할 때 사용한 리소스를 정리해 주세요.
cap.release()
cv2.destroyAllWindows()