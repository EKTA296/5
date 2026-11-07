from ultralytics import YOLO

# yolov8n-seg.pt is the segmentation variant (bbox model won't do masks)
model = YOLO("yolov8n-seg.pt")

model.train(
    data="config_seg.yaml",   # must point to polygon-labeled data, not box labels
    epochs=50,                # segmentation needs more epochs than detection to converge
    imgsz=640,
    batch=4,
    workers=0,
)

print("✅ Segmentation training completed! Weights at runs/segment/train/weights/best.pt")