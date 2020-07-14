#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main story
==========
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 1K * 10
#   4. Spec
#   5. Plot         - 1/4: 2.5K * 10
#   6. Scenes
#   7. Conte        - 1/2: 5K * 10
#   8. Layout
#   9. Draft        - 1/1: 10K * 10
#
################################################################


# Constant
TITLE = "勇者なう"
MAJOR, MINOR, MICRO = 2, 2, 0
COPY = "勇者はスマフを手に入れた！"
ONELINE = "色々なアプリが使えるスマフという魔道具を使い、魔王を見つけて退治すべく奮闘する勇者とその仲間たちの冒険譚"
OUTLINE = "お城に呼び出されたタロウはスマフを貰い、勇者の称号を授けられる。魔王退治を命じられたタロウはスマフを駆使して仲間と共に冒険の旅に出ようとするが"
THEME = "便利な道具を使っても、自分で努力しないと目的は達成されない"
GENRE = "ファンタジィ"
TARGET = "10-20台（男）"
SIZE = "100K"
CONTEST_INFO = ""
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
RELEASED = (7, 12, 2020)


# Note
def abstract(w: World):
    return w.writer_note("概要",
            "お城に呼ばれ、スマフと呼ばれる魔道具を与えられ、勇者の称号を得た若者は魔王退治を命じられる",
            "$heroは言われたように仲間を集めて冒険の旅に出ようとするが、様々なアプリの誘惑に負け、またそれが災難を呼び、何度も死ぬことになる",
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_released(*RELEASED)
    return w.run(
            abstract(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

