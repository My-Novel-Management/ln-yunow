# -*- coding: utf-8 -*-
"""Chapter 8: 第八章「人気者なう！」
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
from src.c8_popularman.e1_buzz import ep_buzz
from src.c8_popularman.e2_popular import ep_popular
from src.c8_popularman.e3_kingparty import ep_party_incastle

## define alias
W = Writer


## chapter
def ch08(w: World):
    return w.chapter("第八章「人気者なう！」",
            ep_buzz(w),
            ep_popular(w),
            ep_party_incastle(w),
            ##  NOTE
            ##  - 次の資金稼ぎバイトを探していたら、ゴブリン退治動画が大反響になっていると知る
            ##  - 配信者として一躍トップスターになる
            ##  - 人気者として王宮のパーティに招待された（しかしそこで多くの嫉妬も集める）
            note="ゴブリンを退治した動画が大ヒットし、一躍人気者になった勇者たち。王宮に招かれてパーティに参加する",
            )
