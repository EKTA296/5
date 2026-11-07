from ultralytics import YOLO

# Load lightweight YOLO model (fast for your laptop)
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data="config.yaml",   # path to your dataset config
    epochs=10,            # keep small for CPU
    imgsz=640,            # good balance speed + accuracy
    batch=4,              # small batch for your system
    workers=0             # prevents lag/crash on CPU
)

print("✅ Training Completed!")               
  