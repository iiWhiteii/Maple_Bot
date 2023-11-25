import gym
from gym import spaces
from time import time
import numpy as np
import math


class MapleEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.observation_space = spaces.Dict({
            "Minimap_Character_Position": spaces.Discrete(2),
            "NPC_nearby": spaces.Discrete(25),
            'GCP 1' : spaces.Discrete(1),
            'GCP 2' : spaces.Discrete(1), 
            'GCP 3' : spaces.Discrete(1),
            'GCP 4' : spaces.Discrete(1)            
        })

        self.action_space = spaces.Discrete(6)  


    
    def step(self, data): 
       
       
        self.data  = data 



        ''' this is all we need'''

        reward = 0
        

        '''If there are more NPCs on the right and the agent pressed the right + Q key,
           reward the agent with a score of 2.'''

        if self.data['most_npc_density'] == 2 and self.data['action'] == 4 or self.data['action'] == 3:
            reward = 10
            
            
        elif self.data['most_npc_density'] == 2 and self.data['action'] != 4 or self.data['action'] != 3:
            reward = -5
            

        ''' If there are more NPCs on the left and the agent pressed the left + Q key,
           reward the agent with a score of 2.'''

        if self.data['most_npc_density'] == 3 and self.data['action'] == 5 or self.data['action'] == 3:
            reward = 10
        elif self.data['most_npc_density'] == 3 and self.data['action'] != 5 or self.data['action'] != 3:
            reward = -5

        ''' If there are more NPCs on the Top and the agent pressed the Up Arrow + W key,
           reward the agent with a score of 2.'''
        if self.data['most_npc_density'] == 0 and self.data['action'] == 0 or self.data['action'] == 3:
            reward = 10
        elif self.data['most_npc_density'] == 0 and self.data['action'] != 0 or self.data['action'] != 3:
            reward = -5

        #''' If there are more NPCs are the found then .'''
        
        #print('Minimap_Charc_X_Coordinates : ', len(self.data['Minimap_Charc_X_Coordinates']))
        #NO NPC FOUND
        ''' if self.data['most_npc_density'] == -1 and len(self.data['Minimap_Charc_X_Coordinates']) > 0:
           if self.data['action'] == 0 or self.data['action'] == 1 or self.data['action'] == 2 or self.data['action'] == 3:
                reward = 2
           elif self.data['action'] != 0 or self.data['action'] != 1 or self.data['action'] != 2 or self.data['action'] != 3:
                reward = -2
            
           
            print('Pass')
            self.x1 = self.data['Minimap_Charc_X_Coordinates'][0]
            self.y1 = self.data['Minimap_Charc_Y_Coordinates'][0]
            for center in self.data['Green Circle on Mini Map Coordinates']:
                self.x2, self.y2 = center
                distance = math.sqrt(( self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
    
              #  Point A: (35, 80)
              #  Point B: (75, 80)
              #  Point C: (115, 80)
              #  Point D: (35, 125)
              #  Point E: (75, 125)
              #  Point F: (115, 125)
                

                #Reward for point A
                if distance <= 19 and self.x2 == 35 and self.y2 == 80 and (self.data['action'] == 3 or self.data['action'] == 1):
                    reward = 1 
                elif distance <= 19 and self.x2 == 35 and self.y2 == 80 and (self.data['action'] != 3 or self.data['action'] != 1):
                    reward = -2
                
                # Reward for point B
                if distance <= 19 and self.x2 == 75 and self.y2 == 80 and (self.data['action'] == 0 or self.data['action'] == 1):
                    reward = 1 
                elif distance <= 19 and self.x2 == 75 and self.y2 == 80 and (self.data['action'] != 0 or self.data['action'] != 1):
                    reward = -2

                # Reward for point C
                if distance <= 19 and self.x2 == 115 and self.y2 == 80 and (self.data['action'] == 0 or self.data['action'] == 3 or self.data['action'] == 2):
                    reward = 1 
                elif distance <= 19 and self.x2 == 115 and self.y2 == 80 and (self.data['action'] != 0 or self.data['action'] != 3) or self.data['action'] != 2:
                    reward = -2


                #Reward for point D
                if distance <= 19 and self.x2 == 35 and self.y2 == 125 and (self.data['action'] == 2 or self.data['action'] == 1):
                    reward = 1 
                elif distance <= 19 and self.x2 == 35 and self.y2 == 125 and (self.data['action'] != 2 or self.data['action'] != 1):
                    reward = -2
                
                # Reward for point E
                if distance <= 19 and self.x2 == 75 and self.y2 == 125 and (self.data['action'] == 0 or self.data['action'] == 1):
                    reward = 1 
                elif distance <= 19 and self.x2 == 75 and self.y2 == 125 and (self.data['action'] != 0 or self.data['action'] != 1):
                    reward = -2

                # Reward for point F
                if distance <= 19 and self.x2 == 115 and self.y2 == 125 and (self.data['action'] == 0 or self.data['action'] == 2):
                    reward = 1 
                elif distance <= 19 and self.x2 == 115 and self.y2 == 125 and (self.data['action'] != 0 or self.data['action'] != 2):
                    reward = -2'''
           
        obs = {
        "Minimap_Character_Position": None,
        "NPC_nearby": None,
        'GCP 1' : None,
        'GCP 2' : None, 
        'GCP 3' : None,
        'GCP 4' : None
            
                }

        #WARN: Expects `done` signal to be a boolean, actual type: <class 'dict'>
        #WARN: The reward returned by `step()` must be a float, int, np.integer or np.floating, actual type: <class 'dict'>
        
        
    
     
            

        
        return obs, reward, {} , {}
    
    def reset(self):

        
        obs = {
            "Minimap_Character_Position": None,
            "NPC_nearby": None,
            'GCP 1' : None,
            'GCP 2' : None, 
            'GCP 3' : None,
            'GCP 4' : None } 
        
        
        return obs, {}
    

    
