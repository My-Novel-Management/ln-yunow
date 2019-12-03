# -*- coding: utf-8 -*-
"""Main story.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.common.times import COMMON_TIMES
from config import PERSONS, CHARAS, STAGES, DAYS, TIMES, ITEMS, WORDS
from src.demo import ep_demo


## chapters
def ch_demo(w: World):
    return w.chapter("Demo",
            ep_demo(w),
            )

def ch_Iamhero(w: World):
    return w.chapter("勇者なう",
            )

def ch_gatherally(w: World):
    return w.chapter("仲間なう",
            )

def ch_destruction(w: World):
    return w.chapter("全滅なう",
            )

def ch_adventurechannel(w: World):
    return w.chapter("冒険チャンネルなう",
            )

def ch_goblin1(w: World):
    return w.chapter("ゴブリンの巣なう・１",
            )

def ch_goblin2(w: World):
    return w.chapter("ゴブリンの巣なう・２",
            )

def ch_popularman(w: World):
    return w.chapter("人気者なう",
            )

def ch_burnout(w: World):
    return w.chapter("炎上なう",
            )

def ch_heroismaou(w: World):
    return w.chapter("勇者が魔王なう",
            )

def ch_maou_coming(w: World):
    return w.chapter("魔王降臨なう",
            )

## main
def world():
    """Create a world.
    """
    w = World(2)
    w.set_times(COMMON_TIMES)
    w.set_db(PERSONS, CHARAS,
            STAGES, DAYS, TIMES,
            ITEMS,
            WORDS)
    return w

def story(w: World):
    return w.story("勇者なう！",
            ch_demo(w).omit(),
            ch_Iamhero(w),
            ch_gatherally(w),
            ch_destruction(w),
            ch_adventurechannel(w),
            ch_goblin1(w),
            ch_goblin2(w),
            ch_popularman(w),
            ch_burnout(w),
            ch_heroismaou(w),
            ch_maou_coming(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

