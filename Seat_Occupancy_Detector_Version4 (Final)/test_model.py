from ultralytics import YOLO

model = YOLO(r"C:\Seat\runs\detect\train-2\weights\best.pt")

model.predict(
    source="test_images",
    save=True,
    conf=0.55
)