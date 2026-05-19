from ultralytics import YOLO

model = YOLO("yolov8m_custom.pt")

model.predict(source="1.mp4", show=True, conf=0.5, line_thickness=1)