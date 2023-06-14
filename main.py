import cv2 as cv
import os
from time import time
from windowCapture import window_capture
import numpy as np




# This is an instance of the window_capture class


wincap = window_capture('Maplestory')

#window_capture.list_window_names()

from template_matching import ImageMatching


template_images = ['Memory_Monk_1.PNG','Memory_Monk_2.PNG','In_Game_Name.PNG','eye_of_time_looking_left.PNG','eye_of_time_looking_right.PNG']

loop_time = time()
while True:
    frame = wincap.screenshot()
    cv.imwrite('main_image.png',frame)
    image_match = ImageMatching('main_image.png', template_images, 0.70)
    image_match.template_matching()

    #cv.imshow('Computer Vision', frame)

    # Calculate the frame rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # Break the loop when 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
