import sys
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Signal
from ui_main import Ui_MainWindow  # PySide6로 생성된 GUI 파일 import
from ultralytics import YOLO

# YOLO 모델 로드
model = YOLO("best.engine")

class WebcamThread(QThread):
    # 프레임 업데이트 신호
    frame_updated = Signal(QImage, int, int)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        # 웹캠 초기화
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("웹캠을 열 수 없습니다!")
            return

        while self.running:
            ret, frame = cap.read()
            if not ret:
                print("프레임을 읽을 수 없습니다!")
                break

            # YOLO 감지 수행
            results = model(frame)
            annotated_frame = results[0].plot()  # YOLO 감지 결과

            head = 0
            helmet = 0
            for box in results[0].boxes:
                if box.cls[0] == 0:
                    head += 1
                elif box.cls[0] == 1:
                    helmet += 1

            # print("helmet: ",helmet,"   head: ",head)

            # OpenCV 프레임을 Qt 이미지로 변환
            rgb_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            qt_image = QImage(
                rgb_frame.data,
                rgb_frame.shape[1],
                rgb_frame.shape[0],
                QImage.Format_RGB888
            )

            # 신호를 통해 업데이트
            self.frame_updated.emit(qt_image, helmet, head)

        cap.release()

    def stop(self):
        self.running = False
        self.wait()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 웹캠 스레드 시작
        self.webcam_thread = WebcamThread()
        self.webcam_thread.frame_updated.connect(self.update_webcam)
        self.webcam_thread.start()

    def update_webcam(self, image, helmet, head):
        # QLabel에 웹캠 프레임 표시
        self.ui.webcam_label.setPixmap(QPixmap.fromImage(image))
        self.ui.helmet_count.setText(str(helmet))
        self.ui.head_count.setText(str(head))

        if head > 0 :
            self.ui.warning_label.setText("Ensure safety helmet!")
            self.ui.warning_label.setStyleSheet("color:red")
        else:
            self.ui.warning_label.setText("Good!")
            self.ui.warning_label.setStyleSheet("color:black")

    def closeEvent(self, event):
        # 창 닫을 때 스레드 정리
        self.webcam_thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
