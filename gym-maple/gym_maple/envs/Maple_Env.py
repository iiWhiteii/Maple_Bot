import gym
from gym import spaces
from time import time

class MapleEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.observation_space = spaces.Dict({
            "Flash Blade": spaces.Discrete(2),
            "Puncture": spaces.Discrete(1),
            "Skill illusion": spaces.Discrete(2),
            "Raging Blow": spaces.Discrete(1),
            "World Reaver": spaces.Discrete(2),
            "Memory_Monk_Facing_Right": spaces.Discrete(51),
            "Memory_Monk_Facing_Left": spaces.Discrete(51),
            "Memory_Monk_Death_Right": spaces.Discrete(20),
            "Memory_Monk_Death_Left": spaces.Discrete(20),
            "Death By World Reaver": spaces.Discrete(50)
        })

        self.action_space = spaces.Discrete(9)

    def step(self, info_capture):
        self.info_capture = info_capture

        '''There are a lot of limitation and improvement '''
        if self.info_capture['Sword Illusion2.PNG'] == 1:
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
                print(reward)
            
        obs = {
        "Flash Blade": 0,
        "Puncture": 0,
        "Skill illusion": 0,
        "Raging Blow": 0,
        "World Reaver": 0,
        "Memory_Monk_Facing_Right": 0,
        "Memory_Monk_Facing_Left": 0,
        "Memory_Monk_Death_Right": 0,
        "Memory_Monk_Death_Left": 0,
        "Death By World Reaver": 0
                }

        #WARN: Expects `done` signal to be a boolean, actual type: <class 'dict'>
        #WARN: The reward returned by `step()` must be a float, int, np.integer or np.floating, actual type: <class 'dict'>

        reward = {1,2,3,4}



        return obs, {}, reward, {}
    


    def reset(self):
        obs = {
        "Flash Blade": 0,
        "Puncture": 0,
        "Skill illusion": 0,
        "Raging Blow": 0,
        "World Reaver": 0,
        "Memory_Monk_Facing_Right": 0,
        "Memory_Monk_Facing_Left": 0,
        "Memory_Monk_Death_Right": 0,
        "Memory_Monk_Death_Left": 0,
        "Death By World Reaver": 0
                }


        return obs, {}
