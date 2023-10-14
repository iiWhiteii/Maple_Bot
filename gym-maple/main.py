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
from state import state
from button_press import tracker





state_game = state()
start_time = time.time()
rewards = []

reply_memory = []

import cv2
import time
import sys

# Assuming you have these functions/objects
# wincap = ...
# yolov8 = ...
# state_game = ...
# tracker = ...
# env = ...

# Specify the file path

start_time = time.time()

# Open the file for writing

while True:

    # Get an updated image of the game
    screenshot = wincap.get_screenshot()
    screenshot, charc_pos, eye_of_time_pos, eye_of_time_kills, memory_monk_pos, memory_monk_kills, yellow_dot_pos, greencircle_pos = yolov8.detection(screenshot)
    print(eye_of_time_pos)
   
    # Representing Current States
    current_states = state_game.state(charc_pos=charc_pos, eye_of_time_pos=eye_of_time_pos,
                                          memory_monk_pos=memory_monk_pos, yellow_dot_pos=yellow_dot_pos,
                                          green_circle_pos=greencircle_pos)

    ''' By employing a hashmap in this manner, the environment can provide responses.   '''
    hashmap = { 'memory_monk_death_pos' : memory_monk_kills, 'eye_of_time_death_pos' : eye_of_time_kills, 'yellow_dot_pos' : yellow_dot_pos, 'green circle' : greencircle_pos, 'charc_minimap_pos' : yellow_dot_pos }
    
    dummy, reward, dummy , dummy = env.step(hashmap)














    # Display the images
    cv2.imshow('Maplestory', screenshot)

    # Debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()

    # Press 'q' with the output window focused to exit.
    # Press 'f' to save screenshot as a positive image, press 'd' to
    # save as a negative image.
    # Waits 1 ms every loop to process key presses
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
print('Done.')
