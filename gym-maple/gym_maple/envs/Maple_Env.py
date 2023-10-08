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


    #reward = 0
    def step(self, info_capture): 
        self.info_capture = info_capture
        print(self.info_capture['charc_minimap_pos'], self.info_capture['green circle'])

        if len(self.info_capture['eye_of_time_death_pos']) > 0: 
            reward = len(self.info_capture['eye_of_time_death_pos']) * 5
            #print(reward)

        elif len(self.info_capture['memory_monk_death_pos']) > 0: 
            reward = len(self.info_capture['memory_monk_death_pos']) * 5 
            #print(reward)

        self.green_circle_pos = self.info_capture['green circle']
        self.charc_minimap_pos = self.info_capture['charc_minimap_pos']
        
        if len(self.charc_minimap_pos) >  0:
            x1 = self.charc_minimap_pos[0][0]
            y1 = self.charc_minimap_pos[0][1]
            for center in self.green_circle_pos:
                x2,y2 = center
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                if distance <= 19:
                    reward = 0.50
                else:
                    reward = -0.50
            

        











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
        
        reward = 0 
    
       # if self.info_capture['magnitude'] < 250:
         #   reward = 0
            

        
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
    

    
