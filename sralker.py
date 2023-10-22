from pynput import keyboard

def on_press(key):
    modifier = "none"
    try:
        k = str(key.char)  # single-char keys
    except:
        k = str(key.name)  # other keys
    if k == "enter":
        print("\n", end="")
        modifier = k
    if k == "backspace":
        modifier = k
        pass
    if k == "shift":
        modifier = k
        pass
    if k == "space":
        modifier = k
        print(" ", end="")
    if modifier == "none":
        print(k, end="")

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
