import cocos
from cocos.director import director
from cocos.scene import *
from cocos.layer import *
from cocos.sprite import *
from cocos.menu import *

class MenuSceneMenu(Menu):
    def __init__(self):
        super(MenuSceneMenu, self).__init__()
        self.position = (0, 0)

        play = ImageMenuItem('resources/graphics/menu/menu_play.png', self.on_play)
        play.scale = 3.0
        instructions = ImageMenuItem('resources/graphics/menu/menu_instructions.png', self.on_instructions)
        instructions.scale = 3.0
        options = ImageMenuItem('resources/graphics/menu/menu_options.png', self.on_options)
        options.scale = 3.0
        achievements = ImageMenuItem('resources/graphics/menu/menu_achievements.png', self.on_achievements)
        achievements.scale = 3.0

        self.create_menu([play, instructions, options, achievements], shake(), shake_back())
        
    def on_play(self):
        return
        # play clicked
    
    def on_instructions(self):
        return
        # instructions clicked

    def on_options(self):
        return
        # options clicked

    def on_achievements(self):
        return
        # achievements clicked  

class MenuScene(Scene):
    def __init__(self):
        super(MenuScene, self).__init__()
        print('MenuScene init')
        
        # background
        background = Sprite('resources/graphics/backgrounds/background_forest_light.png')
        background.position = (384,512)
        self.add(background, 0)
        
        # header
        header = Sprite('resources/graphics/menu/menu_header.png')
        header.position = (384, 811.5)
        self.add(header, 1)
        
        # menu
        menu = MenuSceneMenu()
        self.add(menu, 1)


