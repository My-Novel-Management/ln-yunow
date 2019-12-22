# -*- coding: utf-8 -*-
"""Episode: chapter 09
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
W = Writer


## scenes
def sc_runaway(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("逃亡勇者", "勇者は$n_solたちの前から逃げ出してしまった",
            he.talk("も、もう無理だ……"),
            sol.talk("とにかくさっさと謝っちまえって。ちょっといい気になりましたって"),
            he.talk("だって魔王にされてるじゃないか！　こんなん無理だよ！"),
            he.go(),
            ma.talk("太郎様！"),
            sol.talk("ほっとけよ。どうせそこらで見つかってぼこされる"),
            ma.talk("けど……$meやっぱり行きます"),
            ma.go(),
            yula.talk("ちょっとつれないんじゃない？　親友でしょ？"),
            sol.talk("そういうんじゃねえし、まだ一月ばかりの付き合いだからな"),
            sol.talk("それにしても、こっちこそどうすんだ？"),
            sol.look("勇者の家の前には沢山の人混みが"),
            yula.talk("一応お母様だけは神父さんのところにかくまってもらったけどさ"),
            yula.do("苦笑"),
            sol.talk("やっぱ$meも探すわ。あいつ引っ張り出して謝らせるのが一番だろ？"),
            yula.talk("$meは絶対行かないからね"),
            )

def sc_vanishhero(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("消えた勇者", "炎上が怖くなり、ついには仲間たちの前から姿を消す勇者",
            sol.talk("なあ、いたか？"),
            ma.talk("全然"),
            yula.talk("あいつ、これ置いてったから、探せないわ"),
            yula.have("勇者のスマフを"),
            ma.talk("通りで反応しないはずです"),
            ma.look("自分のスマフの追跡アプリを"),
            ma.talk("どこか心当たりは……あっ"),
            sol.talk("ん？　どした？"),
            ma.talk("一箇所だけ、思い当たるところがあるんですよ"),
            ma.talk("太郎様がずっと勇者を目指して剣の練習をしていた、近所の森に、横穴があるんです"),
            sol.talk("なんでそんなこと知ってんだ？"),
            ma.talk("$me、太郎様のストーカーですから！"),
            )

def sc_indooryusha(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("発見された勇者は", "勇者は思い出の洞窟で引きこもりになっていた",
            he.talk("もう嫌なんだよ！　結局どこにいったって見つかるし、誰もかも繋がってる世界なんか沢山だ！"),
            ma.talk("ここは$meだから見つけられただけですって"),
            sol.talk("こいつ完全に駄目モードだろ"),
            yula.talk("でもさ、一生ここに閉じ籠もってる訳にもいかないでしょ？"),
            he.talk("変装とかすればいいのかな。なあ？"),
            sol.talk("じゃあ山田花子としてでも生きてくってか？"),
            he.talk("もうそれでいいよ"),
            ma.do("溜息"),
            sol.do("落ちているスマフを拾って見ている"),
            sol.talk("しかし何で魔王だなんて言われてるんだ？"),
            ma.talk("これじゃないですか？"),
            ma.do("指摘する"),
            sol.look(doing="アプリ乗っ取りで「魔王」として呟いている画像が貼り付けられている"),
            sol.talk("あいつ何やってんだよ……"),
            )

## episode
def ep_yusha_indoor(w: World):
    return w.episode("そして引きこもり", "勇者は引きこもりになってしまった",
            sc_runaway(w),
            sc_vanishhero(w),
            sc_indooryusha(w),
            )
