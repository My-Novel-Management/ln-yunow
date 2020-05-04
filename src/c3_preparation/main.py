# -*- coding: utf-8 -*-
"""Chapter 3: 第三章「準備なう！」
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
from src.c3_preparation.e1_foradventure import ep_ready
from src.c3_preparation.e2_preparation import ep_shopping
from src.c3_preparation.e3_poor import ep_poor

## define alias
W = Writer


## chapter
def ch03(w: World):
    return w.chapter("第三章「準備なう！」",
            ep_ready(w),
            ep_shopping(w),
            ep_poor(w),
            ## NOTE
            ##  - ソルと魔子を仲間にし、冒険の準備を整えることにする勇者たち
            ##  - 街の市場や商店街を見て歩くが、所持金が少なく、なかなか思うように道具を揃えられない
            ##  - 結局金がなくて困る勇者。しかし魔子は「困りましたね」と自分だけ豪華な食事を注文していてみんなが注目する
            note="冒険準備を整える為、城下町の市場や商店街を回る",
            )
