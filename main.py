
import cv2 as cv 
import pyautogui
import numpy as np 
import matplotlib.pyplot as plt 
from time import time 
from PIL import ImageGrab
from windowCapture import window_capture
import screeninfo

monitors = screeninfo.get_monitors()


wincap = window_capture('Maplestory')



loop_time = time()



while True:    
    frame = wincap.screenshot()
    # Display the resulting frame
    cv.imshow('Computer Vision', frame)
    #Let calculate the While loop time To load this frame
    print('FPS {}'.format( 1 / (time() - loop_time)))
    loop_time = time()
    # Break the loop when 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break    

window_capture()










