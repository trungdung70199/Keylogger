from pynput import mouse

def on_move(x, y):
    print("Pointer moved to {0}".format(x, y))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format ('Pressed' if pressed else 'Released', (x, y)))

    if not pressed:
        return False
    
def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format ('down' if dy < 0 else 'up', (x, y)))

with mouse.Listener(on_move=on_move,
                    on_click=on_click,
                    on_scroll=on_scroll) as listener:
    listener.join()

with open ("Result.txt", "a") as file:
    file.write(listener)
print(listener)

listener = mouse.Listener(on_move=on_move,
                          on_click=on_click,
                          on_scroll=on_scroll)
listener.start()

