# !/usr/bin/env python3

import neopixel as neo
from BlazeMatrix import *
import time

# LED strip configuration:
LED_COUNT = 16
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 100
LED_INVERT = False
LED_CHANNEL = 0

strip = neo.Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,
                              LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

display = PyGameDisplay()
effects = [Snow, RainbowFill]
button = KeyboardButton('space')
button_controller = ButtonController(button)
matrix = Matrix(display, effects, [button_controller])

strip.setPixelColor(0, neo.Color(255, 255, 255))
strip.show()
previous_frame_time = time.time()

time.sleep(5)
strip.setPixelColor(0, neo.Color(255, 255, 255))
strip.show()

# while 1:
#     delta_time = time.time() - previous_frame_time
#     previous_frame_time = time.time()
#
#     matrix.update(delta_time)
#
#     time.sleep(1 / display.max_fps)
