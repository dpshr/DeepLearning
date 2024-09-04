import cv2

# 웹캠 객체 생성
cap= cv2.VideoCapture(0)
cnt = 0

while True:
    ref,frame = cap.read()
    if not ref:
        print("카메라 구동실패")
        break
    # f'img{cnt}.jpeg'
    # 's' 누르면 저장
    cv2.imshow("Webcam Capture",frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('capture/' + f"captured_img{cnt}.jpeg", frame, params=[cv2.IMWRITE_JPEG_QUALITY, 90])  # 0~100
        # cv2.imwrite(f'capture/captured_img{cnt}.jpeg',frame)
        cnt+=1
        print('프레임저장완료')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

 # 루프를 종료할 때 사용한 리소스를 정리해 주세요.
cap.release()
cv2.destroyAllWindows()