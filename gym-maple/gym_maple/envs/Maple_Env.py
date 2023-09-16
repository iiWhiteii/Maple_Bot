import gym
from gym import spaces
from time import time
import numpy as np

class MapleEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.observation_space = spaces.Dict({

            "Magnitude": spaces.Discrete(2),
            "Memory_Monk": spaces.Discrete(51),
            
        })

        self.action_space = spaces.Discrete(9)  



    reward = 0
    def step(self, info_capture): 
        self.info_capture = info_capture
        
        obs = {
        "Magnitude": np.array(self.info_capture['magnitude']),
        "Memory_Monk": np.array(self.info_capture['Memory_Monk_L.PNG'] + self.info_capture['Memory_Monk_R.PNG'])
                }

        #WARN: Expects `done` signal to be a boolean, actual type: <class 'dict'>
        #WARN: The reward returned by `step()` must be a float, int, np.integer or np.floating, actual type: <class 'dict'>

        if self.info_capture['magnitude'] <= 250:
            reward = 3 
            print(reward)
        else: 
            reward = -3 
            print(reward)

        
        if self.info_capture['Memory_Monk_Death_L.PNG'] > 0:
            reward = self.info_capture['Memory_Monk_Death_L.PNG'] * 2 
        
        if self.info_capture['Memory_Monk_Death_R.PNG'] > 0:
            reward = self.info_capture['Memory_Monk_Death_R.PNG'] * 2 

        
        return obs, reward, {}, {}
    
    def reset(self):
        obs = {
        "Magnitude": 0,
        "Memory_Monk": 0
                }

        return obs, {}
