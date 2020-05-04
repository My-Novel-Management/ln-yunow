# -*- coding: utf-8 -*-
"""Chapter 2: 第二章「仲間なう！」
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
from src.c2_gatherally.e1_restart import ep_re_church
from src.c2_gatherally.e2_gather import ep_bar
from src.c2_gatherally.e3_ally import ep_ally

## define alias
W = Writer


## chapter
def ch02(w: World):
    return w.chapter("第二章「仲間なう！」",
            ep_re_church(w),
            ep_bar(w),
            ep_ally(w),
            ## NOTE
            ##  - 教会で目覚めた勇者は、神父が戻っていることを不思議に思う。夢を見ていたと思い、再び仲間探しに向かう
            ##  - 酒場は子どもだからと追い出され、仕方なく街を歩いて探すと、空腹で倒れている野良戦士を拾った
            ##  - 家を飯を食べさせているところに客が訪れる。勇者をストーキングしてきたという魔法使いの少女だった
            note="目覚めた勇者は再度、仲間を集めようと声を掛けて回る",
            )
