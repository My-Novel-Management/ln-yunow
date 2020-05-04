# -*- coding: utf-8 -*-
"""Chapter 6: 第六章「ゴブリン退治なう！その１」
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
from src.c6_goblin1.e1_quest_gob import ep_quest_goblin
from src.c6_goblin1.e2_gobnest import ep_goblin_nest
from src.c6_goblin1.e3_destruction import ep_destruction

## define alias
W = Writer


## chapter
def ch06(w: World):
    return w.chapter("第六章「ゴブリン退治なう！その１」",
            ep_quest_goblin(w),
            ep_goblin_nest(w),
            ep_destruction(w),
            ## NOTE
            ##  - 冒険費用を稼ぐ為に真面目にクエストを受けることにした勇者たちはゴブリン退治をすることにした
            ##  - ゴブリンの巣に向かい、潜入する
            ##  - ゴブリンたちもスマフを活用していて、すぐに囲まれ、なぶり殺された
            note="ゴブリン退治前編。冒険費用を稼ぐ為に街道上に巨大な巣を建造しているゴブリン退治に出かけた勇者たちだったが",
            )
