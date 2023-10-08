from button_press import tracker
from pynput import keyboard


while True:
    with keyboard.Listener(on_press=tracker.on_press, on_release=tracker.on_release) as listener:
        listener.join()