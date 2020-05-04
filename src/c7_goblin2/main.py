# -*- coding: utf-8 -*-
"""Chapter 7: 第七章「ゴブリン退治なう！その２」
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
from src.c7_goblin2.e1_retry import ep_retry
from src.c7_goblin2.e2_changednest import ep_changed_nest
from src.c7_goblin2.e3_destory import ep_destroy

## define alias
W = Writer


## chapter
def ch07(w: World):
    return w.chapter("第七章「ゴブリン退治なう！その２」",
            ep_retry(w),
            ep_changed_nest(w),
            ep_destroy(w),
            ## NOTE
            ##  - ゴブリンに襲われてやられた勇者は、復活して再びゴブリン退治に挑む
            ##  - しかしゴブリンの巣は巨大な城壁に変わり果てていた
            ##  - ゴブリンの巣は魔子の魔力暴発により破壊され、ダムになっていた巣は壊れ、下流域は全て被害を被った
            note="ゴブリン退治後編。対策をして再度ゴブリン退治に挑む勇者たち。しかしゴブリンの巣の構造が変わっていて",
            )
