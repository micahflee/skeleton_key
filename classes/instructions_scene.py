import cocos
from cocos.director import director
from cocos.scene import *
from cocos.layer import *
from cocos.sprite import *
from cocos.menu import *
from cocos.scenes.transitions import FadeTRTransition as Transition

class InstructionsSceneMenu(Menu):
    def __init__(self):
        super(InstructionsSceneMenu, self).__init__()

        back_button = ImageMenuItem('resources/graphics/instructions/instructions_back.png', self.on_back)
        back_button.scale = 3
        menu_button = ImageMenuItem('resources/graphics/instructions/instructions_menu.png', self.on_menu)
        menu_button.scale = 3
        next_button = ImageMenuItem('resources/graphics/instructions/instructions_next.png', self.on_next)
        next_button.scale = 3

        self.create_menu([back_button, menu_button, next_button], shake(), shake_back(), layout_strategy=fixedPositionMenuLayout([(140,60), (384,60), (628,60)]))

    def on_quit(self):
        return

    def on_back(self):
        return

    def on_menu(self):
        director.replace(Transition(self.parent.return_scene, 0.5))

    def on_next(self):
        return

class InstructionsScene(Scene):
    def __init__(self, return_scene):
        super(InstructionsScene, self).__init__()
        print('InstructionsScene init')
        self.return_scene = return_scene
        
        # background
        background = Sprite('resources/graphics/backgrounds/background_forest_dark.png')
        background.position = (384,512)
        self.add(background, 0)
        
        # header
        header = Sprite('resources/graphics/instructions/instructions_header.png')
        header.position = (384, 937.5)
        self.add(header, 1)
        
        # menu
        menu = InstructionsSceneMenu()
        self.add(menu, 1)

        # the page
        self.page_number = 1
        self.page_layer = Layer()
        self.add(self.page_layer, 1)
        page1 = Sprite('resources/graphics/instructions/instructions_page1.png')
        page2 = Sprite('resources/graphics/instructions/instructions_page2.png')
        page3 = Sprite('resources/graphics/instructions/instructions_page3.png')
        page4 = Sprite('resources/graphics/instructions/instructions_page4.png')
        page1.position = (384, 485.5)
        page2.position = (1152, 485.5)
        page3.position = (1920, 485.5)
        page4.position = (2688, 485.5)
        self.page_layer.add(page1)
        self.page_layer.add(page2)
        self.page_layer.add(page3)
        self.page_layer.add(page4)

