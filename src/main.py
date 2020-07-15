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
#   3. Structure    - 1/8: 1K * 10 (10K)
#   4. Spec
#   5. Plot         - 1/4: 2.5K * 10 (25K)
#   6. Scenes
#   7. Conte        - 1/2: 5K * 10 (50K)
#   8. Layout
#   9. Draft        - 1/1: 10K * 10 (100K)
#
################################################################


# Constant
TITLE = "勇者なう"
MAJOR, MINOR, MICRO = 2, 2, 1
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


# Episodes
def ch_main(w: World):
    return w.chapter("main stroy",
            "冒頭",
            w.plot_note("$heroはお城に呼び出され、そこで$smaphを渡され、勇者の称号を与えられる"),
            w.plot_note("魔王を探し出して退治し、世界に平和を取り戻すことを命じられた$hero"),
            w.plot_note("$smaphを使い、冒険に必要なものを一つ一つ揃えていく$hero"),
            w.plot_note("しかし$smaphの$tweetにより魔物たちに見つけられ、なぶり殺しに遭ってしまう"),
            w.plot_note("死んだと思った$heroは教会で目覚める"),
            w.plot_note("教会ではあの金髪の女性ではなく、旅に出たはずの神父がいた"),
            "仲間",
            w.plot_note("$heroは酒場に仲間集めに向かう"),
            w.plot_note("酒場では子ども扱いされたが、酒場の女店主$aidaに何とか話を聞いてもらえる"),
            w.plot_note("逃げ出した元英雄として汚名を負っている$heroの父のことを、彼女はよく知っていた"),
            w.plot_note("傭兵ギルドに口利きしてもらえることになる"),
            w.plot_note("傭兵を雇う資金がなく、ひとまず諦める$hero"),
            w.plot_note("しかし偶然から、傭兵志願者だった$solに夕飯をご馳走する羽目になり、結果、彼を仲間とすることができた"),
            "$makoとの初対面",
            w.plot_note("突然$heroの家を尋ねてきた魔法使いの少女$mako"),
            w.plot_note("彼女は誰が開設したのか分からない$heroチャンネルを見て、ファンになってやってきたと言った"),
            w.plot_note("結婚を申し込まれたが、$heroはアイドルの$yuiが好きだったので断る"),
            w.plot_note("ともかく$solと$makoの三人で魔王退治の旅に出ることになった"),
            "冒険準備",
            w.plot_note("$amazonを利用してみて、その便利さに驚く$hero"),
            w.plot_note("$amazonで魔王退治を依頼すると、魔王が退治され、大魔王が出現した"),
            w.plot_note("魔王軍の全面攻撃により、世界は滅んでしまった"),
            "初めてのクエスト",
            w.plot_note("冒険準備を整える為に冒険者ギルドで適当なクエストを受注し、お金を稼ごうとする$hero"),
            w.plot_note("しかし実績がない冒険者登録したての$heroが受注可能なものがなく、おつかいをこなすことに"),
            w.plot_note("何とか実績を詰み、初めてのクエストに出るが、ゴブリン退治といういきなり難易度が高いものを選択"),
            w.plot_note("森に巣食ったゴブリンを退治しに出かけるが、逆に囲まれて、逃げ出す羽目になる"),
            w.plot_note("死に戻り、再度ゴブリンのクエストにチャレンジする$hero"),
            w.plot_note("しかし今度はゴブリンたちは川の上に巨大な要塞を築いてダムにしてしまっていた"),
            w.plot_note("$heroはやめて帰ろうとしたが、その要塞に捕まえられて入っていく$yulaを見て助け出すと言う"),
            w.plot_note("$yulaはわざと捕まっただけだった"),
            w.plot_note("今度は$makoが捕まったらしく、$yulaを加えた三人で彼女を救出に向かう"),
            w.plot_note("要塞の最深部で$makoがボスのゴブリンと何か交渉している"),
            w.plot_note("$makoの魔力が暴発し、施設は崩壊し、大洪水になってしまった"),
            "人気配信者になる",
            w.plot_note("損害分で大赤字になり、結局地道に肉体労働をして金を返すことになった$heroたち"),
            w.plot_note("ある日、放置していた$hero_chが急に人気になる"),
            w.plot_note("どうやらアイドルの$yuiが、この前のゴブリン要塞崩壊の動画を見てそれがバズっていた"),
            w.plot_note("放送局から取材申込みがある"),
            w.plot_note("そこから無茶なクエストを$heroがやる企画が持ち上がり、それが大人気番組になる"),
            w.plot_note("人気者となった$heroは、城に招かれる"),
            w.plot_note("城で姫と再会した$heroは、姫にも言い寄られる"),
            "$makoの失恋",
            w.plot_note("アイドルの$yuiと一緒に仕事をすることが増えた$hero"),
            w.plot_note("彼女に自分が勇者だと打ち明け、急速に距離を縮める$hero"),
            w.plot_note("失恋した$makoは$heroたちの前から姿を消してしまう"),
            w.plot_note("突如、魔物が凶暴化し、街を襲い始める"),
            "魔王降臨",
            w.plot_note("魔王の正体が$makoだったと判明するが、"),
            "ラストエピソード",
            w.plot_note("気づくと$heroは教会の中にいた"),
            w.plot_note("すぐに$makoを探すがどこにもいない", "$solや$yulaはそんな女は知らないという"),
            w.plot_note("街中探したがどこにも$makoはいなかった"),
            w.plot_note("また、魔王のことを誰も知らないと言う", "この世界から完全に魔王が消えてしまったのだ"),
            w.plot_note("$heroは$solと$yulaと共に、消えた$makoを探す旅に出る"),
            )


# Note
def writenote(w: World):
    return w.writer_note("作者覚書",
            )

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
            writenote(w),
            abstract(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

