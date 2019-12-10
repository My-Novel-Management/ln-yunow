# -*- coding: utf-8 -*-
"""Demo: story no1
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_daimaou(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("大魔王", "mamazonで魔王退治を依頼したら大魔王が降臨したでござる",
            he.talk("おい何だよ。魔王いなくなったんじゃないのかよ？"),
            ma.talk("そ、そんなはずないですって"),
            he.look("空がどんどん黒くなって雲に覆われるのを"),
            sol.talk("おいあれ。見てみろ"),
            he.look(doing="黒いのが全てモンスターだ"),
            he.talk("嘘だろ……"),
            yula.talk("何してんのよ？　さっさと逃げるわよ"),
            sol.talk("逃げるってどこへ？"),
            he.talk("$me、責任取るよ。こうなったの、もともと$meがあんなもん注文したから"),
            sol.talk("お前がしなくたっていつか誰かがやってただろ？"),
            he.do("剣を構える"),
            sol.talk("ああもう！　どうなっても知らんからな！"),
            sol.do("剣を構える"),
            he.talk("来いよ！"),
            he.look("魔物たちが降ってくるのを"),
            ma.talk("そんなの、絶対許さない"),
            ma.do("目が紅く光る"),
            he.be(doing="世界が真っ白になった"),
            )


## episode
def ep_demo_alldead(w: World):
    return w.episode("全滅", "勇者たちは全滅した",
            sc_daimaou(w),
            )
