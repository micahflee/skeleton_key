'''
Skeleton Key
Copyright (C) 2011 Micah Lee

This file is part of Skeleton Key.

Skeleton Key is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cocos'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'classes'))

import cocos
from cocos.director import director
import pyglet

import menu_scene

if __name__ == "__main__":
    pyglet.font.add_directory('resources/fonts')
    director.init(resizable=True, width=768, height=1024, caption='Skeleton Key')
    director.show_FPS = True
    director.run(menu_scene.MenuScene())

