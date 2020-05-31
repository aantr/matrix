from BlazeMatrix import *
import time

DEBUG = True
effects = [Snow, RainbowFill]
if DEBUG:
    display = PyGameDisplay()
else:
    display = Ws2812b16x16Display()
if DEBUG:
    button = KeyboardButton('space')
else:
    button = Button()
button_controller = ButtonController(button)
matrix = Matrix(display=display, effects=effects, controllers=[button_controller])

previous_frame_time = time.time()
while 1:
    delta_time = time.time() - previous_frame_time
    previous_frame_time = time.time()
    matrix.update(delta_time)
