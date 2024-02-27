from ultralytics import YOLO
import cv2

model = YOLO('./ml_model/final_korean_cam.pt')
model.predict(source="0", show=True, conf=0.5)

# Increase the frame rate by adjusting the waitKey value
while True:
    key = cv2.waitKey(1)  # Adjust the value (e.g., 10) to increase the frame rate
    
    # Break the loop if the 'q' key is pressed
    if key == ord('q'):
        break