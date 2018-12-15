import arcade
import os
import time
import pyglet

#constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
volume_on = True

class main_menu:
    def draw_background():
        background = arcade.load_texture("Assets/background0.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, background)

    def draw_playbutton():
        global playbuttoncenter_x
        global playbuttoncenter_y
        global playbuttonscale
        global playbuttonwidth
        global playbuttonheight
        scale = 0.7
        width = 397
        height = 87
        playbuttoncenter_x = SCREEN_WIDTH / 2
        playbuttoncenter_y = SCREEN_HEIGHT / 2
        playbuttonwidth = width * scale
        playbuttonheight = height * scale            
        play = arcade.load_texture("Assets/Main-menu/Buttons/PLAYbtn.png")
        arcade.draw_texture_rectangle(playbuttoncenter_x, playbuttoncenter_y, playbuttonwidth, playbuttonheight, play)
    def check_mouse_press_playbutton(x,y):
        if x > (playbuttoncenter_x - playbuttonwidth / 2):
            print("test")



    def menusound():
        menusound = arcade.load_sound("Assets/Fig_Leaf_Times_Two.mp3")
        arcade.play_sound(menusound)

    def draw_settingsbutton():
        scale = 0.7
        width = 87
        height = 87

        settingsbutton = arcade.load_texture("Assets/Main-Menu/Buttons/SETTINGSbtn.png")
        arcade.draw_texture_rectangle(1150.5, 675, width*scale, height*scale, settingsbutton)                        

    def draw_volumebutton():
        scale = 0.7
        width = 87
        height = 87

        if volume_on == False:
            volumeoff = arcade.load_texture("Assets/Main-Menu/Buttons/VOLUME-OFFbtn.png")
            arcade.draw_texture_rectangle(1232.5,675, width*scale, height*scale, volumeoff)                                                    
        else:
            volumeon = arcade.load_texture("Assets/Main-Menu/Buttons/VOLUME-ONbtn.png")
            arcade.draw_texture_rectangle(1232.5,675, width*scale, height*scale, volumeon)

    def draw_selectcat():
        scale = 0.45
        width = 397
        height = 87
        selectcat = arcade.load_texture("Assets/Main-Menu/Buttons/SELECTCATbtn.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2 - 94.325, SCREEN_HEIGHT / 2 - 60.025, width*scale, height*scale, selectcat)

    def draw_selectlevel():
        scale = 0.45
        width = 397
        height = 87
        selectlevel = arcade.load_texture("Assets/Main-Menu/Buttons/LEVELSELECTbtn.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2 + 94.325, SCREEN_HEIGHT / 2 - 60.025, width*scale, height*scale, selectlevel)                                

    def draw_title():
        scale = 0.85
        width = 877
        height = 161
        
        title = arcade.load_texture("Assets/Main-Menu/Bongocat-the-game.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, 575, width*scale, height*scale, title)
        
    def bongo_cat1():
        scale1 = 0.5      
        width = 423
        height = 423

        bongocat = arcade.load_texture("Assets/Main-Menu/Bongocat1.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2 + 180, SCREEN_HEIGHT // 2 + 200, width*scale1, height*scale1, bongocat, -5)

    def bongo_cat2():
        scale2 = 0.5
        width = 680
        height = 689
                
        bongocat = arcade.load_texture("Assets/Main-Menu/Bongocat2.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 500, width*scale2, height*scale2, bongocat, -5)
        
    """def bongo_cat():
        while True:
            main_menu.bongo_cat1()
            time.sleep(0.8)
            main_menu.bongo_cat2()
            time.sleep(0.8)     """                           
                                       

def draw_Main_Menu():
    main_menu.draw_background()
    main_menu.draw_playbutton()
    main_menu.draw_selectcat()
    main_menu.draw_selectlevel()
    main_menu.draw_volumebutton()
    main_menu.draw_settingsbutton()
    main_menu.draw_title() 


class Bongogame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
    def on_draw(self):
        draw_Main_Menu()
    def on_mouse_press(self, x,y, buttons, keymodifiers):
        main_menu.check_mouse_press_playbutton(x,y)
    """def on_update(self, delta_time):
        main_menu.bongo_cat()
    def set_update_rate(self, rate):
        pyglet.clock.unschedule(self.on_update)
        pyglet.clock.schedule_interval(self.on_update, 1/20)"""
  


def main():
    window = Bongogame(SCREEN_WIDTH, SCREEN_HEIGHT, "Bongo Cat: The Game")
    #main_menu.menusound()
    arcade.run()

main()