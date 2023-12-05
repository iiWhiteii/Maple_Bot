from ultralytics import YOLO 
import cv2 as cv
import time
from collections import deque



class model:
    def __init__(self,weight_path):
        self.pretain_weight_path = weight_path 
        self.model = self.yolov8_model()
        
    
    def yolov8_model(self):
        self.yolov8 = YOLO(self.pretain_weight_path)        
        return self.yolov8 
    

    def detection(self,screenshot): 
        self.screenshot = screenshot
        self.detected_object = self.yolov8(self.screenshot)[0] 
        
         
        self.class_label = deque(maxlen=50)
        self.player_coordinates = deque(maxlen=50)
        self.eye_of_time_pos = deque(maxlen=50)
        self.eye_of_time_death_pos = deque(maxlen=50)
        self.memory_monk_coordinates = deque(maxlen=50)
        self.memory_monk_death_coordinates = deque(maxlen=50)
        self.yellow_dot_pos = deque(maxlen=50)





        
        self.label_counter = {}


        # Drawing area
       
        self.area = [(115,72),(135,72),(135, 88),(15,88),(75,88), (45,88), (105,88) , (135, 115),(15,115), (15,135), (75,135), (45,135), (105,135), (135,135)]
        for (x, y) in self.area:

            """ green circle have an radius of 19"""

            cv.circle(self.screenshot, (x, y), 12, (0, 255, 0,1000))
            
        
        
















        #this for something else
        for data in self.detected_object.boxes.data.tolist():
            self.screenshot = cv.rectangle(screenshot, (int(data[0]), int(data[1])), (int(data[2]),int(data[3])), (0, 255, 0), 2)    
            self.class_id = int(data[5])  
            if self.class_id == 0: 
                self.center_x = (int(data[0]) + int(data[2])) // 2
                self.center_y = (int(data[1]) + int(data[3])) // 2
                self.player_coordinates.append((self.center_x, self.center_y ))  
                cv.circle(self.screenshot, (self.center_x, self.center_y), radius=3, color=(0, 0, 255), thickness=-1)

            elif self.class_id == 1: 
                self.center_x = (int(data[0]) + int(data[2])) // 2
                self.center_y = (int(data[1]) + int(data[3])) // 2
                
                self.eye_of_time_pos.append(( self.center_x, self.center_y ))
                
                cv.circle(self.screenshot, (self.center_x, self.center_y), radius=3, color=(0, 0, 255), thickness=-1)

            elif self.class_id == 2:
                self.center_x = (int(data[0]) + int(data[2])) // 2
                self.center_y = (int(data[1]) + int(data[3])) // 2
                
                
                self.eye_of_time_death_pos.append(( self.center_x, self.center_y ))
                
                cv.circle(self.screenshot, (self.center_x, self.center_y), radius=3, color=(0, 0, 255), thickness=-1)

            elif self.class_id == 3:
                self.center_x = (int(data[0]) + int(data[2])) // 2
                self.center_y = (int(data[1]) + int(data[3])) // 2
                self.memory_monk_coordinates.append(( self.center_x, self.center_y ))
                cv.circle(self.screenshot, (self.center_x, self.center_y), radius=3, color=(0, 0, 255), thickness=-1)
        
            elif self.class_id == 4: 

                self.center_x = (int(data[0]) + int(data[2])) // 2
                self.center_y = (int(data[1]) + int(data[3])) // 2 


                self.memory_monk_death_coordinates.append(( self.center_x, self.center_y ))
                
                cv.circle(self.screenshot, (self.center_x, self.center_y), radius=3, color=(0, 0, 255), thickness=-1)

            elif self.class_id == 5:
                
                self.center_x = (int(data[0]) + int(data[2])) // 2
                self.center_y = (int(data[1]) + int(data[3])) // 2

                
                self.yellow_dot_pos.append((self.center_x,  self.center_y  ))
                
                cv.circle(self.screenshot, (self.center_x, self.center_y), radius=3, color=(0, 0, 255), thickness=-1)

















            self.data = data
            

            if self.class_id not in self.label_counter:
                self.label_counter[self.class_id] = 1
            else:
                self.label_counter[self.class_id] += 1   

       

        return self.screenshot, self.player_coordinates,self.eye_of_time_pos, self.eye_of_time_death_pos, self.memory_monk_coordinates,self.memory_monk_death_coordinates,self.yellow_dot_pos, self.area

    
  




