from BlazeMatrix import *
import time

display = Ws2812b16x16Display()
effects = [Snow, RainbowFill]
button = Button()
button_controller = ButtonController(button)
matrix = Matrix(display=display, effects=effects, controllers=[button_controller])

while 1:
    delta_time = time.time() - previous_frame_time
    previous_frame_time = time.time()

    matrix.update(delta_time)

    time.sleep(1 / display.max_fps)
