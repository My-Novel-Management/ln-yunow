# -*- coding: utf-8 -*-
"""Episode: 1-2.教会なう
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## define alias
W = Writer
_ = W.getWho()


## scenes
def sc_church(w: World):
    hero = W(w.hero)
    yula = W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("教会にて",
            hero.come("教会を訪れる"),
            w.eventPoint("人物紹介", "$yula初登場"),
            yula.be("神父の代わりに、知らない女性がいる"),
            hero.talk("あのー、$clerc神父は？"),
            yula.talk("あ、えっとね、神父なら今旅行中だから、$meが代行しているのよ"),
            hero.talk("そうなんですか"),
            yula.look("普通の服装", "長い金髪を後ろでくくっている", "美人でスリム",
                "胸は大きい"),
            hero.talk("あの、お祈りいいすか？"),
            yula.talk("ええ、どうぞ"),
            hero.do("祈りの言葉を唱えて、手を合わせる"),
            hero.do("こう見えて$dadが失踪して以来、毎日帰ってくることを願って祈りを欠かさなかった"),
            w.comment("$yulaと話しておく"),
            )

def sc_explainsmaph(w: World):
    hero = W(w.hero)
    yula = W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$smaphの使い方",
            yula.be(),
            hero.be(),
            hero.do("$yulaから$smaphの使い方について少し教わる"),
            yula.talk("だからね、ここをこうして"),
            hero.talk("おお、すげえ！"),
            hero.do("画面にはずらずらと世界中の人の$w_tweetが流れてくる"),
            hero.do("その中にやけに「$w_Y」という文字が踊っている"),
            yula.talk("あれ？　なんかバズってるわね"),
            hero.talk("バズ？"),
            yula.talk("人気だってこと",
                "で、もういい？", "$meもそろそろ行かないと"),
            hero.talk("あ、どうもありがとうございました"),
            yula.go("出て行ってしまう"),
            hero.talk("あれ？　代行はいいの？"),
            )

def sc_followers(w: World):
    hero = W(w.hero)
    yula = W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("勇者のフォロワー",
            hero.do("見るとフォロワーというのが増えている"),
            hero.talk("なんだこれ？"),
            hero.do("$makoという知らない名前"),
            hero.talk("ま、いっか"),
            hero.do("市場に向かって歩き出す"),
            )

## episode
def ep_church(w: World):
    return w.episode("1-2.教会なう",
            sc_church(w),
            sc_explainsmaph(w),
            sc_followers(w),
            ## NOTE
            ##  - 教会にやってきて祈ろうとする
            ##  - 教会は神父代理という女性がいた
            ##  - 祈りを済ませて外に出る。勇者のフォローが増えていて喜ぶ
            )
