# -*- coding: utf-8 -*-
"""Demo: chapter 08
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
W = Writer


## scenes
def sc_hidecave(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("洞窟籠り", "ついに町中を歩けなくなり、勇者たちは洞窟に篭った",
            sol.come("入って"),
            sol.talk("ほらよ、食いもん。こんなじゃmamazonも使えないぞ"),
            hero.talk("だいたい$meが何したってんだよ"),
            hero.look("スマフで外の様子を"),
            hero.look(doing="そこには勇者に対する大量の悪口にスクショがあった"),
            hero.talk("$meなんも悪いことしてないのに"),
            sol.talk("これだろ？　調子にのんなってのに対する返答"),
            hero.talk("あれはあっちが悪いし"),
            yula.talk("仕方ないじゃないの。相手が悪かったんだから"),
            # NOTE: なんだかんだあって
            hero.look("スマフに「勇者を名乗っているのは本当は魔王だ」と書き込みを"),
            hero.talk("なんでなんだよ！？"),
            hero.look("外を覗くと暗雲が垂れ込めているのを"),
            )

## episode
def ep_demo_burnout(w: World):
    return w.episode("Demo", "炎上してどうしようもなくなり、洞窟に篭った",
            sc_hidecave(w),
            )
