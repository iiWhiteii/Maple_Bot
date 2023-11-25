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
import tensorflow as tf
from tensorflow import keras
from collections import deque
import pydirectinput as pdi
from DQN import DQN
from reply_memory import ReplayMemory





pretain_weight = "C:\\Users\\liang\\OneDrive\\Desktop\\Maple_Bot\\gym-maple\\position_minimap_detector\\runs\\detect\\train\\weights\\best.pt"
yolov8 = model(weight_path=pretain_weight)
wincap = WindowCapture('Maplestory')
env = gym.make('gym_maple/MapleEnv-v0')
env.reset()

state_game = state()
start_time = time.time()
rewards = []













epsilon = 0.01
step_count = 0
training_frequency = 1





''' Let Construct Reply Memory '''
Agent_Memory = ReplayMemory(max_size=10000)






'''Construct Neural Network For DQN '''
dqn_agent = DQN(input_shape=(3,),n_outputs=6)
print("Neural Network Summary:",dqn_agent.model_summary())



# Just need this 
def play_one_step(state, epsilon):
    action = dqn_agent.epsilon_greedy_policy(state,epsilon)
    time.sleep(0.25)
    return action




while True:
    step_count += 0.50
    # Get an updated image of the game
    screenshot = wincap.get_screenshot()
    '''"Class 0: Player Coordinates")
    "Class 1: Eye of Time Coordinates")
    "Class 2: Eye of Time Death Coordinates")
    "Class 3: Memory Monk Coordinates")
    "Class 4: Memory Monk Death Coordinates")
    "Class 5: Mini Map Character Coordinates")
    "Class 6: Green Circle on Mini Map Coordinates")'''


    screenshot, class_0, class_1, class_2, class_3, class_4, class_5, class_6 = yolov8.detection(screenshot)


   
    # Current States
    current_state = state_game.state(Player_Coordinates=class_0,Eye_of_Time_Coordinates=class_1, Memory_Monk_Coordinates=class_3,Minimap_Charc_Coordinates=class_5, GC_MINIMAP_Coordinates=class_6)

    # randomly does an action
    epsilon = max(1 - step_count / 500, 0.01)
    
    action = play_one_step(np.array(current_state), epsilon)

    print('action : ', action )


    ''' By employing a hashmap in this manner, the environment can provide responses '''
    environment_response_data  = { "most_npc_density" : current_state[0], 'Green Circle on Mini Map Coordinates' : class_6, 'action': action, 'Minimap_Charc_X_Coordinates': [current_state[1]],'Minimap_Charc_Y_Coordinates':[current_state[2]]}
    print('env response :',environment_response_data)
    dummy, reward, dummy , dummy = env.step(environment_response_data)
    
    #time.sleep(0.55)

    screenshot, class_0, class_1, class_2, class_3, class_4, class_5, class_6 = yolov8.detection(screenshot)
    next_state = state_game.state(Player_Coordinates=class_0,Eye_of_Time_Coordinates=class_1, Memory_Monk_Coordinates=class_3,Minimap_Charc_Coordinates=class_5, GC_MINIMAP_Coordinates=class_6)
    
    #Replay memory    
    Agent_Memory.add_experience((current_state, action, reward, next_state))


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
        dqn_agent.training_step(discount_rate=0.95, sample_experiences=Agent_Memory.sample_experiences(batch_size=1))


    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
    print('Done.')