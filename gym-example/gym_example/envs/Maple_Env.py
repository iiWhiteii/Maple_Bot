import gym
from gym import error, spaces, utils
from gym.utils import seeding

class BasicEnv(gym.Env):
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

            "Memory_Monk_Facing_Right" : spaces.Discrete(51),
            "Memory_Monk_Facing_Left" : spaces.Discrete(51), 
            "Memory_Monk_Death_Right" : spaces.Discrete(20),
            "Memory_Monk_Death_Left" : spaces.Discrete(20), 
            "Death By World reaver" : spaces.Discrete(20)

            }
                )


        # #There are essentially 9 actions 
        # Right, Left, Up, Down, Jump(Alt), 1(Raging Blow), 2(Skill illusion), Q(Puncture), W(Flash Blade) 
        self.action_space = spaces.Discrete(9)








        

    def step(self, action):

        # if we took an action, we were in state 1
        obs = ['Character_Pos','Num_MOD_Pos','Skills CC']
    
        if action == 2:
            reward = 1
        else:
            reward = -1
            
        # regardless of the action, game is done after a single step
        done = True

        info = {}

        return obs, reward, done, info
    



    

    def reset(self):
        obs = 'state'
        info = {}
        return obs, info 
  
    def render(self, mode='human'):
        pass

    def close(self):
        pass
