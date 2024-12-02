import cv2
import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit
import tensorrt as trt

# TensorRT 모델 로딩
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)

# TensorRT 엔진 로드
def load_trt_model(model_path):
    with open(model_path, "rb") as f:
        runtime = trt.Runtime(TRT_LOGGER)
        engine = runtime.deserialize_cuda_engine(f.read())
        if engine is None:
            print("Failed to load the TensorRT engine.")
            return None
        print("TensorRT engine loaded successfully.")
        return engine

# TensorRT 모델 추론을 위한 데이터 준비
def prepare_input(frame, input_shape):
    # 이미지 전처리 (BGR -> RGB, 크기 조정, 정규화)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
    image = cv2.resize(image, (input_shape[2], input_shape[3]))  # (C, H, W) 순서로 크기 맞추기
    image = np.asarray(image, dtype=np.float32)
    image /= 255.0  # 정규화

    # 배치 차원 추가 (batch_size, channels, height, width)
    image = np.expand_dims(image, axis=0)
    return image

# TensorRT 모델로 추론 실행
def infer(engine, image):
    # 모델의 입력 크기 확인
    input_shape = (1, 3, 224, 224)  # 모델이 예상하는 입력 크기 (배치 크기, 채널 수, 높이, 너비)
    output_shape = (1, 1000)  # 예시로 1000개의 클래스 (모델에 따라 다를 수 있음)

    # GPU 메모리 할당
    input_buffer = cuda.mem_alloc(image.nbytes)
    output_buffer = cuda.mem_alloc(output_shape[0] * output_shape[1] * np.float32().itemsize)

    # 입력 데이터 GPU로 복사
    cuda.memcpy_htod(input_buffer, image.ravel())

    # 실행 컨텍스트 생성
    context = engine.create_execution_context()

    # 바인딩을 위한 메모리 리스트 준비
    bindings = [int(input_buffer), int(output_buffer)]

    # 실행 스트림 준비
    stream = cuda.Stream()

    # 추론 실행
    context.execute_v2(bindings)

    # 결과를 CPU로 복사
    output = np.empty(output_shape, dtype=np.float32)
    cuda.memcpy_dtoh(output, output_buffer)

    # 가장 확률이 높은 클래스를 출력
    predicted_class = np.argmax(output)
    return predicted_class, output

# 메인 코드
def main():
    # TensorRT 모델 로드
    model_path = "model.trt"  # .trt 모델 파일 경로
    engine = load_trt_model(model_path)
    if engine is None:
        return

    # 웹캠 캡처 시작
    cap = cv2.VideoCapture(0)  # 기본 웹캠 (ID: 0)
    if not cap.isOpened():
        print("Webcam not found.")
        return

    # 모델의 입력 크기 설정 (예: 224x224x3)
    input_shape = (1, 3, 224, 224)  # 모델이 요구하는 입력 크기

    while True:
        # 웹캠에서 프레임 캡처
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # 이미지 전처리 및 모델 입력 준비
        image = prepare_input(frame, input_shape)

        # TensorRT 모델로 추론
        predicted_class, output = infer(engine, image)

        # 추론 결과 출력
        print(f"Predicted class: {predicted_class}")

        # 웹캠 영상 출력
        cv2.putText(frame, f"Predicted class: {predicted_class}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Webcam Feed', frame)

        # 'q' 키를 눌러 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
