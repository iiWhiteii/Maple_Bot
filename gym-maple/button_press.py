from pynput import keyboard
import time

class KeyTracker:
    def __init__(self):
        self.last_left_pressed = 0
        self.alt_l_count = 0
        self.alt_r_count = 0 
        self.actions = []

        self.left_trigger = False
        self.right_trigger = False
        self.w_pressed = False

    def on_press(self, key):
        # Set the flag if 'w' is pressed
        if isinstance(key, keyboard.KeyCode) and key.char == 'w':
            self.w_pressed = True

        ''' The Left Side '''
        if key == keyboard.Key.left:
            if not self.left_trigger: 
                self.left_trigger = True
                print('Left arrow key pressed')
                self.last_left_pressed = time.time()  

        elif key == keyboard.Key.alt_l and self.left_trigger == True:
            if time.time() - self.last_left_pressed < 0.50:
                self.alt_l_count += 1
                print(self.alt_l_count)
                if self.alt_l_count == 2:
                    print('Alt Twice')
                    self.actions.append(0)
                    self.alt_l_count = 0
            else: 
                self.alt_l_count = 0
                self.left_trigger = False

        '''  The Right Side '''
        if key == keyboard.Key.right:
            if not self.right_trigger: 
                self.right_trigger = True
                print('Right arrow key pressed')
                self.last_left_pressed = time.time()
        
        elif key == keyboard.Key.alt_l and self.right_trigger == True:
            if time.time() - self.last_left_pressed < 0.50:
                self.alt_r_count += 1
                print(self.alt_r_count)
                if self.alt_r_count == 2:
                    self.actions.append(1)
                    print('Alt Twice')
                    self.alt_r_count = 0
            else: 
                self.alt_r_count = 0
                self.right_trigger = False 

        '''    Up Arrow + W   '''
        if self.w_pressed and key == keyboard.Key.up:
            print('W + Up key pressed')
            self.actions.append(2)


        '''   Down Arrow + W '''

        if self.w_pressed and key == keyboard.Key.down:
            print('W + Down Key pressed')
            self.actions.append(3)


        if isinstance(key,keyboard.KeyCode) and key.char == '1':
            print('One is pressed')
            self.actions.append(4)


    def on_release(self, key):
        # Reset the flag when 'w' is released
        if isinstance(key, keyboard.KeyCode) and key.char == 'w':
            self.w_pressed = False

        if key == keyboard.Key.esc:
            return False  # You can add additional logic here if needed

# Create an instance of KeyTracker
tracker = KeyTracker()

# Start the listener in a non-blocking way
listener = keyboard.Listener(on_press=tracker.on_press, on_release=tracker.on_release)
listener.start()

# Main loop
#while True:
    # Your main loop logic goes here
 ##  print("Actions:", tracker.actions)




        






        

