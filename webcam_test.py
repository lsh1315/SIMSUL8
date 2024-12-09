import cv2
from ultralytics import YOLO

# TensorRT 모델 로드
model = YOLO("best.pt")  # TensorRT 모델 경로

# 웹캠 초기화
cap = cv2.VideoCapture(0)  # 0번 카메라 (웹캠)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다!")
    exit()

temp = 0

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다!")
        break

    # YOLO 감지 수행
    results = model(frame)  # 프레임을 YOLO 모델에 전달

    # 감지 결과 그리기
    annotated_frame = results[0].plot()  # 결과를 플롯하여 주석 추가

    # 화면에 출력
    cv2.imshow("TensorRT Real-Time Detection", annotated_frame)
    

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()