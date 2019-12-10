# -*- coding: utf-8 -*-
"""Demo: chapter 07
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_castleparty(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("城でパーティ", "人気者として城に呼び出された勇者たち",
            he.come("城にやって"),
            he.talk("すげえご馳走"),
            sol.talk("いいのかよ、$meらこんなとこ来てさ"),
            he.talk("何を言っているのだ。今や時の人となった勇者様なのだよ？"),
            ma.talk("$meはこういうの苦手なんで外出てますね"),
            ma.go(),
            yula.talk("しかしセキュリティが甘そうねえ。宝物庫どこかしら"),
            sol.talk("おい、やめろよ。こんなところでお縄ちょうだいしたら逃げられないどころか炎上して$meら世界中でさらし者になるからな"),
            yula.talk("分かってるわよ"),
            he.walk(),
            he.glad("サインをねだられたり、一緒にシャメしたりして"),
            sol.eat(),
            sol.talk("うめえよ。なあこんなもん食ったことねえ！"),
            yula.talk("ほんと。いい材料使ってるわこれ"),
            # NOTE: 王様直々に祝の言葉を
            he.talk("ありがたき幸せ"),
            he.do("一緒のシャメとってアップする"),
            he.glad("それがまたたく間に拡散されていくのが"),
            # NOTE: だが炎上の足音が近づいていた
            )

## episode
def ep_demo_popular(w: World):
    return w.episode("人気者", "人気者になった勇者たちだが",
            sc_castleparty(w),
            )
