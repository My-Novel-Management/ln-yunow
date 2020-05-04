# -*- coding: utf-8 -*-
"""Chapter 4: 第四章「全滅なう！」
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
from src.c4_destruction.e1_trouble import ep_trouble
from src.c4_destruction.e2_mamazon import ep_mamazon
from src.c4_destruction.e3_destruction import ep_destruction

## define alias
W = Writer


## chapter
def ch04(w: World):
    return w.chapter("第四章「全滅なう！」",
            ep_trouble(w),
            ep_mamazon(w),
            ep_destruction(w),
            ## NOTE
            ##  - 買い物ならママゾンで済ませればいいと、魔子に教えてもらったママゾンで冒険用の買い物をする
            ##  - 次々と届く商品。段々と楽しくなってくる勇者たち
            ##  - 注文品の中に「魔王退治」を発見し、それを注文してみる。魔王が倒されたと報せがあったが、空は黒くなり、大魔王が出現した
            note="ママゾンで準備をし、いざ冒険出発と意気込む勇者たちだったが、あることに気づき、それを注文してみることにした",
            )
