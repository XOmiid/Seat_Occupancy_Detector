from ultralytics import YOLO

def main():

    model = YOLO("yolov8l.pt")

    model.train(
       data="Seat-Detection-4/data.yaml",
       epochs=75,
       imgsz=832,
       batch=8,
       device=0,

        
    )

if __name__ == "__main__":
    main()