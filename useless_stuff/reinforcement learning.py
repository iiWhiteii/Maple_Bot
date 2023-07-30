import cv2 as cv 
import os 
from time import time 
from windowCapture import window_capture 
import numpy as np 
from template_matching import ImageMatching
import gym 
import gym_maple 

env = gym.make('gym_maple/MapleEnv-v0') 




import glob
template_images = [img for img in glob.glob(r'C:\Users\liang\OneDrive\Desktop\Maple_Bot\Asset\Hero_Skills\*.png')] 

template_images = template_images + [img for img in glob.glob(r'C:\Users\liang\OneDrive\Desktop\Maple_Bot\Asset\Temple Of Time\*.png')] 




wincap = window_capture('Maplestory')



for episode in range(500): 
    frame = wincap.screenshot()
    main_image = cv.imwrite('main_image.png',frame)
    image_match = ImageMatching('main_image.png', 0.74)

    for step in range(400):