import os, shutil
from ultralytics import YOLO
import cv2

MODEL_PATH = "yolov8n.pt"
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"

def detect_objects():
    model = YOLO(MODEL_PATH)
    
    os.makedirs(OUTPUT_FOLDER) 
    if os.path.exists(OUTPUT_FOLDER):
        shutil.rmtree(OUTPUT_FOLDER)
        os.makedirs(OUTPUT_FOLDER)
    
    for image_name in os.listdir(INPUT_FOLDER):
        input_path = os.path.join(INPUT_FOLDER, image_name)
        output_path = os.path.join(OUTPUT_FOLDER, image_name)

        if not input_path.lower().endswith(('.png','.jpg','.jpeg')):
            continue

        results = model.predict(input_path, conf=0.5, save=False)

        
        for result in results:
            annotated_image = result.plot(result)
            cv2.imwrite(output_path, annotated_image)
            print(f"Haseil deteksi disimpan ke: {image_name}")
            # print(result)
            # exit()

if __name__== "__main__":
    detect_objects()