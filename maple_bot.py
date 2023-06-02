import numpy as np
import cv2 as cv 
import pyautogui


while True:
    # Capture screen frame
    frame = pyautogui.screenshot()
    frame = np.array(frame)
    
    # Convert the image to OpenCV format
    #frame = cv.cvtColor(np.array(frame), cv.COLOR_RGB2BGR)
    
    # Display the resulting frame
    cv.imshow('Computer Vision', frame)
    
    # Break the loop when 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

## Close all windows
#cv.destroyAllWindows()