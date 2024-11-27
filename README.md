This is a project created by Nareg Koshanian and Jacob Nowack.

Our goal is to create and implement a cop detection model on live footage through a dashcam.

In the current version of this repo as of 11/27/24 you will find the following:
CopCars.v2i.yolov11; a directory containing our dataset
newPictures; a directory containing a few images the model has never seen (for further testing purposes)
metrics.txt; displays the metrics I got after training for 100 epochs using train.py on a NVIDIA 1650 Super
test.py; python script that loops through newPictures and displays results
train.py: python script used to train the model
yolo11n.pt: yolo11's nano model which was the base of our current model
