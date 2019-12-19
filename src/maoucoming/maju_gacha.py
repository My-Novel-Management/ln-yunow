# -*- coding: utf-8 -*-
"""Episode: daemon's gacha (chapter10)
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_breakthrough(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    return w.scene("URを手に入れろ", "魔獣は次々とガチャを回す",
            maju.walk(),
            he.look("魔獣の歩くのを"),
            yula.look("スマフを"),
            yula.talk("こっちに来るのも時間の問題ね"),
            sol.talk("ほんとにお嬢の言う通りにするしか"),
            ma.talk("太郎様？"),
            he.talk("なあ"),
            he.do("提案する"),
            he.talk("あれってさ、みんなの鬱屈した感情なんだろ？"),
            he.talk("だったらあれみたいにさ、ゲームでもやって解消すればいいんじゃないか？"),
            sol.talk("タロ、何ばかなこと"),
            ma.talk("ガチャってことですか？"),
            he.talk("そう、それだよ！　憎悪なんか吹き飛ぶと思うんだ"),
            ma.talk("連絡してみます"),
            ma.do("スマフで部下に連絡している"),
            ma.talk("来月実装予定だったのがあるって……けど、ほんとに"),
            he.talk("それで駄目ならそん時はその魔王の石を使うさ"),
            ma.talk("じゃあ"),
            )

def sc_majugacha(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    return w.scene("魔獣ガチャ", "魔獣はガチャをやりはじめた",
            ma.talk("ほんとにいいんですね？"),
            he.talk("ああ、頼む"),
            ma.do("連絡を入れる"),
            he.look("空から魔王軍が巨大なスマフを魔獣に与えるのを"),
            sol.talk("はじめやがった"),
            yula.talk("あんなでもスマフ触れるんだ……"),
            he.look("動きが止まり、その場で端末を触るのを"),
            he.talk("いいぞ……やるんだ"),
            maju.do("ガチャを始める"),
            )

def sc_getUR(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    return w.scene("手に入れたUR", "ついにURを出した魔獣は消滅する",
            he.look("魔獣を"),
            he.talk("なんか、小さくなってる？"),
            he.notice("立ち止まっている魔獣が徐々に小さくなっているのに"),
            sol.talk("あいつ、まさかはまってんのか、ほんとに？"),
            yula.talk("さすが人間だけじゃないってことかい"),
            he.look("結果に一喜一憂する魔獣を"),
            he.talk("調整して出せないの？"),
            ma.talk("必死にやってるみたいなんですけど、なんか魔獣のパワーがすごいらしくて"),
            he.talk("出やすくするんじゃなくて、もっと詫び石を配るんだ"),
            ma.talk("え？　けど"),
            he.talk("$meには分かる。あいつの気持ちが。もっと回したいんだ！"),
            ma.talk("分かりました！"),
            he.move("魔獣の近くへと"),
            sol.talk("おい！　何やってんだよ！"),
            he.talk("あいつ、応援してくる！"),
            sol.do("頭を抱える"),
            he.talk("もっと集中して、ここぞってところで引くんだ！　そうだ！　いいぞ！"),
            he.feel(doing="いつしか魔獣と通じ合う"),
            he.do("魔獣とともにガチャを回す勇者"),
            he.do("遂に引き当てた"),
            maju.cry(),
            he.cry(),
            maju.do("消えた"),
            he.look("世界を覆う光を"),
            )

## episode
def ep_gacha(w: World):
    return w.episode("魔獣とガチャ", "かくして魔獣はガチャを回す",
            sc_breakthrough(w),
            sc_majugacha(w),
            sc_getUR(w),
            )
