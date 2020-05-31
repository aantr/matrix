import time
from BlazeMatrix import Display


class Matrix:
    def __init__(self, display, effects, controllers=()):
        self.display: Display = display
        self.effects = [effect(display) for effect in effects]
        self.activity = self.effects[0]
        self.controllers = controllers

    def set_activity(self, activity):
        self.activity = activity

    def update(self, dt):
        if self.activity is not None:
            self.activity.call(dt)
        for controller in self.controllers:
            controller.update(dt)
            if controller.next_activity():
                self.next_activity()
            if controller.prev_activity():
                self.prev_activity()
        time.sleep(self.activity.frame_time)

    def next_activity(self):
        print('next')

    def prev_activity(self):
        print('prev')
