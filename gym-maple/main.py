
#Goal is to make this works

#Name : Liang
# Project DQL On Maplestory 

import cv2 as cv
import os
from time import time
from windowCapture import window_capture
import numpy as np
import gym 
import gym_maple
import tensorflow as tf 
from tensorflow import keras


#This is an instance of the window_capture class
wincap = window_capture('Maplestory')

from template_matching import ImageMatching
import glob
template_images = [img for img in glob.glob(r'C:\Users\liang\OneDrive\Desktop\Maple_Bot\Asset\Hero_Skills\*.png')] 
template_images = template_images + [img for img in glob.glob(r'C:\Users\liang\OneDrive\Desktop\Maple_Bot\Asset\Temple Of Time\*.png')] 
#print(template_images)

#Creating an instance of gym Environment 
env = gym.make('gym_maple/MapleEnv-v0')
env.reset()
#print(env.observation_space) 




import pydirectinput

#loop_time = time()  
episode = 0

import time
  
#DQN
from Deep_Q_Learning import DQN

input_shape = [3]
n_outputs = 2
dqn_agent = DQN(input_shape, n_outputs)
model = dqn_agent.build_model()




max_training_duration = 3600
start_time = time.time()
episode = 0

step = 0

 
import keyboard

while time.time() - start_time < max_training_duration:
       
    frame = wincap.screenshot()
    main_image = cv.imwrite('main_image.png',frame) # create it
    image_match = ImageMatching('main_image.png', 0.74)    
    dictionary = image_match.template_matching(template_images) 
    episode += 1
    cumulative_reward = 0 

    # treat this as an env.reset() due to custom env
    state, reward, dummy_a, dummy_b = env.step(dictionary)
    state = np.array([state['Magnitude'],state['Memory_Monk'],state['num_nearby_npcs']])
     
    
    for step in range(2000):
        epsilon = max(1 - episode / 500, 0.01)
        next_state, reward, action = dqn_agent.play_one_step(env,state,epsilon,dictionary)
        cumulative_reward += reward

        #print('cumulative_reward',cumulative_reward)
        #print('episode',episode)
        if episode > 25:
            #print('True')
            dqn_agent.training_step()
            



    
    # Break the loop when 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break









