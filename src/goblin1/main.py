# -*- coding: utf-8 -*-
"""Chapter: title
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files


## define alias
W = Writer


## chapter
def ch_main(w: World):
    return w.chapter("main",
            note="chapter desc",
            )
