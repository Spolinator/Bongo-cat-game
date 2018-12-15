import arcade
import os
import time

#constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
                               
"""class Bongogame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Bongo Cat")
        self.background = None
        #setup empty background
        background = 0
        self.menusound = None
        #set empty sound
    def setup(self):
        self.background = arcade.load_texture("Assets/background0.png")
        #set background
        setbackground()
        
    def on_draw(self):
        arcade.start_render()
        #starts rendering
        displaybackground()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        #draws background        
    def update(self, delta_time):
        pass
    def on_key_press(self, key, key_modifiers):
        pass
    def on_key_release(self, key, key_modifiers):
        pass
    def on_mouse_press(self, x,y,buttons, key_modifiers):
        pass
    def on_mouse_release(self, x,y,buttons, key_modifiers):
        pass"""

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Bongo cat")      

self.background = arcade.load_texture("Assets/background0.png")
arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

def main_menu():
    menusound = arcade.load_sound("Assets/Fig_Leaf_Times_Two.mp3")
    arcade.play_sound(menusound)
    arcade.run()

if __name__ == "__main__":
    main_menu()
