import cv2 as cv 
import numpy as np 
import os 
import time 
from collections import deque
import math




class ImageMatching():
    def __init__(self, screenshot_obj,threshold):
        self.threshold = threshold
        self.main_image = cv.imread(screenshot_obj)

    #overthinking it continue tmr. 
    def template_matching(self,template_images):
        empty_dictionary = {} 
        position_dictionary = {}    # Only want position for tomeless and all the npc position. Then we calculate the distance formula from this    
        replay_buffer = deque(maxlen=2000) 
        replay_buffer_me  = deque(maxlen=2000) 
        for img in template_images: 
            name = (os.path.basename(img))
            # Convert the main image to grayscale
            main_gray = cv.cvtColor(self.main_image, cv.COLOR_BGR2GRAY)
            template_image = cv.imread(img) 
            # Convert the template image to grayscale
            template_gray = cv.cvtColor(template_image, cv.COLOR_BGR2GRAY) 
            #Matching
            result = cv.matchTemplate(main_gray, template_gray, cv.TM_CCOEFF_NORMED)  
            # Find all matches above the threshold
            loc = np.where(result >= self.threshold)   
            #empty_dictionary = {}   
            if img not in template_image: 
                empty_dictionary[name] = 0 

            count = 0 
            for pt in list(zip(*loc[::-1])):
                bottom_right = (pt[0] + template_image.shape[1], pt[1] + template_image.shape[0])
                cv.rectangle(self.main_image, pt, bottom_right, (0, 255, 0), 2)
                cv.putText(self.main_image, "Skill", (pt[0], pt[1] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 250, 0), 2)  
                count +=1 
                empty_dictionary[name] = count 
                


                #Asset\Temple Of Time\Memory_Monk_R.PNG

                #Asset\Hero_Skills\player_username.PNG
                if name == 'player_username.PNG':
                    position_dictionary[name] = [pt[0],pt[1]] 
                    replay_buffer_me.append(position_dictionary[name])

                if name == 'npc.PNG':
                    position_dictionary[name] = [pt[0],pt[1]] 
                    replay_buffer.append(position_dictionary[name])
                

                magnitudes = []

                #print(replay_buffer_me,replay_buffer)  

                left_or_right = []
                for vector1 in replay_buffer_me:
                    for vector2 in replay_buffer:
                        magnitude = math.sqrt((vector2[0] - vector1[0]) ** 2 + (vector2[1] - vector1[1]) ** 2)
                        magnitudes.append(magnitude) 

                        if vector2[0] < vector1[0]: 
                            left_or_right.append(0) # if the npc is on our left
                        elif vector2[0] > vector1[0]: 
                            left_or_right.append(1) # if the npc is on our left
                                     
                print(left_or_right)

                print("Magnitudes:", magnitudes)
                    
        # Display the resulting frame
        cv.imshow('Computer Vision', self.main_image)

        # Remove the main_image.png file 

        time.sleep(0.00001)
        os.remove('main_image.png') 

        return empty_dictionary 



  
            

        