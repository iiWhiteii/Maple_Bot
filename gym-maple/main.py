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
print(template_images)

#Creating an instance of gym Environment 
env = gym.make('gym_maple/MapleEnv-v0')
print(env.observation_space) 

env.reset()     



#Constructuring Deep Neural Network
input_shape = [2] # == env.observation_space.shape
n_outputs = 4 # == env.action_space.n

model = keras.models.Sequential([
    keras.layers.Dense(32, activation="elu", input_shape=input_shape),
    keras.layers.Dense(32, activation="elu"),
    keras.layers.Dense(n_outputs)
])  


from Deep_Q_Learning import epsilon_greedy_policy

#loop_time = time()  
episode = 0
while True:
    episode += 1
    frame = wincap.screenshot()
    main_image = cv.imwrite('main_image.png',frame) # create it
    #print(main_image)
    image_match = ImageMatching('main_image.png', 0.74)    
    
    dictionary = image_match.template_matching(template_images)

    print(dictionary)


    
    obs,reward,c,d = env.step(dictionary) 
    #obs = [obs['Magnitude'],obs['Memory_Monk']]
    #print(obs['Memory_Monk'])
    obs = np.array([obs['Memory_Monk'],obs['Magnitude']])
    print('obs',obs)

    epsilon = 0.50
    print('greedy_policy',epsilon_greedy_policy(obs,epsilon)) # Trigger and do it action 

    #When it trigger it do an action our environment response to it 
    #---> Action that when trigger <---- 
    #  we call this again obs,reward,c,d = env.step(dictionary) so we have information about obs, reward 
    # we assign to memory for obs,reward then attach obs,reward append it to replay_memory
    # then we have a if statement for reward  
    # if the reward let say 100, we get our model to get_weights 
    # 
    # if episode is 50 then we use the training_step(batch_size)
    # 
    #  

        
    



    #Calculate FPS
    ##print('FPS {}'.format(1 / (time() - loop_time)))
    #loop_time = time()

    # Break the loop when 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break









