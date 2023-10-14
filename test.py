import time
import pydirectinput as pdi

# Function to press a key and release it after a delay
def press_and_release(key, duration=0.1):
    pdi.keyDown(key)
    time.sleep(duration)
    pdi.keyUp(key)

# Infinite loop
while True:
    # Pressing Left Alt twice
    press_and_release("left")
    press_and_release("alt")
    press_and_release("alt")
    
# action_to_id = {'Double Jump Left' : 0, 'Double Jump Right' : 1 ,'UP + W' : 2, 'DOWN + W' : 3 ,'Right Q' : 4 ,'LEFT Q' : 5}