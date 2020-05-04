# -*- coding: utf-8 -*-
"""Chapter 1: 第一章「勇者なう！」
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
from src.c1_iamhero.e1_getsmaph import ep_start
from src.c1_iamhero.e2_yushanow import ep_church
from src.c1_iamhero.e3_monster import ep_bar

## define alias
W = Writer


## chapter
def ch01(w: World):
    return w.chapter("第一章「勇者なう！」",
            ep_start(w),
            ep_church(w),
            ep_bar(w),
            ## NOTE
            ##  - 王宮に呼ばれた少年は「勇者」に当選したと云われ、魔法具スマフを渡される。魔王退治を命じられた
            ##  - 初めて触れるスマフに喜び「勇者なう」等と自分の画像を投稿してはつぶやく
            ##  - まずは仲間探しと酒場に向かうが、何故か魔物に取り囲まれた。スマフは魔物たちも持っていたのだ。ぼこられる勇者
            note="王宮に呼ばれて魔王退治を命じられた勇者は魔法具スマフを手に入れ、意気揚々とそれで遊ぶ。しかしスマフは世界中で繋がっているということを勇者はまだ理解していなかった",
            )
