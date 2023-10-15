import cv2 as cv2
import numpy as np
import os
import time
from windowcapture import WindowCapture 
from yolov8 import model
import gym_maple
import gym 
import math
from state import state
import time
import sys
import tensorflow as tf
from tensorflow import keras
from collections import deque











import time
import pydirectinput as pdi


pretain_weight = "C:\\Users\\liang\\OneDrive\\Desktop\\TestMapleBot\\gym-maple\\position_minimap_detector\\runs\\detect\\train\\weights\\last.pt"
yolov8 = model(weight_path=pretain_weight)
wincap = WindowCapture('Maplestory')
env = gym.make('gym_maple/MapleEnv-v0')
env.reset()

state_game = state()
start_time = time.time()
rewards = []
start_time = time.time()




def press_and_release(key, duration=0.1):
    pdi.keyDown(key)
    time.sleep(duration)
    pdi.keyUp(key)

def special_press_and_release(key):
    pdi.keyDown(key)
    pdi.keyUp(key)



model = keras.models.Sequential([
    keras.layers.Dense(128, activation="elu", input_shape=(3,)),
    keras.layers.Dense(64, activation="elu"),
    keras.layers.Dense(32, activation="elu"),
    keras.layers.Dense(6)
])


def epsilon_greedy_policy(state, epsilon):
    if np.random.rand() < epsilon:
        random_action = np.random.randint(6)
        perform_action(random_action)
        return random_action
    else:
        Q_values = model.predict(state[np.newaxis])
        best_action = np.argmax(Q_values[0])
        perform_action(best_action)
        return best_action


def perform_action(action):
    if action == 0:
        press_and_release("left")
        press_and_release("alt")
        press_and_release("alt")
    elif action == 1:
        press_and_release("right")
        press_and_release("alt")
        press_and_release("alt")
    elif action == 2:
        special_press_and_release("up")
        special_press_and_release("w")
    elif action == 3:
        special_press_and_release("down")
        special_press_and_release("w")
    elif action == 4:
        press_and_release("right")
        press_and_release("q")
    elif action == 5:
        press_and_release("left")
        press_and_release("q")

    return action






# Just need this 
def play_one_step(state, epsilon):
    action = epsilon_greedy_policy(state, epsilon)  
    time.sleep(0.50)
    return action


replay_memory = deque(maxlen=7000)

def sample_experiences(batch_size):
    indices = np.random.randint(len(replay_memory), size = batch_size)
    batch = [replay_memory[index] for index in indices] 
    return [np.array([experience[field_index] for experience in batch]) for field_index in range(4)] 




optimizer = keras.optimizers.Adam(lr=1e-3)
loss_fn = keras.losses.mean_squared_error


def training_step(batch_size,discount_rate): 
    current_states, actions, rewards, next_states = sample_experiences(batch_size)
    actions = np.array(actions)
    rewards = np.array(rewards)
    next_Q_values = model.predict(next_states)
    max_next_Q_values = np.max(next_Q_values, axis=1)
    target_Q_values = rewards + (discount_rate * max_next_Q_values)
    mask = tf.one_hot(actions, 6)
    with tf.GradientTape() as tape:
        all_Q_values = model(current_states)
        Q_values = tf.reduce_sum(all_Q_values * mask, axis=1, keepdims=True)
        loss = tf.reduce_mean(loss_fn(target_Q_values, Q_values))   
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    print('optimizer:', optimizer.apply_gradients(zip(grads, model.trainable_variables)))
    




epsilon = 0.01
step_count = 0
training_frequency = 25


while True:
    step_count += 1
    # Get an updated image of the game
    screenshot = wincap.get_screenshot()
    screenshot, charc_pos, eye_of_time_pos, eye_of_time_kills, memory_monk_pos, memory_monk_kills, yellow_dot_pos, greencircle_pos = yolov8.detection(screenshot)
   
   
    # Current States
    current_state = state_game.state(charc_pos=charc_pos, eye_of_time_pos=eye_of_time_pos,
                                          memory_monk_pos=memory_monk_pos, yellow_dot_pos=yellow_dot_pos,
                                          green_circle_pos=greencircle_pos)
    
    print('current_state:',current_state)


    ''' By employing a hashmap in this manner, the environment can provide responses '''
    hashmap = { 'memory_monk_death_pos' : memory_monk_kills, 'eye_of_time_death_pos' : eye_of_time_kills, 'yellow_dot_pos' : yellow_dot_pos, 'green circle' : greencircle_pos, 'charc_minimap_pos' : yellow_dot_pos }
    
    # randomly does an action
    action = play_one_step(np.array(current_state), epsilon)
    

    epsilon = max(1 - step_count / 500, 0.01)
    dummy, reward, dummy , dummy = env.step(hashmap)
    
    screenshot, charc_pos, eye_of_time_pos, eye_of_time_kills, memory_monk_pos, memory_monk_kills, yellow_dot_pos, greencircle_pos = yolov8.detection(screenshot) 
    next_state = state_game.state(charc_pos=charc_pos, eye_of_time_pos=eye_of_time_pos,memory_monk_pos=memory_monk_pos, yellow_dot_pos=yellow_dot_pos, green_circle_pos=greencircle_pos)
    
    #Replay memory    
    replay_memory.append((current_state, action, reward, next_state))


    print('step_count',step_count)  
    print('current_state:',current_state)
    print('action', action)
    print('reward:',reward)
    print('next_state',next_state)
    cv2.imshow('Maplestory', screenshot)


    if step_count % training_frequency == 0:
        #print(replay_memory)
        print('AT TRAINING STAGE')
        print('AT TRAINING STAGE')
        print('AT TRAINING STAGE')
        print('AT TRAINING STAGE')
        print('AT TRAINING STAGE')
        print('AT TRAINING STAGE')
        print('AT TRAINING STAGE')
        print('AT TRAINING STAGE')
        training_step(batch_size=20,discount_rate=0.95)


    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
    print('Done.')