import gym
from gym import spaces
from time import time

class MapleEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.observation_space = spaces.Dict({
            "Flash Blade": spaces.Discrete(2),
            "Skill illusion": spaces.Discrete(2),
            "Memory_Monk_Facing_Right": spaces.Discrete(51),
            "Memory_Monk_Facing_Left": spaces.Discrete(51),
            "Memory_Monk_Death_Right": spaces.Discrete(20),
            "Memory_Monk_Death_Left": spaces.Discrete(20)
            
        })

        self.action_space = spaces.Discrete(9)  



    reward = 0
    def step(self, info_capture): # passing in additonal parameter 
        self.info_capture = info_capture

        '''There are a lot of limitation and improvement '''
        if self.info_capture['Sword Illusion2.PNG'] == 1:
            Sword_Illusion = True
            if Sword_Illusion & self.info_capture['Multiple Kill 7.PNG'] == 1:
                reward = 7
                print(reward)
            if Sword_Illusion & self.info_capture['Multiple Kill 8.PNG'] == 1:
                reward = 8
                print(reward) 

        #if self.info_capture['']




            
        obs = {
        "Flash Blade": self.info_capture['Sword Illusion2.PNG'],
        "Skill illusion": self.info_capture['Sword Illusion2.PNG'],
        "Memory_Monk_Facing_Right": self.info_capture['Memory_Monk_R.PNG'],
        "Memory_Monk_Facing_Left": self.info_capture['Memory_Monk_L.PNG'],
        "Memory_Monk_Death_Right": self.info_capture['Memory_Monk_Death_R.PNG'],
        "Memory_Monk_Death_Left": self.info_capture['Memory_Monk_Death_L.PNG']
                }

        #WARN: Expects `done` signal to be a boolean, actual type: <class 'dict'>
        #WARN: The reward returned by `step()` must be a float, int, np.integer or np.floating, actual type: <class 'dict'>

        reward = {0}



        return obs, {}, reward, {}
    

    def reset(self):

        obs = {
        "Flash Blade": 0,
        "Skill illusion": 0,
        "Memory_Monk_Facing_Right": 0,
        "Memory_Monk_Facing_Left": 0,
        "Memory_Monk_Death_Right": 0,
        "Memory_Monk_Death_Left": 0
                }


        return obs, {}
