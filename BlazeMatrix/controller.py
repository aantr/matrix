from BlazeMatrix import Button


class Controller:
    def update(self, dt):
        ...

    def next_activity(self):
        ...

    def prev_activity(self):
        ...


class ButtonController(Controller):
    def __init__(self, button: Button):
        self.button = button

    def update(self, dt):
        self.button.update(dt)

    def next_activity(self):
        return self.button.get_clicks() == 2

    def prev_activity(self):
        return self.button.get_clicks() == 3
