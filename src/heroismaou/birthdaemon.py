# -*- coding: utf-8 -*-
"""Episode: chapter 09
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
W = Writer


## scenes
def sc_birthdaemon(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    return w.scene("魔獣誕生", "スマフ上のヘイトは遂に魔獣を生み出した",
            sol.talk("何だこりゃあ"),
            he.look("勝手にスマフを見ていた$n_solを"),
            he.talk("勝手に使うなって言ってる……ん？"),
            he.look("スマフ上が騒がしいのを"),
            he.look("沢山の人が空の写真を上げる様子を"),
            he.talk("これ何？"),
            ma.come(),
            ma.talk("大変です！"),
            ma.talk("これ、魔獣です"),
            he.talk("どういうこと？"),
            ma.talk("だから、魔獣が生まれちゃったんですよ！　太郎様のせいで！"),
            he.talk("なんで？"),
            )


## episode
def ep_birth_daemon(w: World):
    return w.episode("ヘイトの魔獣", "ヘイトの魔獣が誕生した",
            sc_birthdaemon(w),
            )
