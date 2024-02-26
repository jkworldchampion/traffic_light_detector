from ultralytics import YOLO

# Load the model
model = YOLO("yolov8n.yaml")
print("hello")

# Use the model
results = model.train(data="D:/programming/book/traffic_light_detector/config.yaml", epochs=5) 