from ultralytics import YOLO

def main():

    model = YOLO("yolov8l.pt")

    model.train(
       data="Seat-Detection-6/data.yaml",
       epochs=85,
       imgsz=832,
       batch=8,
       device=0,

        
    )

if __name__ == "__main__":
    main()