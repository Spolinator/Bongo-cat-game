import arcade
import os
import time

#constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND = 0

class Bongogame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Bongo Cat")
        self.background = None
        #setup empty background



    def setup(self):
        self.background = arcade.load_texture("Assets/background0.png")
        #sets background

    def on_draw(self):
        arcade.start_render()
        #starts rendering

        BACKGROUND = arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        #draws background

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

class buttons:
    def __init__(self, width, height):
        super().__init__(self, width, height)

        #set up buttons
        self.play_btn = None
        self.lvlslct_btn = None
        self.slctcat_btn = None
        self.settings_btn = None
        self.volume_btn = None

    def setup(self):
        self.all_buttons_list = arcade.SpriteList()
        

        #setup buttons
        self.play_btn = arcade.load_texture("Assests/Main_Menu/Buttons/PLAYbtn.png")
        self.lvlslct_btn = arcade.load_texture("Assests/Main_Menu/Buttons/LEVELSELECTbtn.png")
        self.slctcat_btn = arcade.load_texture("Assests/Main_Menu/Buttons/SELECTCATbtn.png")
        self.settings_btn = arcade.load_texture("Assests/Main_Menu/Buttons/SETTINGSbtn.png")
        self.volume_btn = arcade.load_texture("Assests/Main_Menu/Buttons/VOLUME_ONbtn.png")
        
    def on_draw(self):
        arcade.start_render()
        #start render

        playbtn_x = 560
        playbtn_y = 350

        def draw_playbtn(self):
            
            self.width = 397
            self.height = 87
            self.scale = 0.7
            
            PLAYbtn = arcade.draw_texture_rectangle(playbtn_x, playbtn_y, scale*width, scale*height, self.play_btn)

        def draw_lvlslctbtn(self):
            self.width = 397
            self.height = 87
            self.scale = 0.7
            
            LEVELSELECTbtn = arcade.draw_texture_rectangle(playbtn_x, playbtn_y-87-10, sclae*width, scale*height, self.lvlslct_btn)
      


def main_menu():
    game = Bongogame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()        

if __name__ == "__main_menu__":
    main_menu()