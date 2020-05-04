# -*- coding: utf-8 -*-
"""Chapter 5: 第五章「冒険者チャンネルなう！」
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
from src.c5_adv_channel.e1_howtomoney import ep_howto_money
from src.c5_adv_channel.e2_setup_channel import ep_setup_channel
from src.c5_adv_channel.e3_giveup import ep_giveup

## define alias
W = Writer


## chapter
def ch05(w: World):
    return w.chapter("第五章「冒険者チャンネルなう！」",
            ep_howto_money(w),
            ep_setup_channel(w),
            ep_giveup(w),
            ## NOTE
            ##  - 目覚めた勇者はママゾンを使うことを避け、真面目に冒険費用を稼ごうと考える
            ##  - 実況チャンネルを開設し、そこで人気実況者となって儲けようとする
            ##  - しかし人気どころか視聴者数も伸びず、散々罵倒され、チャンネルで儲けることは諦めた
            note="冒険費用を稼ぐ為に楽に稼げるという実況者チャンネルを開設し、色々試行錯誤する勇者たちだったが",
            )
