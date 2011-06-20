import cocos
from cocos.director import director
from cocos.scene import *
from cocos.layer import *
from cocos.sprite import *
from cocos.menu import *
from cocos.scenes.transitions import FadeTRTransition as Transition

from instructions_scene import InstructionsScene

class MenuSceneMenu(Menu):
    def __init__(self):
        super(MenuSceneMenu, self).__init__()
        self.position = (0, -256)
        self.scale = 3

        play_button = ImageMenuItem('resources/graphics/menu/menu_play.png', self.on_play)
        instructions_button = ImageMenuItem('resources/graphics/menu/menu_instructions.png', self.on_instructions)
        options_button = ImageMenuItem('resources/graphics/menu/menu_options.png', self.on_options)
        achievements_button = ImageMenuItem('resources/graphics/menu/menu_achievements.png', self.on_achievements)

        self.create_menu([play_button, instructions_button, options_button, achievements_button], shake(), shake_back())

    def on_quit(self):
        return
        
    def on_play(self):
        return
    
    def on_instructions(self):
        director.replace(Transition(InstructionsScene(self.parent), 0.5))
        return

    def on_options(self):
        return

    def on_achievements(self):
        return

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

