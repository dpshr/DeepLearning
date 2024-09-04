import cv2
import os
try:
    cap = cv2.VideoCapture('capture/captured_video.mp4')
    print('영상을 실행합니다')
except:
    print('영상 로드 실패')


cap.set(3,480)
cap.set(4,320)
cnt = 0

folder_path = 'capture/'

while True:
    ret,frame = cap.read()

    if not ret:
        print('비디오 읽기 오류')
        cap.release()
        cv2.destroyAllWindows()
        break
    cv2.imshow('Video',frame)
    # 키 입력 대기시간
    k = cv2.waitKey(20)
    # ascii : 1 = 49, 2 = 50
    if k == 50: # 2번 누르면 캡쳐
        file_name = f"img{cnt}.png"
        # 이미지 저장 전체경로
        out_path = os.path.join(folder_path,file_name) # 폴더에 저장할 때
        # print('frame',frame)
        cv2.imwrite(out_path,frame,params=[cv2.IMWRITE_PNG_COMPRESSION,0])
        # cv2.imwrite('capture/'+f"img{cnt}.jpeg",frame,params=[cv2.IMWRITE_JPEG_QUALITY,90]) #  0~100
        # cv2.imwrite('capture/'+f"img{cnt}.png",frame,params=[cv2.IMWRITE_PNG_COMPRESSION,0]) #  0~9 기본:3
        cnt += 1
    if k == 49: # 1번 누르면 종료
        cap.release()
        cv2.destroyAllWindows()
        break
