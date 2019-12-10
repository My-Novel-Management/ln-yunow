# -*- coding: utf-8 -*-
"""Demo: chapter 05
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_impossible(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("ゴブリン無理", "勇者たちは命からがら巣から逃げ出した",
            he.talk("なんなんだよあいつら！"),
            he.run(),
            sol.talk("噂には聞いてたが、すげえな"),
            yula.talk("感心してる場合じゃないでしょ？"),
            ma.talk("もう全部爆裂魔法かなんかでやっちゃいませんか？"),
            he.talk("そんなことしたらここに溜め込まれてる汚水が下流域まで流れるだろ？"),
            he.talk("とりあえずテントまで戻って立て直しだな"),
            he.look("スマフを手に連絡を取り合っているゴブリンたちを遠目に"),
            )

## episode
def ep_demo_goblinnest(w: World):
    return w.episode("ゴブリンの巣", "勇者たちはゴブリンの巣を何とかしてくれと依頼された",
            sc_impossible(w),
            )
