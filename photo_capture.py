import serial
from vpython import *
import cv2
import os
import numpy as np
import shutil
import time

video=cv2.VideoCapture(0)

check,frame = video.read()
print(check)
print(frame)
cv2.imshow("Capturing",frame)
cv2.waitKey(0)
img_name="opencv_frame_{}.jpg".format(0)

cv2.imwrite(img_name,frame)

video.release()
cv2.destroyAllWindows()
