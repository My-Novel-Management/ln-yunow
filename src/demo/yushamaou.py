# -*- coding: utf-8 -*-
"""Demo: chapter 09
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
W = Writer

## scenes
def sc_birthdevil(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("ヘイトの魔獣誕生", "ヘイトが大きくなりヘイトの魔獣が誕生した",
            hero.look("スマフを"),
            hero.look("彼を含めた家族や仲間たちへのいわれない罵詈雑言たちを"),
            hero.talk("どうすればいいんだよ！"),
            sol.talk("ひでえなあ"),
            yula.talk("ほっとくしかないのよ"),
            hero.talk("けどさ、このままじゃ"),
            hero.be("洞窟に閉じこもって"),
            mako.come("戻って"),
            mako.talk("駄目だよ。外はどこも抗議活動の行列"),
            yula.look("スマフで抗議活動の様子を"),
            sol.talk("もうさっさと出てって謝ったらいいんじゃね？"),
            yula.talk("それじゃ収まらないわよ、ほら"),
            yula.look(doing="スマフで見せる"),
            hero.think(doing="出て行ったところで殴り殺される様が想像できる"),
            hero.attention("空模様を"),
            hero.look("空に憎悪が浮上して、何か形を取っていくのを"),
            hero.talk("これ何だろ？"),
            mako.talk("何ですか？"),
            mako.expression("まずい、という"),
            sol.talk("何だよ？"),
            mako.talk("ヘイトです。人間たちの憎悪の感情は魔物のエネルギィ源なんです"),
            mako.talk("それが吸収しきれず、実体化する"),
            yula.talk("どうなるんだい？"),
            mako.talk("誕生するんですよ、魔物が"),
            hero.look("外に出て"),
            hero.talk("何だありゃ！"),
            hero.look("天高くをつく巨大な黒い魔獣"),
            mako.talk("ヘイトの魔獣です"),
            hero.look("魔獣が街を襲う様を"),
            hero.look("スマフに流れる街の人々の悲鳴を"),
            hero.think("どうすりゃいいんだと"),
            )


## episode
def ep_demo_yusha_is_maou(w: World):
    return w.episode("勇者が魔王", "炎上の挙げ句に勇者が魔王だったことになってしまった",
            sc_birthdevil(w),
            )
