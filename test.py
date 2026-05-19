from ultralytics import YOLO

model = YOLO("yolov8m_custom.pt")

model.predict(
    source=0,
    show=True,
    conf=0.5,
    imgsz=640,
    device=0,  
    half=True
)