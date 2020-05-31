from BlazeMatrix import Color, Effect, Game
from random import randrange


class RainbowFill(Effect):
    def init(self):
        self.hue = 0
        return {'name': 'rainbow fill', 'default_fps': 60, 'values': {}}

    def update(self):
        self.hue += 1 if self.hue < 255 else -255
        color = Color(self.hue, 255, 255, hsv=True)
        for x in range(16):
            for y in range(16):
                self.display.set_pixel(x, y, color)


class Snow(Effect):
    def init(self):
        return {'name': 'snowfall', 'default_fps': 30, 'values': {'dense': 10}}

    def update(self):
        for x in range(self.w):
            for y in range(self.h - 1):
                self.display.set_pixel(x, y, self.display.get_pixel(x, y + 1))

        for x in range(self.w):
            if self.display.get_pixel(x, self.h - 2).rgb == (0, 0, 0) and randrange(0, self.values['dense']) == 0:
                self.display.set_pixel(x, self.h - 1, Color(*[255 - randrange(0, 10) * 10] * 3))
            else:
                self.display.set_pixel(x, self.h - 1, Color(0, 0, 0))
