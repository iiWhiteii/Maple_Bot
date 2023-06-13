import cv2 as cv
import os
from time import time
from windowCapture import window_capture
import numpy as np




# This is an instance of the window_capture class
wincap = window_capture('Maplestory')

from template_matching import image_matching





loop_time = time()
while True:
    # Capture the frame
    frame = wincap.screenshot() 
    cv.imwrite('main_image.png',frame)
    image_match = image_matching('main_image.png','Memory_Monk_2.PNG')
    image_match.template_matching()


    # Calculate the frame rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # Break the loop when 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
