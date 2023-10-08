

import math 
import numpy


class state:
    ''' 
    Transforming a YOLOv8 screenshot into a state for a Deep Q-Network (DQN). 

    '''
    def __init__(self):
        self.State = []
        #self.total_npc_nearby = []
        #self.charc_pos = charc_pos
        #self.memory_monk_pos = memory_monk_pos 
        #self.yellow_dot_pos = yellow_dot_pos
        #self.green_circle_pos = green_circle_pos

    def state(self,charc_pos,eye_of_time_pos,memory_monk_pos,yellow_dot_pos, green_circle_pos):
        self.green_circle_pos = green_circle_pos
        self.all_npc_pos = []
        self.yellow_dot_pos = yellow_dot_pos
        self.charc_pos = charc_pos
        self.npc_pos = eye_of_time_pos + memory_monk_pos
       # print('total npc :', self.npc_pos)
        threshold_distance = 450 
        self.most_npc_on_top = 0
        self.most_npc_on_bottom = 0
        self.most_npc_on_right = 0
        self.most_npc_on_left = 0


        min_npc_threshold  = 2


        if len(self.charc_pos) > 0: 
            for vector in self.npc_pos:
                x1 = self.charc_pos[0][0]
                y1 = self.charc_pos[0][1]
                x2 = vector[0]
                y2 = vector[1]
                #print('y2',y2,'y1',y1)
                magnitude = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                if magnitude <= threshold_distance: 
                    #self.all_npc_pos.append(magnitude)
                    if y2 < y1 and y2 <= 80 and y2>=60:
                        self.most_npc_on_top += 1
                        
                    elif y1 > y2 and y2 >= 490: 
                        self.most_npc_on_bottom += 1
                           
                    if x2 > x1 and y2 > y1 - 120:
                        self.most_npc_on_right += 1 
                       
                    elif x2 < x1 and y2 > y1 - 120:
                        self.most_npc_on_left += 1
                    

        min_npc_threshold = max(self.most_npc_on_top,self.most_npc_on_bottom,self.most_npc_on_left,self.most_npc_on_right)   
        #print('min_npc_threshold:', min_npc_threshold)           

        if len(self.yellow_dot_pos) > 0 and min_npc_threshold != 0 : 
            if self.most_npc_on_top >= min_npc_threshold:
               # print('npc on top')
                self.State.append(((0, 0), (self.yellow_dot_pos[0]),self.green_circle_pos[0], self.green_circle_pos[1], self.green_circle_pos[2]))
            if self.most_npc_on_bottom >= min_npc_threshold:
                #print('npc on bottom')
                self.State.append(((1, 0), (self.yellow_dot_pos[0]), self.green_circle_pos[0], self.green_circle_pos[1], self.green_circle_pos[2]))
            if self.most_npc_on_right >= min_npc_threshold:
                #print('npc on right')
                self.State.append(((3, 0), (self.yellow_dot_pos[0]), self.green_circle_pos[0], self.green_circle_pos[1], self.green_circle_pos[2]))
            if self.most_npc_on_left >= min_npc_threshold:
               # print('npc on left')
                self.State.append(((4, 0), (self.yellow_dot_pos[0]), self.green_circle_pos[0], self.green_circle_pos[1], self.green_circle_pos[2]))

        
        return self.State
            


                   
        

                    

        

                



