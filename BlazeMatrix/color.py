import colorsys


class Color:
    def __init__(self, hsv=False, *args):
        if len(args) != 3:
            raise TypeError('invalid number of arguments, expected 3')
        if hsv:
            args = tuple(map(lambda x: int(x * 255), colorsys.hsv_to_rgb(*map(lambda x: x / 255, args))))
        self.rgb = args

    def __str__(self):
        return str(self.rgb)
