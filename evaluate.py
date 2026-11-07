from ultralytics import YOLO

MODEL_PATH = "runs/detect/train/weights/best.pt"  # or runs/segment/train/weights/best.pt
DATA_CONFIG = "config.yaml"                        # or config_seg.yaml

model = YOLO(MODEL_PATH)
metrics = model.val(data=DATA_CONFIG)

precision = metrics.box.mp        # mean precision across classes
recall = metrics.box.mr           # mean recall across classes
map50 = metrics.box.map50         # mAP at IoU=0.5
map50_95 = metrics.box.map        # mAP averaged over IoU=0.5:0.95
f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0

print("===== Evaluation Results =====")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1-score  : {f1:.4f}")
print(f"mAP@0.5   : {map50:.4f}")
print(f"mAP@0.5:0.95 : {map50_95:.4f}")
print("===============================")
print("Full per-class breakdown, PR curve, and confusion matrix saved under runs/detect/val/")