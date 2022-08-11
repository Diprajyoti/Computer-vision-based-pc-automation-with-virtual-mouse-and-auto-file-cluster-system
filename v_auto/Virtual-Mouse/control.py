
import keyboard
from win10toast import ToastNotifier
toast=ToastNotifier()
toast.show_toast(
    "Attention  !", "Gesture automation has been started", duration=10)

while True:
    try:
        if keyboard.is_pressed("ctrl+8"):
            exec(open("automate.py").read())
    except:
        continue

    