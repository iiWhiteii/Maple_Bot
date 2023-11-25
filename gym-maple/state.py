

import math 
import numpy as np


class state:
    ''' 
    Transforming a YOLOv8 screenshot into a state for a Deep Q-Network (DQN). 

    '''
    def __init__(self):
        self.State = np.array([])
        

    def state(self,Player_Coordinates,Eye_of_Time_Coordinates, Memory_Monk_Coordinates,Minimap_Charc_Coordinates, GC_MINIMAP_Coordinates):
        self.GC_MINIMAP_Coordinates = GC_MINIMAP_Coordinates
        self.Minimap_Charc_Coordinates = Minimap_Charc_Coordinates
        print(self.Minimap_Charc_Coordinates)
        self.Player_Coordinates = Player_Coordinates
        self.NPC_Coordinates = Eye_of_Time_Coordinates + Memory_Monk_Coordinates


        
        
        self.all_npc_pos = []
        
        
        
        threshold_distance = 800
        
        
        #These variables represent the state for the agent to be trained using DQN
        #Indicate the number of non-player characters (NPCs) in different directions
        # from the agent's perspective.
        self.most_npc_on_top = 0
        self.most_npc_on_bottom = 0
        self.most_npc_on_right = 0
        self.most_npc_on_left = 0
        self.min_npc_threshold  = 1


        if len(self.Player_Coordinates) > 0: # if computer vision detect our character exists  
            for vector in self.NPC_Coordinates:
                # Represent Player_Coordinates
                x1 = self.Player_Coordinates[0][0]
                y1 = self.Player_Coordinates[0][1]
                # Represent NPC_Coordinates 
                x2 = vector[0]
                y2 = vector[1]
                magnitude = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                if magnitude <= threshold_distance: 
                    #self.all_npc_pos.append(magnitude)
                    if y2 < y1 and y2 <= 80 and y2>=60:
                        self.most_npc_on_top += 1
                        
                    if y1 > y2 and y2 >= 490: 
                        self.most_npc_on_bottom += 1
                           
                    if x2 > x1 and y2 > y1 - 120:
                        self.most_npc_on_right += 1 
                       
                    if x2 < x1 and y2 > y1 - 120:
                        self.most_npc_on_left += 1
                    
       

        if len(self.Minimap_Charc_Coordinates) > 0: 
            print(len(self.Minimap_Charc_Coordinates))
            ''' -1: No NPCs around ''' 
            self.State = np.array([-1, self.Minimap_Charc_Coordinates[0][0], Minimap_Charc_Coordinates[0][1]])

            if self.most_npc_on_top >= self.min_npc_threshold :
                #0: Most NPCs on top
                self.State = np.array(([0, self.Minimap_Charc_Coordinates[0][0], Minimap_Charc_Coordinates[0][1]]))
                #1: Most NPCs on bottom
            elif self.most_npc_on_bottom >= self.min_npc_threshold :
                self.State = np.array(([1, self.Minimap_Charc_Coordinates[0][0], Minimap_Charc_Coordinates[0][1]]))
                #2: Most NPCs on right
            elif self.most_npc_on_right >= self.min_npc_threshold:
                self.State = np.array(([2, self.Minimap_Charc_Coordinates[0][0], Minimap_Charc_Coordinates[0][1]]))
                #3: Most NPCs on left
            elif self.most_npc_on_left >= self.min_npc_threshold:
                self.State = np.array(([3, self.Minimap_Charc_Coordinates[0][0], Minimap_Charc_Coordinates[0][1]]))





        return self.State
            


                   
        

                    

        

                



