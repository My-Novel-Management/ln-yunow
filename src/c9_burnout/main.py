# -*- coding: utf-8 -*-
"""Chapter 9: 第九章「炎上なう！」
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
from src.c9_burnout.e1_fakenews import ep_fakenews
from src.c9_burnout.e2_burnout import ep_burnout
from src.c9_burnout.e3_birthmaju import ep_birth_maju

## define alias
W = Writer


## chapter
def ch09(w: World):
    return w.chapter("第九章「炎上なう！」",
            ep_fakenews(w),
            ep_burnout(w),
            ep_birth_maju(w),
            ## NOTE
            ##  - 勇者が魔王だったというフェイクニュースにより、勇者は引きこもる
            ##  - しかし世間は勇者を許さず、次々と居場所を暴かれ、SNSにアップされる
            ##  - 遂には山に籠もった勇者。民衆のヘイトは収まらず、遂にその感情はヘイトの魔獣を生み出した
            note="勇者が魔王だったというフェイクニュースにより大炎上し、ヘイトの魔獣が誕生する",
            )
