import cv2
import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit
import tensorrt as trt

# TensorRT 모델 로딩
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)
with open("model.trt", "rb") as f:
    runtime = trt.Runtime(TRT_LOGGER)
    engine = runtime.deserialize_cuda_engine(f.read())

# 웹캠 캡처
cap = cv2.VideoCapture(0)  # 웹캠 ID는 0 (기본 카메라)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 이미지 전처리 (예: 크기 조정 및 색상 변경)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    image = np.asarray(image, dtype=np.float32)
    image = np.expand_dims(image, axis=0)

    # TensorRT 모델 inference 수행
    bindings = []
    stream = cuda.Stream()
    # input/output 버퍼를 위한 메모리 할당
    # 이 부분은 모델의 input/output 형태에 맞춰 수정해야 합니다.
    
    # inference 실행 (TensorRT 엔진을 사용하여)
    # 결과 출력 및 후처리 (필요한 후처리 작업)
    
    # 결과 화면에 출력
    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q'를 눌러 종료
        break

cap.release()
cv2.destroyAllWindows()
