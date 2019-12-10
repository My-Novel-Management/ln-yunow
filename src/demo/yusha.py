# -*- coding: utf-8 -*-
"""Demo: chapter 01
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_findout(w: World):
    he = W(w.hero)
    return w.scene("勇者発見", "勇者はモンスターたちに何故か見つかり、囲まれる",
            he.talk("え？　なんで？"),
            he.look(doing="いつの間にか大量のモンスターに囲まれている"),
            he.look(doing="モンスターの一匹がスマフを見せる"),
            he.look("勇者発見なう！　という呟きが山ほどあるのを"),
            he.talk("え……"),
            he.run(),
            he.do("囲まれた"),
            )

## episode
def ep_demo_yushanow(w: World):
    return w.episode("勇者なう", "勇者誕生したのだが",
            sc_findout(w),
            )
