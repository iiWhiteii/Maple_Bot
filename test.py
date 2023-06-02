
import pyautogui
import numpy as np
import os 
import pandas as pd 
from skimage.transform import resize
from skimage.io import imread 
from skimage import io 
import matplotlib.pyplot as plt 



#frame = pyautogui.screenshot()
#frame = np.array(frame)
#print(frame)

#print(frame.shape) 



input_dir = 'C:/Users/liang/OneDrive/Desktop/Maple_Bot'


for file in os.listdir(os.path.join(input_dir)): 
    if file == 'red.png':
        img = file

 


img = imread(img)
plt.imshow(img.reshape(img.shape))
plt.show()
img = np.array(img)
print(img.shape)
  