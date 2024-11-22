from ultralytics import YOLO
import cv2

# Load a YOLO model
model = YOLO("best.pt")  # Replace with your model path

# Open webcam stream
cap = cv2.VideoCapture(0)  # Change to video file path if needed

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model.predict(source=frame, show=False)  # Inference on the frame

    # Annotate the frame with results
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLO Detection", annotated_frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
