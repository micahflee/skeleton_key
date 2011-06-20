#!/usr/bin/env python

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cocos'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'classes'))

import cocos
from cocos.director import director
import pyglet

from menu_scene import MenuScene

if __name__ == "__main__":
    pyglet.font.add_directory('resources/fonts')
    director.init(resizable=True, width=768, height=1024, caption='Skeleton Key')
    director.show_FPS = True
    director.run(MenuScene())

