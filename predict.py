
from pathlib import Path
from ultralytics import YOLO

# Project folder
project_dir = Path(r"C:\Users\HP\yolo_v8_project")

# Load your trained model
model_path = project_dir / "runs" / "detect" / "train" / "weights" / "best.pt"
model = YOLO(str(model_path))

def run_prediction(image_path=None):
    if image_path is None:
        return None

    image_path = Path(image_path)

    if not image_path.is_file():
        print(f"Image not found: {image_path}")
        return None

    results = model.predict(
        source=str(image_path),
        conf=0.25,
        save=True
    )
    return results

if __name__ == "__main__":
    # Replace this with the actual image path from your dataset
    image_path = r"C:\Users\HP\microplastic_ai_dataset\train\images\YOUR_IMAGE.jpg"

    results = run_prediction(image_path)

    if results is not None:
        print("Prediction completed!")
        print("Detected objects:", len(results[0].boxes))
        print("Annotated image saved in the runs/detect folder.")
