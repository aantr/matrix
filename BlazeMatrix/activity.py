from BlazeMatrix import Display


class Activity:
    def __init__(self, display, check_settings=None):
        self.display: Display = display
        self.w = display.w
        self.h = display.h

        self.default_fps = self.display.default_fps
        self.fps = self.default_fps

        self.frame_time = 1 / self.fps
        self.passed_time = 0

        self.settings = self.init()
        if type(self.settings) != dict:
            raise TypeError('type dict of returned value of method "init" was expected')

        if check_settings is None:
            check_settings = {}
        default_check = {'name': str, 'values': dict}
        for k, v in default_check.items():
            if k not in self.settings:
                self.settings[k] = v

        for k, v in check_settings.items():
            if k not in self.settings:
                raise KeyError(f'"{k}" not in settings')
            if type(self.settings[k]) != v:
                raise TypeError(f'{v} type of {k} was expected')

        self.name = self.settings['name']
        self.values = self.settings['values']

    def call(self, dt):
        self.passed_time += dt
        if self.passed_time > self.frame_time:
            self.passed_time = 0
            self.update()
            self.display.update()

    def set_fps(self, fps):
        if fps < self.display.min_fps:
            fps = self.display.min_fps
        if fps > self.display.max_fps:
            fps = self.display.max_fps
        self.fps = fps
        self.frame_time = 1 / self.fps

    def get_fps(self):
        return self.fps

    def init(self):
        ...

    def update(self):
        ...


class Effect(Activity):
    ...


class Game(Activity):
    def __init__(self, display, controller):
        super().__init__(display)
