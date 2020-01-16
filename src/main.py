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
from storybuilder.assets import basic
## settings
from src.config import PERSONS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS
## local files


## NOTE:
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


## main
def create_world():
    """Create a world.
    """
    w = World("勇者なう！")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.buildDB(PERSONS,
            STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    w.setBaseDate(1020)
    # set persons
    # set stages
    # set blocks
    # set outline
    w.setOutline("スマフと呼ばれる魔法具を手に入れた勇者はそれを使って魔王退治に繰り出すはずだったが、何故か魔物たちに取り囲まれてしまう")
    return w

def main(): # pragma: no cover
    w = create_world()
    return w.build(
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

