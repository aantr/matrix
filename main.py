from BlazeMatrix import *
import neopixel as neo
import board
import time

# LED strip configuration:
LED_COUNT = 16
LED_PIN = board.D18
LED_BRIGHTNESS = 0.2
ORDER = neo.GRB

pixels = neo.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=ORDER)

display = Display()
effects = [Snow, RainbowFill]
# button = KeyboardButton('space')
# button_controller = ButtonController(button)
matrix = Matrix(display, effects, [])

pixels[0] = neo.Color(255, 255, 255)
pixels.show()
previous_frame_time = time.time()

time.sleep(5)
pixels[0] = neo.Color(0, 0, 0)
pixels.show()

# while 1:
#     delta_time = time.time() - previous_frame_time
#     previous_frame_time = time.time()
#
#     matrix.update(delta_time)
#
#     time.sleep(1 / display.max_fps)
