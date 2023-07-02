import gym
from gym import error, spaces, utils
from gym.utils import seeding

class MapleEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self): 







        #Observation(state) 

        #1 Memory_Monk_Facing_Right
        #2 Memory_Monk_Facing_Left
        #3 Memory_Monk_Death_Right
        #4 Memory_Monk_Death_Left 
        #5 Death By worldreaver 

        #6 Skill illusion 
        #7 Raging Blow
        #8 Puncture
        #9 Flash Blade
        


        self.observation_space = spaces.Dict({ 
            
            "Flash Blade" : spaces.Discrete(2), 
            "Puncture" : spaces.Discrete(1), 
            "Skill illusion" : spaces.Discrete(2),
            "Raging Blow" : spaces.Discrete(1), 
            "World Reaver" : spaces.Discrete(2),

            "Memory_Monk_Facing_Right" : spaces.Discrete(51),
            "Memory_Monk_Facing_Left" : spaces.Discrete(51), 
            "Memory_Monk_Death_Right" : spaces.Discrete(20),
            "Memory_Monk_Death_Left" : spaces.Discrete(20), 
            "Death By World Reaver" : spaces.Discrete(20)

            }
                )


        # #There are essentially 9 actions 
        # Right, Left, Up, Down, Jump(Alt), 1(Raging Blow),  
        # 2(Skill illusion), Q(Puncture), W(Flash Blade)
        # Delete(World Reaver) 
        self.action_space = spaces.Discrete(9)




#Passing in computer vision parameter into here



    def step(self,info_capture):

        self.info_capture = info_capture 

        if 'Memory_Monk_Death_Right' in obs: 
            reward = reward * 'quantity computer vision spoting this'  

        if 'Memory_Monk_Death_Left' in obs: 
            reward = reward * 'quantity computer vision spoting this '

        if 'Death By World Reaver' in obs: 
            reward = reward * 'quantity computer vision spotting this' + bonus


        Observation = []




        return obs, reward, done, info
    



    

    def reset(self):
        obs = 'state'
        info = {}
        return obs, info 
  
    def render(self, mode='human'):
        pass

    def close(self):
        pass
