# -*- coding: utf-8 -*-
"""Config: the yusha now
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


# configs
PERSONS = (
        # main
        ("taro", "勇者", "勇者,太郎", 16, "male", "勇者", "me:俺"),
        ("sol", "ソル", "ライアル,ソル", 18, "male", "戦士", "me:オレ"),
        ("mako", "魔子", "魔王,魔子", 16, "female", "魔法使い", "me:僕"),
        ("yula", "ユラ", "ダコタ,ユラ", 25, "female", "盗賊", "me:アタシ"),
        # sub
        ## family
        # mob
        # extra
        )

CHARAS = (
        )

STAGES = (
        # Area
        # Place
        # Ride
        # Part
        )

DAYS = (
        # main
        ("current", "現在", 4,1, 1019),# NOTE: 架空年代
        # sub
        )

TIMES = (
        ("earlymorning", "早朝", 6,0),
        ("morning", "朝", 8,0),
        ("inmorning", "午前", 10,0),
        ("noon", "正午", 12,0),
        ("afternoon", "午後", 14,0),
        ("evening", "夕方", 17,0),
        ("night", "夜", 20,0),
        ("deepnight", "深夜", 2,0),
        )

ITEMS = (
        # main
        # sub
        )

WORDS = (
        )

