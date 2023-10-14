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
        
         
        
        self.class_label = []
        self.player_coordinates = []
        self.eye_of_time_pos = [] 
        self.eye_of_time_death_pos = [] 
        self.memory_monk_coordinates = []  
        self.memory_monk_death_coordinates = [] 
        self.yellow_dot_pos = []

        self.label_counter = {}


        # Drawing green circle
       
        self.green_circle_coordinates = [(115, 80),(35,80),(75,80),(115, 125),(35,125),(75,125)]
        for (x, y) in self.green_circle_coordinates:

            """ green circle have an radius of 19"""

            cv.circle(self.screenshot, (x, y), 19, (0, 255, 0,1000))
            
        
        
        for data in self.detected_object.boxes.data.tolist():
            
            self.screenshot = cv.rectangle(screenshot, (int(data[0]), int(data[1])), (int(data[2]),int(data[3])), (0, 255, 0), 2)    
            
            
            
            self.class_id = int(data[5])  

            if self.class_id == 0: 
                self.center_x = (int(data[0]) + int(data[2])) // 2
                self.center_y = (int(data[1]) + int(data[3])) // 2
                self.player_coordinates.append((self.center_x, self.center_y ))  
                cv.circle(self.screenshot, (self.center_x, self.center_y), radius=2, color=(0, 0, 255), thickness=-1)

            elif self.class_id == 1: 
                
                self.center_x = (int(data[0]) + int(data[2])) // 2
                self.center_y = (int(data[1]) + int(data[3])) // 2
                
                self.eye_of_time_pos.append(( self.center_x, self.center_y ))
                
                cv.circle(self.screenshot, (self.center_x, self.center_y), radius=2, color=(0, 0, 255), thickness=-1)

            elif self.class_id == 2:
                self.center_x = (int(data[0]) + int(data[2])) // 2
                self.center_y = (int(data[1]) + int(data[3])) // 2
                
                
                self.eye_of_time_death_pos.append(( self.center_x, self.center_y ))
                
                cv.circle(self.screenshot, (self.center_x, self.center_y), radius=2, color=(0, 0, 255), thickness=-1)

            elif self.class_id == 3:
                self.center_x = (int(data[0]) + int(data[2])) // 2
                self.center_y = (int(data[1]) + int(data[3])) // 2
                self.memory_monk_coordinates.append(( self.center_x, self.center_y ))
                cv.circle(self.screenshot, (self.center_x, self.center_y), radius=2, color=(0, 0, 255), thickness=-1)
        
            elif self.class_id == 4: 

                self.center_x = (int(data[0]) + int(data[2])) // 2
                self.center_y = (int(data[1]) + int(data[3])) // 2 


                self.memory_monk_death_coordinates.append(( self.center_x, self.center_y ))
                
                cv.circle(self.screenshot, (self.center_x, self.center_y), radius=2, color=(0, 0, 255), thickness=-1)

            elif self.class_id == 5:
                
                self.center_x = (int(data[0]) + int(data[2])) // 2
                self.center_y = (int(data[1]) + int(data[3])) // 2

                
                self.yellow_dot_pos.append((self.center_x,  self.center_y  ))
                
                cv.circle(self.screenshot, (self.center_x, self.center_y), radius=2, color=(0, 0, 255), thickness=-1)

            self.data = data
            

            if self.class_id not in self.label_counter:
                self.label_counter[self.class_id] = 1
            else:
                self.label_counter[self.class_id] += 1   

       

        return self.screenshot, self.player_coordinates,self.eye_of_time_pos, self.eye_of_time_death_pos, self.memory_monk_coordinates,self.memory_monk_death_coordinates,self.yellow_dot_pos, self.green_circle_coordinates

    
    # I want to detect object position etc

    #def




