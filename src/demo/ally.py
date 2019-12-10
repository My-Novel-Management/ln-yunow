# -*- coding: utf-8 -*-
"""Demo: chapter 02
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_catchtheaf(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("泥棒を取っつまえたが", "神父に化けていた泥棒を捕まえたが既に勇者のしるしは売りさばいた後だった",
            he.talk("待て！　とにかくその勇者のしるしだけ返してくれないと困る"),
            sol.talk("え？　お前って勇者なの？"),
            he.talk("そうだけどそうじゃないんだよ！　これには深い訳が！"),
            sol.talk("どう見ても勇者じゃなくね？"),
            he.run(),
            sol.run(),
            yula.run(),
            he.talk("この先で挟み撃ちすっぞ"),
            sol.talk("お、おう"),
            w.br(),
            he.talk("もうここで終わりだぞ？"),
            yula.talk("ごめんなさいね。もう全部売っちゃったからモウカリで"),
            he.talk("え？"),
            )

## episode
def ep_demo_ally(w: World):
    return w.episode("仲間", "勇者は仲間を集めようとするが",
            sc_catchtheaf(w),
            )
