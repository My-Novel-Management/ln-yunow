# -*- coding: utf-8 -*-
"""Chapter 10: 第十章「魔王なう！」
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
from src.c10_maoucoming.e1_confess import ep_confess
from src.c10_maoucoming.e2_hatemaju import ep_hatedaemon
from src.c10_maoucoming.e3_bustered import ep_bustered
from src.c10_maoucoming.e4_epilogue import ep_epilogue

## define alias
W = Writer


## chapter
def ch10(w: World):
    return w.chapter("第十章「魔王なう！」",
            ep_confess(w),
            ep_hatedaemon(w),
            ep_bustered(w),
            ep_epilogue(w),
            ## NOTE
            ##  - 魔子が自分が魔王だと告白し、ヘイトの魔獣を止める為には世界を再構成するしかないと言う
            ##  - 勇者はヘイトの魔獣はみんなの鬱憤だからストレス発散させようとガチャで大当たりさせようと提案
            ##  - ヘイトの魔獣はUR当てて霧散するが、魔子も同時に消えてしまった
            note="魔王だと告白した$mako。世界を滅ぼそうとしているヘイトの魔獣は倒せないと言うが、勇者はあることを提案した",
            )
