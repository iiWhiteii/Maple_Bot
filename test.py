
import cv2
import numpy as np



# Load the main image
main_image = cv2.imread('main_image_3.PNG')

# Define a list of template images
template_images = ['ice_drake_1.PNG', 'ice_drake_2.PNG','ice_drake_4.PNG','ice_drake_5.PNG','ice_drake_6.PNG']

# Convert the main image to grayscale
main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)

# Set a threshold for the matching score
threshold = 0.8

# Iterate over each template image
for template_image_path in template_images:
    # Load the template image
    template_image = cv2.imread(template_image_path)
    # Convert the template image to grayscale
    template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
    # Perform template matching
    result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)


    #Trying to understand the threshold 
    # Get the locations of matches above the threshold
    locations = np.where(result >= threshold)
    print(locations)
    
    # Draw a rectangle for each match
    for loc in zip(*locations[::-1]):
        top_left = loc
        bottom_right = (top_left[0] + template_image.shape[1], top_left[1] + template_image.shape[0])
        cv2.rectangle(main_image, top_left, bottom_right, (0, 255, 0), 2)

# Display the result
cv2.imshow('Matching Result', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
