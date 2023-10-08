from pynput import keyboard

def on_press(key):
    if isinstance(key, keyboard.KeyCode) and key.char == 'w':
        print('W key pressed')
    elif isinstance(key, keyboard.KeyCode):
        print('Alphanumeric key {0} pressed'.format(key.char))
    else:
        print('Special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
