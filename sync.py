import cv2
import ctypes
import os
from time import sleep

def screenshot():
    os.system('@echo off')
    os.system('del .screen.png')
    os.system('adb exec-out screencap -p > .screen.png')
    image = cv2.imread('.screen.png')
    if image is None:
        print("sorry, but .scren.png not found.")
        exit()
    return(image)

windowName='IMG'
img = screenshot()
imgHeight = int(img.shape[0]/3)
imgWidth = int(img.shape[1]/3)

def checksize(image):
    nowWidth = image.shape[1]
    nowHeight = image.shape[0]
    if nowWidth == imgWidth :
        return(0)#大小未變回傳0
    else:
        return(1)#大小未變回傳1

def setsize(image):
    if checksize(img)==1:
        imgHeight = image.shape[0]
        imgWidth = image.shape[1]

def mouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        x1 = str(x)
        y1 = str(y)
        command = "adb shell input tap "+x1+" "+y1
        print(command)
        os.system(command)



cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
cv2.resizeWindow(windowName, imgWidth, imgHeight)

while 1==1:
    img = screenshot()
    #print("c1")
    setsize(img)
    #print("c2")
    cv2.setMouseCallback(windowName, mouse)
    cv2.imshow(windowName, img)
    print(img.shape)
    cv2.waitKey(1)
