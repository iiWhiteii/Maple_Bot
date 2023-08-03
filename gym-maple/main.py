import cv2 as cv
import os
from time import time
from windowCapture import window_capture
import numpy as np
import gym 
import gym_maple
import tensorflow as tf

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

loop_time = time()
while True:
    frame = wincap.screenshot()
    main_image = cv.imwrite('main_image.png',frame) # create it
    #print(main_image)
    image_match = ImageMatching('main_image.png', 0.74)    
    #these dictionary value will be representing as info capture by CV
    dictionary = image_match.template_matching(template_images)

    step = env.step(dictionary)
    

    #Calculate FPS
    ##print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # Break the loop when 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


input_shape = [4] # == env.observation_space.shape
n_outputs = 2 # == env.action_space.n

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(32, activation="elu", input_shape=input_shape),
    tf.keras.layers.Dense(32, activation="elu"),
    tf.keras.layers.Dense(n_outputs)
])


def epsilon_greedy_policy(state,epsilon=0):
    if np.random.rand() < epsilon:
        return np.random.randint(n_outputs) # random action 
    
    else: 
        Q_values = model.predict(state[np.newaxis], verbose=0)[0]
        return Q_values.argmax() 
    
from collections import deque 
replay_buffer = deque(maxlen=2000) 


def sample_experiences(batch_size):
    indices = np.random.randint(len(replay_buffer),size = batch_size)
    batch = [replay_buffer[index] for index in indices] 
    return [   

        np.array([experience[field_index] for experience in batch]) 
        for field_index in range(6)

    ]  


def play_one_step(env,state,epsilon): 
    action = epsilon_greedy_policy(state,epsilon)
    next_state, reward, done, truncated, info = env.step(action)
    replay_buffer.append((state,action,reward,next_state,done,truncated))
    return next_state, reward, done, truncated, info  

batch_size = 32 
discount_factor = 0.95 
optimizer = tf.keras.optimizers.Nadam(learning_rate=1e-2)
loss_fn = tf.keras.losses.mean_absolute_error 

def training_step(batch_size): 
    experiences = sample_experiences(batch_size)
    states, actions, rewards, next_states, dones, truncateds = experiences 
    next_Q_values = model.predict(next_states, verbose=0)
    max_next_Q_values = next_Q_values.max(axis=1)
    runs = 1.0 - (dones | truncateds)
    target_Q_values = rewards + runs * discount_factor * max_next_Q_values
    target_Q_values = target_Q_values.reshape(-1,1)
    mask = tf.one_hot(actions,n_outputs)

    with tf.GradientTape() as tape: 
        all_Q_values = model(states)
        Q_values = tf.reduce_sum(all_Q_values * mask, axis = 1, keepdims = True)
        loss = tf.reduce_mean(loss_fn(target_Q_values,Q_values))

    grads = tape.gradient(loss,model.trainable_variables)
    optimizer.apply_gradients(zip(grads,model.trainable_variables))


