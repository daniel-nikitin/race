import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = 'race'
SPEED_CAR = 10
SPEED_CAR2 = -2


class Car(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x


class Car2(arcade.Sprite):
    def update(self):
        self.center_y += self.change_y
        if self.top < 0:
            self.bottom = 700
            window.onemorebigscore += 1
            self.center_x = random.randint(1, 1000)


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.stategame = True
        self.road = arcade.load_texture("background.jpeg")
        self.car = Car("blue_car.png")
        self.car2 = Car2("yellow_car.png")
        self.car.center_x = 300
        self.car.center_y = 100
        self.car2.center_x = random.randint(1, 1000)
        self.car2.center_y = 400
        self.car2.change_y = SPEED_CAR2
        self.onemorebigscore = 0
        self.road_offset = 0

    def on_key_press(self, symbol: int, modifiers: int):  # нажатие клавиш
        print(self.car.right)
        if symbol == arcade.key.A:
            self.car.angle = 10
            self.car.change_x = -SPEED_CAR
        if symbol == arcade.key.D:
            self.car.angle = -10
            self.car.change_x = SPEED_CAR

    def on_key_release(self, symbol: int, modifiers: int):  # отпускание клавиш
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.car.change_x = 0
            self.car.angle = 0

    def on_draw(self):
        self.clear()
        if self.stategame == False:
            arcade.draw_text("game over", 200, 200, arcade.color.WHITE, 40)
            return
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT * (.5 - self.road_offset), SCREEN_WIDTH,
                                      SCREEN_HEIGHT, self.road)
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT * (.5 - self.road_offset) + SCREEN_HEIGHT,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.road)
        self.car.draw()
        self.car2.draw()
        arcade.draw_text(f"SCORE {self.onemorebigscore}", 200, 600)

    def update(self, delta_time: float):  # двигатель всего проекта (работает постоянно)
        if self.car.right > SCREEN_WIDTH:
            self.car.right = SCREEN_WIDTH
        if self.car.left < 0:
            self.car.left = 0

        if arcade.check_for_collision(self.car2, self.car):
            self.stategame = False

        self.car.update()
        self.car2.update()

        self.road_offset += 0.03
        if self.road_offset >= 1:
            self.road_offset = 0


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
