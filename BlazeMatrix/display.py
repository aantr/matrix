from BlazeMatrix import Color
# import pygame
import neopixel as neo
import board

class Display:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.min_fps = 1
        self.max_fps = 100
        self.default_fps = 30

    def update(self):
        ...

    def set_pixel(self, x, y, color: Color):
        ...

    def get_pixel(self, x, y):
        ...


class PyGameDisplay(Display):
    def __init__(self):
        super().__init__(16, 16)
        self.max_fps = 100
        pygame.init()
        self.m = [[Color(0, 0, 0) for _ in range(self.w)] for _ in range(self.h)]
        self.screen = pygame.display.set_mode([512, 512])

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        a = 32
        w = 4
        for y in range(self.h):
            for x in range(self.w):
                s = pygame.Surface((a - w, a - w))
                s.fill(self.m[self.h - y - 1][x].rgb)
                self.screen.blit(s, pygame.Rect((x * a + w, y * a + w, 0, 0)))
        pygame.display.update()

    def set_pixel(self, x, y, color: Color):
        self.m[y][x] = color

    def get_pixel(self, x, y):
        return self.m[y][x]


class Ws2812b16x16Display(Display):
    def __init__(self):
        super().__init__(16, 16)
        self.max_fps = 60
        LED_COUNT = 256
        LED_PIN = board.D18
        LED_BRIGHTNESS = 0.1
        ORDER = neo.GRB
        self.pixels = neo.NeoPixel(
            LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS,
            auto_write=False, pixel_order=ORDER
        )

