import arcade

SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100
SCREEN_TITLE = 'example'


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        self.clear()

    def update(self, delta_time: float):
        pass


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()