import cv2
import numpy as np
import os 



dir_path =  "C:/Users/liang/OneDrive/Desktop/Maple_Bot"
sub_directories = ["Asset"]

images = [file for sub_dir_idx, sub_dir in enumerate(sub_directories) for file in os.listdir(os.path.join(dir_path,sub_dir))]
memory_monk_1 = images[0]


threshold = 0.80

# Load the main image and the template image
main_image = cv2.imread('main_image.PNG')
template_image = cv2.imread('Memory_Monk_2.PNG')

# Convert both images to opencv format
main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)



# Get the location of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0] + template_image.shape[1], top_left[1] + template_image.shape[0])
print('bottom_right',bottom_right)

# Draw a rectangle around the matched region
cv2.rectangle(main_image, top_left, bottom_right, (0, 255, 0), 2)

# Display the result
cv2.imshow('Matching Result', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
