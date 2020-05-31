import keyboard


class Button:
    def __init__(self, holding_timeout=0.3, multiply_click_timeout=0.3):
        self.button_state = self.get_state()
        self.holding_timeout = holding_timeout
        self.multiply_click_timeout = multiply_click_timeout

        self.state_time = 0
        self.prev_state_time = 0
        self.clicks = 0
        self.clicks_flag = False
        self.holding = False
        self.held = False

    def update(self, dt):
        new_state = self.get_state()
        if new_state != self.button_state:
            self.prev_state_time = self.state_time
            self.state_time = 0
        else:
            self.state_time += dt
        if new_state:
            self.on_button_down()
        else:
            self.on_button_up()
        self.button_state = new_state

    def get_clicks(self):
        return self.clicks if self.clicks_flag else 0

    def is_holding(self):
        return self.holding

    def is_held(self):
        return self.held

    def get_state(self):
        ...

    def on_button_down(self):
        if self.state_time == 0:
            # When button pressed
            ...
        if self.state_time > self.holding_timeout:
            if not self.held and not self.holding:
                self.held = True
                self.clicks = 0  # If made a few clicks and after holding occurred then clicks will not work
            else:
                self.held = False
                self.holding = True

    def on_button_up(self):
        if self.state_time == 0:
            # When button released
            self.holding = False
            # || If hold on current frame "on_button_down" is true and next frame is "on_button_up" then
            # || variable reset will not work and it must be there
            # \/
            self.held = False
            if not self.prev_state_time > self.holding_timeout and self.prev_state_time > 0:
                self.clicks += 1

        if self.clicks_flag:
            self.clicks_flag = False
            self.clicks = 0
        if self.state_time > self.multiply_click_timeout and self.clicks > 0:
            self.clicks_flag = True


class KeyboardButton(Button):
    def __init__(self, key):
        self.key = key
        super().__init__()

    def get_state(self):
        return keyboard.is_pressed(self.key)
