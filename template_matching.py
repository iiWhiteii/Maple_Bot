


import cv2 as cv 
import numpy as np 
import os 




class image_matching(): 
    def __init__(self,screenshot_obj,template_images): 
        self.threshold = 0.50
        self.main_image = cv.imread(screenshot_obj) 
        self.template_image = cv.imread(template_images)

    def template_matching(self):
        #Convert both images to grayscale
        main_gray = cv.cvtColor(self.main_image, cv.COLOR_BGR2GRAY)
        template_gray = cv.cvtColor(self.template_image, cv.COLOR_BGR2GRAY)

        #Perform template matching
        result = cv.matchTemplate(main_gray, template_gray, cv.TM_CCOEFF_NORMED)
        # Find all matches above the threshold
        loc = np.where(result >= self.threshold)  

        # Iterate over all matches and draw rectangles
        for pt in zip(*loc[::-1]):
            bottom_right = (pt[0] + self.template_image.shape[1], pt[1] + self.template_image.shape[0])
            cv.rectangle(self.main_image, pt, bottom_right, (0, 255, 0), 2)
        
        #Display the resulting frame
        cv.imshow('Computer Vision', self.main_image) 

        #Remove the main_image.png file
        os.remove('main_image.png')


  
            

        