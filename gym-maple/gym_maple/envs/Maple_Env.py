import gym
from gym import spaces
from time import time

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
        '''if self.info_capture['Sword Illusion2.PNG'] == 1:
            Sword_Illusion = True 
            if Sword_Illusion & self.info_capture['Multiple Kill 3.PNG'] == 1:
                reward = 3
                print(reward)
            if Sword_Illusion & self.info_capture['Multiple Kill 4.PNG'] == 1:
                reward = 4
                print(reward) 
            if Sword_Illusion & self.info_capture['Multiple Kill 5.PNG'] == 1:
                reward = 5
                print(reward)     
            if Sword_Illusion & self.info_capture['Multiple Kill 6.PNG'] == 1:
                reward = 6
                print(reward)
            if Sword_Illusion & self.info_capture['Multiple Kill 7.PNG'] == 1:
                reward = 7
                print(reward)
            if Sword_Illusion & self.info_capture['Multiple Kill 8.PNG'] == 1:
                reward = 8
                print(reward) '''
    
        obs = {
        "Magnitude": self.info_capture['magnitude'],
        "Memory_Monk": self.info_capture['Memory_Monk_L.PNG'] + self.info_capture['Memory_Monk_R.PNG']
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
