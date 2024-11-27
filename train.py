from ultralytics import YOLO

# Load yolo11 nano model 
model = YOLO("yolo11n.pt")

'''
Start training, args explained:
imgsz set to 640 to match training data
batch set to 8 to avoid memory overflow and it worked better than 16
epochs set to 100 like default
workers set to 0 to avoid freezing error
device set to 0 to use cuda and train on gpu
amp set to false to improve stability in performance especially since it performed worse when on
'''
model.train(data = "CopCars.v2i.yolov11\data.yaml", imgsz = 640, batch = 8, epochs = 100, workers = 0, device = 0, amp = False)