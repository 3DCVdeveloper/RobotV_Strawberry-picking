import time
import cv2
from matplotlib import pyplot as plt
import numpy as np
from Arm7Bot_py.lib.Arm7Bot import Arm7Bot

arm = Arm7Bot('COM5')
file_path = "data.txt"

while(1):
    openfile = open(file_path)
    content = openfile.readlines()
    if len(content)==0:
        continue
    x = float(content[0].split(" ")[1])
    y = float(content[0].split(" ")[2])
    z = float(content[0].split(" ")[3])

    X = int(z) - 315
    Y = -int(x) + 12-
    Z = int(y) + 130


    openfile.close()
    file=open(file_path,'w+')
    file.close()

    if x==0 and y==0 and z==0:
        continue

    print("read", x, y, z)
    print("out", X, Y, Z)


    arm.setIK6([X, Y, Z], [0, 0, -1])
    time.sleep(2)
    arm.setIK6([X, Y, Z], [1, 1, 0])
    time.sleep(3)

    arm.setAngle(6, 18)  # close hand
    time.sleep(1)
    arm.setIK6([-170, 1, 100], [0, 0, -1])
    time.sleep(2)
    arm.setAngle(6, 90)  # open hand
    time.sleep(1)
    arm.setIK6([-170, 1, 180], [0, 0, -1])
    time.sleep(2)

    arm.setIK6([0, 200, 150], [0, 0, -1])
    time.sleep(2)

    x = 0
    y = 0
    z = 0
