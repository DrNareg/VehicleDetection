import os
from ultralytics import YOLO
import cv2

# Path to the directory containing the images you want to test
# remove r if path doesn't include backslashes
image_dir = r"path/to/dir"

# Load the trained YOLO model
model = YOLO(r"path/to/best.pt")

# Iterate over all files in the directory
for image_name in os.listdir(image_dir):
    # Check if the file is an image (you can adjust the extensions as needed)
    if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        # Construct the full image path
        image_path = os.path.join(image_dir, image_name)

        # Read the image using OpenCV
        image = cv2.imread(image_path)

        # Run inference on the image
        results = model(image)

        # Display the results with predicted boxes
        results[0].show()  # This will show the image with bounding boxes and labels
