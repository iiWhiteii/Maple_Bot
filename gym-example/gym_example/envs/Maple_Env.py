import gym
from gym import error, spaces, utils
from gym.utils import seeding

class BasicEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):

        '''
            Observation_space(State_space):  
            0 Character_Pos
            1 Num_MOD_Pos
            2 Skills CC
        '''  

        ''' 
            Action_space:  
            0 Right Movement: Move the character to the right.
            1 Left Movement: Move the character to the left.
            2 Skill 1: Activate skill 1 
            3 Skill 2: Activate skill 2
            4 Skill 3: Activate skill 3
            5 Skill 4: Activate skill 4
            6 Skill 5: Activate skill 5
            7 Jump: Make the character jump
        '''

        
        
        self.observation_space = spaces.Discrete(3)
        self.action_space = spaces.Discrete(7)

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
