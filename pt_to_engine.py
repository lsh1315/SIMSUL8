from ultralytics import YOLO
import cv2

model = YOLO("best.pt")

# model = YOLO("best.onnx")

model.export(format="engine")

tensorrt_model = YOLO("best.engine")

results = tensorrt_model("image.png")

annotated_frame = results[0].plot()

cv2.imshow("Detectiion Results", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()