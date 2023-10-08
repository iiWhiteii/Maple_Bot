import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture 
#from ultralytics import YOLO
from yolov8 import model

#constuct yolo

pretain_weight = "C:\\Users\\liang\\OneDrive\\Desktop\\TestMapleBot\\gym-maple\\position_minimap_detector\\runs\\detect\\train\\weights\\last.pt"

#yolov8 = YOLO("C:\\Users\\liang\\OneDrive\\Desktop\\TestMapleBot\\position_minimap_detector\\runs\\detect\\train3\\weights\\best.pt") 

yolov8 = model(weight_path=pretain_weight)


# initialize the WindowCapture class
wincap = WindowCapture('Maplestory')

#Creating maple_gym environment 
import gym_maple
import gym 


import math
env = gym.make('gym_maple/MapleEnv-v0')
env.reset()
#import keyboard
#from button_press import KeyTracker 
#action_tracker = KeyTracker()
from hash_map import hash_map_tracker
from state import state
from button_press import tracker





state_game = state()
start_time = time.time()
rewards = []

while True:
   
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    screenshot, charc_pos, eye_of_time_pos , d ,memory_monk_pos , f ,yellow_dot_pos, greencircle_pos = yolov8.detection(screenshot)
       
    # Representing Current States 
    current_states = state_game.state(charc_pos=charc_pos, eye_of_time_pos=eye_of_time_pos,memory_monk_pos=memory_monk_pos,yellow_dot_pos=yellow_dot_pos, green_circle_pos=greencircle_pos)
    
    # Actions
    actions = tracker.actions
    print('actions',actions)
    
    env_information = hash_map_tracker(charc_pos, eye_of_time_pos ,d ,memory_monk_pos , f ,yellow_dot_pos, greencircle_pos)
    
    # Immediate Rewards response by the env
    dummy1, reward, dummy2, dummy3 = env.step(env_information)

    #rewards  
    rewards.append(reward)

    # Next_States
    screenshot, charc_pos, eye_of_time_pos , d ,memory_monk_pos , f ,yellow_dot_pos, greencircle_pos = yolov8.detection(screenshot)
    next_State = state_game.state(charc_pos=charc_pos, eye_of_time_pos=eye_of_time_pos,memory_monk_pos=memory_monk_pos,yellow_dot_pos=yellow_dot_pos, green_circle_pos=greencircle_pos)
        
    print('current_states',current_states,time.time() - start_time)
    print('actions:',actions,time.time() - start_time)
    print('rewards:',rewards,time.time() - start_time)
    print('next_States',next_State,time.time() - start_time)

    # display the images
    cv.imshow('Maplestory',screenshot)

    #debug the loop rate
    #print('FPS {}'.format(1 / (time() - loop_time)))
    #loop_time = time()

    # press 'q' with the output window focused to exit.
    # press 'f' to save screenshot as a positive image, press 'd' to 
    # save as a negative image.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
   # elif key == ord('f'):
   # cv.imwrite('maplestory_temple_of_time/{}.jpg'.format(loop_time), screenshot)
   # elif key == ord('d'):
   # cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)

print('Done.')