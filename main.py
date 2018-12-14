import arcade
import os
#constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND = 0

class Bongogame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Bongo Cat")
        self.background = None
    def setup(self):
        self.background = arcade.load_texture("Assets/background0.png")
    def on_draw(self):
        arcade.start_render()
        BACKGROUND = arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
    def update(self, delta_time):
        pass
    def on_key_press(self, key, key_modifiers):
        pass
    def on_key_release(self, key, key_modifiers):
        pass
    def on_mouse_motion(self, x,y,delta_x,delta_y):
        pass
    def on_mouse_press(self, x,y,delta_x,delta_y):
        pass
    def on_mouse_release(self, x,y,delta_x,delta_y):
        pass
def main():
    game = Bongogame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()        

if __name__ == "__main__":
    main()