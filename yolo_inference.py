from ultralytics import YOLO
import os 
print(os.getcwd())
model = YOLO('yolov8s') 
results = model.predict(source = 'input_video/a.mp4', save=True)
print("Predictions saved at:", results[0])
for box in results[0].boxes:
    print(box)