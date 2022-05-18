# importing required modules.

from pynput.keyboard import Controller
from keyboard import press
import time

# making the controller.
kb = Controller()

# delays 5 seconds, so you can open an app to try the spam.
time.sleep(5)

# start amount, recommended 0, so you can understand what's happening.
start = 0

# setting the amount.
amount = 5

while start < amount:
    # incrementing amount so your device doesn't crash (personal experience)
    start += 1

    #typing the message.
    kb.type("the text you want to type.")

    # pressing enter so it sends the message.
    press("enter")

# end.
