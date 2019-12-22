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
from src.demo.demo import ep_demo
from src.demo.alldead import ep_demo_alldead
from src.demo.ally import ep_demo_ally
from src.demo.burnout import ep_demo_burnout
from src.demo.channel import ep_demo_channel
from src.demo.goblin1 import ep_demo_goblinnest
from src.demo.goblin2 import ep_demo_bustergoblin
from src.demo.maouconfess import ep_demo_confess
from src.demo.popular import ep_demo_popular
from src.demo.yusha import ep_demo_yushanow
from src.demo.yushamaou import ep_demo_yusha_is_maou
from src.heroismaou.birthdaemon import ep_birth_daemon
from src.heroismaou.fakenews import ep_fakenews
from src.heroismaou.stayindoor import ep_yusha_indoor
from src.maoucoming.epigloue import ep_epilogue
from src.maoucoming.maju_gacha import ep_gacha
from src.maoucoming.maouconfess import ep_confession


## chapters
def ch_demo(w: World):
    return w.chapter("Demo",
            ep_demo(w).omit(),
            )

def ch_Iamhero(w: World):
    return w.chapter("勇者なう",
            ep_demo_yushanow(w).omit(),
            )

def ch_gatherally(w: World):
    return w.chapter("仲間なう",
            ep_demo_ally(w).omit(),
            )

def ch_destruction(w: World):
    return w.chapter("全滅なう",
            ep_demo_alldead(w).omit(),
            )

def ch_adventurechannel(w: World):
    return w.chapter("冒険チャンネルなう",
            ep_demo_channel(w).omit(),
            )

def ch_goblin1(w: World):
    return w.chapter("ゴブリンの巣なう・１",
            ep_demo_goblinnest(w).omit(),
            )

def ch_goblin2(w: World):
    return w.chapter("ゴブリンの巣なう・２",
            ep_demo_bustergoblin(w).omit(),
            )

def ch_popularman(w: World):
    return w.chapter("人気者なう",
            ep_demo_popular(w).omit(),
            )

def ch_burnout(w: World):
    return w.chapter("炎上なう",
            ep_demo_burnout(w).omit(),
            )

def ch_heroismaou(w: World):
    return w.chapter("勇者が魔王なう",
            ep_demo_yusha_is_maou(w).omit(),
            # NOTE:
            #   フェイクニュースで勇者が魔王だったとして更に炎上
            #   勇者は隠れ家に引きこもる
            #   ヘイトの魔獣誕生、魔子が「話がある」と言い出す
            ep_fakenews(w),
            ep_yusha_indoor(w),
            ep_birth_daemon(w),
            )

def ch_maou_coming(w: World):
    return w.chapter("魔王降臨なう",
            ep_demo_confess(w).omit(),
            # NOTE:
            #   魔王告白
            #   世界の再構築を
            #   勇者の許し、冒険はこれからだ
            ep_confession(w),
            ep_gacha(w),
            ep_epilogue(w),
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

