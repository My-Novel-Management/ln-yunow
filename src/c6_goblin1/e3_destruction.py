# -*- coding: utf-8 -*-
"""Episode: 6-3.ゴブリン退治なう
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
def sc_runaway(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("逃げろ",
            hero.talk("逃げよう"),
            sol.talk("は？　どうやって？"),
            hero.talk("わかんないけど……あ、いや、これ今こっちに集まってるから、",
                "$makoと同じように入り口側なら抜けられるよ！",
                "ほら、ここ薄いだろ？"),
            sol.talk("十匹ってところか",
                "それなら何とかなるかもな",
                "$k_makoには一人で逃げるよう言っとけ"),
            hero.talk("こっちも逃げるって伝えといた"),
            sol.talk("それじゃ、始めるか"),
            sol.do("目の前$goblinを殴りつけておいて、背を向けて逃げ出す"),
            hero.do("$Sも武器が引き抜けないながら、慌てて後を追う"),
            hero.do("森の中をとにかく逃げていく$Sたち"),
            )

def sc_no_wayout(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("逃げ道がない",
            hero.do("多いところを避けて、とにかく森から出ようと走る"),
            sol.talk("おい、$k_hero！", "今度はどっちだ！"),
            hero.do("また前に$goblinが現れた"),
            hero.do("$smaphを見て考え込む"),
            sol.talk("おい、来るぞ！"),
            hero.talk("西だ！"),
            hero.do("慌てて逃げ出す$Sたち"),
            hero.do("しかし、どこに逃げても自分たちが囲まれてしまう"),
            hero.do("$makoから連絡が入り、どうやらこちらの位置情報が相手にバレているらしいと判明する"),
            sol.talk("おい、$k_hero",
                "その$smaphを捨てろ",
                "そいつがあるから位置特定されるんだろ？", "だったら捨てればバレない"),
            hero.talk("す、捨てるなんてできないって！"),
            sol.talk("殺されてもいいのか？"),
            hero.talk("嫌だ。絶対無理"),
            hero.think("じっと地図をにらみ、何とか解決策がないか考える"),
            hero.talk("あ、$sol", "ここに湖がある"),
            sol.talk("そうだが？"),
            hero.talk("飛び込もう", "そうすれば奴ら追ってこられない"),
            sol.talk("無理だよ！"),
            hero.talk("なんで？"),
            sol.talk("$me、泳げないんだ"),
            )

def sc_gotolake(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("湖に飛び込め",
            hero.do("何とか無理矢理に言いくるめて、湖の方に逃げる$S"),
            sol.talk("$meが溺れ死んだら一生お前を恨んでやるからな！"),
            hero.talk("浅いから大丈夫だって！", "それより来るぞ"),
            hero.do("武器を持った$goblinの群れが見える"),
            hero.talk("見えた"),
            hero.do("茂みを抜けた先に湖が広がる"),
            sol.talk("ええい！"),
            sol.do("思い切って飛び込む"),
            hero.do("$Sも続く"),
            hero.think("これで安心だ、と思った矢先"),
            hero.do("背中に痛みを感じる",
                "見ると胸側に槍が突き出ていて、血が流れた"),
            hero.think("そんなことって……"),
            hero.do("$Sは気を失い、沈んでいった"),
            )

## episode
def ep_destruction(w: World):
    return w.episode("6-3.ゴブリン退治なう？",
            sc_runaway(w),
            sc_no_wayout(w),
            sc_gotolake(w),
            ## NOTE
            ##  - 退治をやめて一旦逃亡することに
            ##  - どんなに逃げても囲まれるので何とか逃げる方法を考えると、湖が浮かぶ
            ##  - ゴブリンに囲まれた中で、湖に潜って逃げようとしたが、背中に槍を投げ込まれて勇者は死んだ
            )
