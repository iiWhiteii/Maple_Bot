
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
print(template_images)

#Creating an instance of gym Environment 
env = gym.make('gym_maple/MapleEnv-v0')
print(env.observation_space) 

env.reset()     

#
import pyautogui

from Deep_Q_Learning import epsilon_greedy_policy, training_step 

epsilon = 0.50 
min_epsilon = 0.01 
epsilon_decay = 0.995  

from collections import deque 
replay_memory = deque(maxlen=2000)

input_shape = [2] # == env.observation_space.shape
n_outputs = 2 # == env.action_space.n

model = keras.models.Sequential([
    keras.layers.Dense(44, activation="elu", input_shape=input_shape),
    keras.layers.Dense(44, activation="elu"),
    keras.layers.Dense(n_outputs)
])  

def epsilon_greedy_policy(state, epsilon):
    if np.random.rand() < epsilon:
        return np.random.randint(2)
    else:
        Q_values = model.predict(state[np.newaxis])
        print('Q_values:',Q_values)
        return np.argmax(Q_values[0]) 

def sample_experiences(batch_size):
    indices = np.random.randint(len(replay_memory), size=batch_size)
    batch = [replay_memory[index] for index in indices]
    states, actions, rewards, next_states = [
        np.array([experience[field_index] for experience in batch])
        for field_index in range(4)]
    return states, actions, rewards, next_states

import pydirectinput

batch_size = 32
discount_rate = 0.95
optimizer = keras.optimizers.Adam(lr=1e-3)
loss_fn = keras.losses.mean_squared_error  


def training_step(batch_size):
    experiences = sample_experiences(batch_size) # this works
    #print('experiences',experiences)
    states, actions, rewards, next_states = experiences
    next_Q_values = model.predict(next_states)
   # print('next_Q_values',next_Q_values)
    max_next_Q_values = np.max(next_Q_values, axis=1)
   # print('max_next_Q_values',max_next_Q_values)
    target_Q_values = rewards + (discount_rate * max_next_Q_values)
    #print('target_Q_values',target_Q_values)
    mask = tf.one_hot(actions, n_outputs)
    #print('mask:',mask)
    with tf.GradientTape() as tape:
        all_Q_values = model(states)
        Q_values = tf.reduce_sum(all_Q_values * mask, axis=1, keepdims=True)
        loss = tf.reduce_mean(loss_fn(target_Q_values, Q_values))
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))

#loop_time = time()  
episode = 0

import time
#epsilon = 0.50  

benchmark_cumulative_reward = 30
cumulative_reward = 0 

while True:
    episode += 1
    frame = wincap.screenshot()
    main_image = cv.imwrite('main_image.png',frame) # create it
    #print(main_image)
    image_match = ImageMatching('main_image.png', 0.74)    
    
    dictionary = image_match.template_matching(template_images)

    #print(dictionary)

    current_obs,dummy_reward,c,d = env.step(dictionary)  
    current_obs = np.array((current_obs['Memory_Monk'],current_obs['Magnitude']))

    epsilon = max(epsilon * epsilon_decay, min_epsilon)
    #print('epsilon:',epsilon)

    cumulative_reward += dummy_reward
    print('cumulative_reward:',cumulative_reward) 


    action = epsilon_greedy_policy(current_obs,epsilon)
    print('greedy_policy',action)   

    if action == 0:
        pydirectinput.press('left')  # Simulate pressing the left arrow key
        time.sleep(0.05)
    if action == 1:
        pydirectinput.press('right') 
        time.sleep(0.05)  # Simulate pressing the right arrow key
   # if action == 2:
     #   pydirectinput.press('left') 
     #   time.sleep(0.05)  # Simulate pressing and holding the Ctrl key
   # if action == 3:
     #   pydirectinput.press('right') 
      #  time.sleep(0.05)  # Simulate pressing the 'w' key
    
   # print('greedy_policy',action)   

    action = [action]
    next_obs,reward,c,d = env.step(dictionary)
    reward = [reward]
    next_obs = [next_obs['Memory_Monk'],next_obs['Magnitude']]
    print('reward', reward)
    

    replay_memory.append((current_obs,next_obs,reward,action)) 


    print(replay_memory)


    if cumulative_reward > benchmark_cumulative_reward: 
        benchmark_cumulative_reward = cumulative_reward
        #training_step(batch_size=31) 
        current_states, next_states, rewards, actions = sample_experiences(batch_size=30)
        print(current_states, next_states,rewards,actions)

        print('next_state:',next_states)

        next_Q_values = model.predict(next_states) 
        print('next_Q_values',next_Q_values) 

        max_next_Q_values = np.max(next_Q_values, axis=1)
        print('max_next_Q_values',max_next_Q_values)




        

    #Calculate FPS
    ##print('FPS {}'.format(1 / (time() - loop_time)))
    #loop_time = time()

    # Break the loop when 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break









