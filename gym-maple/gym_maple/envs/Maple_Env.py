import gym
from gym import spaces

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

        if self.info_capture['Sword Illusion.PNG'] == 0:
            print('hi')

        obs = {"observation": 1, "reward": 2, "done": False, "info": {}}
        return obs

    def reset(self):
        obs = {"observation": 1, "reward": 2, "done": False, "info": {}}
        return obs
