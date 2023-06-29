#Obersation 

"""  Observation:
        Type: Dict "MapleWrapper" : box(4)
        Num     Observation               Min                     Max
        1       Player X1                 0                       825
        2       Mob X1 (1)                0                       825
        3       Player Facing Direction   0                       1
        4       Attacked                  0                       1          """




#Actions: 

    # Walk Left 
    # Walk Right 
    # Jump 
    # Attack 




import gym
import time
from gym import spaces
#from maplewrapper import wrapper
import numpy as np
#import pydirectinput
import cv2





class env(gym.Env):

    def __init__(self,w):
























