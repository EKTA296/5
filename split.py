import os
import random
import shutil

# Your paths
images_path = r"C:\Users\HP\microplastic_ai_dataset\images"
labels_path = r"C:\Users\HP\microplastic_ai_dataset\labels"

train_img = r"C:\Users\HP\microplastic_ai_dataset\images\train"
val_img   = r"C:\Users\HP\microplastic_ai_dataset\images\val"

train_lbl = r"C:\Users\HP\microplastic_ai_dataset\labels\train"
val_lbl   = r"C:\Users\HP\microplastic_ai_dataset\labels\val"

# Create folders if not exist
os.makedirs(train_img, exist_ok=True)
os.makedirs(val_img, exist_ok=True)
os.makedirs(train_lbl, exist_ok=True)
os.makedirs(val_lbl, exist_ok=True)

# Get all images
images = [f for f in os.listdir(images_path) if f.endswith(('.jpg', '.png'))]

# Shuffle
random.shuffle(images)

# Split 80-20
split = int(0.8 * len(images))
train_files = images[:split]
val_files = images[split:]

# Move files
for file in train_files:
    shutil.move(os.path.join(images_path, file), os.path.join(train_img, file))
    
    label_file = file.rsplit('.', 1)[0] + ".txt"
    shutil.move(os.path.join(labels_path, label_file), os.path.join(train_lbl, label_file))

for file in val_files:
    shutil.move(os.path.join(images_path, file), os.path.join(val_img, file))
    
    label_file = file.rsplit('.', 1)[0] + ".txt"
    shutil.move(os.path.join(labels_path, label_file), os.path.join(val_lbl, label_file))

print("✅ Dataset split completed successfully!")