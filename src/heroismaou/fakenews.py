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
def sc_firstcomplaint(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("最初の苦情", "人気爆発の勇者の許に一通の苦情が",
            he.talk("いやあ、人気者ってすごいな"),
            he.remember("城での姫様の対応を"),
            he.talk("このまま姫様と結婚とかなったら、本気で世界救っちゃうよ"),
            sol.talk("なあ。質問なんだが……これ何だ？"),
            sol.do("スマフを触らせてもらっていた$Sが疑問を"),
            he.talk("ん？"),
            he.find("書き込みに勇者に酷いことを言われたというのを"),
            he.talk("あの時の子だけど、こんなこと言ってないのになあ"),
            he.find("続いて投稿されている勇者の悪口を"),
            he.talk("ま、いっか"),
            he.talk("今日は何食べる？　金ならあるんだ"),
            sol.talk("そんな無駄金使ってていいのか？"),
            he.talk("ほら見ろよ。勇者ってだけでどんどん貢いでくれるんだから。ここに欲しいものリスト出しとけば、家にばんばん贈り物くるんだよ。勇者さいこー！"),
            sol.do("苦笑する"),
            )

def sc_stoing(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("投石騒動", "知らない人に石を投げられたり。徐々にエスカレート",
            he.walk(),
            he.feel("痛みを"),
            he.have("小石を"),
            sol.talk("何やってんだ！"),
            sol.look("逃げていく子どもを"),
            he.talk("最近さ、結構あるんだ"),
            he.talk("ほらこれ"),
            sol.look("スマフを"),
            he.talk("なんかやたら悪口が来るようになってさ。全部ブロックだよ"),
            sol.talk("お前、最近寝てないのか？"),
            he.talk("いや、見てたらなんか書いてあるから、つい……いっぱいあるんだ。$meの悪口が"),
            he.talk("別に好きで人気者になった訳じゃないのにさ"),
            )

def sc_heroismaou(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("勇者が魔王だった？", "何故か勇者が魔王だったことになり炎上",
            he.talk("は？　なんで$meが魔王なの？"),
            sol.talk("いや、だって、これ見てみろって"),
            he.look(doing="スマフには勇者が魔王となり、魔王軍を指揮している画像が出回る"),
            he.talk("こんなの全部でたらめだよ。誰かの悪戯だろ？"),
            sol.talk("けどヤッホーニュースにもなってやがるからな"),
            he.talk("なんですと！"),
            he.check(),
            he.do("溜息"),
            he.talk("$meなんか悪いことした？　ただスマフで遊んでただけじゃないか"),
            ma.come(),
            ma.talk("なんか家の前にすごい人だかりなんですけど？"),
            he.talk("え？"),
            )

## episode
def ep_fakenews(w: World):
    return w.episode("フェイクニュース", "勇者が魔王だったと広まって",
            sc_firstcomplaint(w),
            sc_stoing(w),
            sc_heroismaou(w),
            )
