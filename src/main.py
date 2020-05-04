#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main story.
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## assets
from storybuilder.assets import basic, accessory
## settings
from src.config import PERSONS, AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS
## local files
from src.c1_iamhero.main import ch01
from src.c2_gatherally.main import ch02
from src.c3_preparation.main import ch03
from src.c4_destruction.main import ch04
from src.c5_adv_channel.main import ch05
from src.c6_goblin1.main import ch06
from src.c7_goblin2.main import ch07
from src.c8_popularman.main import ch08
from src.c9_burnout.main import ch09
from src.c10_maoucoming.main import ch10

## define alias
W = Writer

################################################################
##  章構成
##  1. 勇者なう
##  2. 仲間なう
##  3. 準備なう
##  4. 全滅なう
##  5. 冒険チャンネルなう
##  6. ゴブリンの巣なう・その１
##  7. ゴブリンの巣なう・その２
##  8. 人気者なう
##  9. 炎上なう
##  10. 魔王なう
################################################################


## main
def create_world():
    """Create a world.
    """
    w = World("勇者なう！")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.setAssets(accessory.ASSET)
    w.buildDB(PERSONS,
            AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    w.setBaseDate(1020)
    w.setBaseArea("Nethgard")
    # set persons
    # set stages
    # set blocks
    w.setOutline("スマフと呼ばれる魔法具を手に入れた勇者はそれを使って魔王退治に繰り出すはずだったが、何故か魔物たちに取り囲まれてしまう")
    return w

def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch01(w),
            ch02(w),
            ch03(w),
            ch04(w),
            ch05(w),
            ch06(w),
            ch07(w),
            ch08(w),
            ch09(w),
            ch10(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

