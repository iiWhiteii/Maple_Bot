import cv2 as cv
import os
from time import time
from windowCapture import window_capture
import numpy as np




# This is an instance of the window_capture class
wincap = window_capture('Maplestory')

from template_matching import ImageMatching


template_images = ['Memory_Monk_1.PNG','Memory_Monk_3.PNG','ME.PNG','ME2.PNG','ME3.PNG','ME4.PNG']




loop_time = time()
while True:
    frame = wincap.screenshot()
    cv.imwrite('main_image.png',frame)
    image_match = ImageMatching('main_image.png', template_images, 0.45)
    image_match.template_matching()


    # Calculate the frame rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # Break the loop when 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
