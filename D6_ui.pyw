#!python2
# coding: utf-8

"""
D6 UI 
Randomly shows a different six sided die face each time the "throw dice" button is pressed

HOW TO RUN:
    Double click script
"""

from kivy.config import Config
Config.set("graphics", "height", 200)
Config.set("graphics", "width", 200)
Config.set("graphics", "minimum_width", 200)
Config.set("graphics", "minimum_height", 200)

import random
import kivy
from kivy.app import App
from kivy.lang import Builder

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '0.1.1'
__date__ = '12:25h, 20/04/2017'
__status__ = 'Finished'


kivy.require('1.9.1')


class D6App(App):

    def throw_dice(self):
        """
        Shows a random dice face each time
        """
        dice = random.randint(1, 6)

        # turn every circle white (background color)
        for circle in self.root.ids.itervalues():
            circle.circle_color = 1, 1, 1

        # each random dice throw draws the required black circles
        if dice == 1:
            self.root.ids.pos5.circle_color = 0, 0, 0
        elif dice == 2:
            self.root.ids.pos7.circle_color = self.root.ids.pos3.circle_color = 0, 0, 0
        elif dice == 3:
            self.root.ids.pos7.circle_color = self.root.ids.pos5.circle_color = self.root.ids.pos3.circle_color \
                = 0, 0, 0
        elif dice == 4:
            self.root.ids.pos7.circle_color = self.root.ids.pos9.circle_color = self.root.ids.pos1.circle_color \
                = self.root.ids.pos3.circle_color = 0, 0, 0
        elif dice == 5:
            self.root.ids.pos7.circle_color = self.root.ids.pos9.circle_color = self.root.ids.pos5.circle_color \
                = self.root.ids.pos1.circle_color = self.root.ids.pos3.circle_color = 0, 0, 0
        elif dice == 6:
            self.root.ids.pos7.circle_color = self.root.ids.pos9.circle_color = self.root.ids.pos4.circle_color \
                = self.root.ids.pos6.circle_color = self.root.ids.pos1.circle_color = self.root.ids.pos3.circle_color \
                = 0, 0, 0

    def build(self):
        layout = Builder.load_string(
"""
#:kivy 1.9.1

<Circle@FloatLayout>:
    circle_color: 1, 1, 1
    
    Widget:
        size: min(root.size)/1.2, min(root.size)/1.2
        size_hint: None, None
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        canvas:
            Color:
                rgb: root.circle_color
            Ellipse:
                pos: self.pos
                size: self.size
                
BoxLayout:
    orientation: "vertical"
    padding: 5
    
    BoxLayout:
        padding: 5
        
        GridLayout:
            cols: 3
            rows: 3
            spacing: 2
            
            canvas:
                Color:
                    rgb: 1, 1,  1
                Rectangle:
                    pos: self.pos
                    size: self.size
            
            # positions 2 and 8 are never used
            Circle:
                id: pos7
            Circle:
            Circle:
                id: pos9
            Circle:
                id: pos4
            Circle:
                id: pos5
            Circle:
                id: pos6
            Circle:
                id: pos1
            Circle:
            Circle:
                id: pos3
    
    Button:
        text: "Throw dice"
        size_hint_y: None
        height: root.height / 6.0
        
        on_release: app.throw_dice()
"""
        )

        return layout

if __name__ == "__main__":
    D6App().run()
