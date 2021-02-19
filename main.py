import gym 
import math
import random
import numpy as np
import matplotlib
import cv2
import time
import torch
import torch.nn as nn

import models.train as train

#set up pytorch
if torch.cuda.is_available():
    device = torch.device("cuda:0")
else:
    device = torch.device("cpu")

print(device)


#read in images from opencv 
camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(0.1)
return_value, image = camera.read()
cv2.imwrite("data/opencv.png", image)
del(camera)

t = train.trained_network()
t.drive_network()
t.set_model_input()








