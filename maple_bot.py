
import cv2 as cv 
import pyautogui
import numpy as np 
import matplotlib.pyplot as plt 
from time import time 
from PIL import ImageGrab



import screeninfo

monitors = screeninfo.get_monitors()




import win32gui, win32ui, win32con



def window_capture(): 
    
    # our monitor size
    
    w =  

    h =  


    hwnd = win32gui.FindWindow(None, windowname)
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY) 


    # save the screenshot

    dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


loop_time = time()
while True:
    # Capture screen frame 
    #frame = ImageGrab.grab()
    

    frame = np.array(frame)
    # Convert the image to OpenCV format
    frame = cv.cvtColor(np.array(frame), cv.COLOR_RGB2BGR)

    # Display the resulting frame
    cv.imshow('Computer Vision', frame)

    #Let calculate the While loop time To load this frame
    print('FPS {}'.format( 1 / (time() - loop_time)))
    loop_time = time()


    # Break the loop when 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break









