# -*- coding: utf-8 -*-
"""Episode: epilogue (chapter10)
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_afterworld(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("目覚めた勇者だが", "勇者は目覚める、再び教会で",
            he.awake(),
            he.look("教会を"),
            he.talk("なんで？"),
            sol.come(),
            yula.come(),
            sol.talk("何してんだよ、さっさと"),
            he.talk("$n_makoは？"),
            yula.talk("誰よそれ？"),
            )

def sc_vanishmako(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("魔子が消えた", "街中探すが魔子は見つからなかった",
            he.walk("魔子を探して"),
            he.talk("おーい"),
            he.have("彼女のブローチを持っている"),
            he.talk("どうしたんだよ"),
            sol.talk("ほんとにそんなやついたのか？"),
            he.talk("いたも何も……"),
            yula.talk("まあちょっと変なのよね……ほら"),
            yula.look("スマフを"),
            he.look("画面にはヘイトの魔獣の痕跡らしきものが残る"),
            he.talk("これ、でっかい魔獣が壊してったんだよ、ほんとに"),
            yula.talk("なんか遥か昔の出来事だって書いてあるわよ？"),
            he.talk("どういうことなんだ……"),
            )

def sc_re_adventure(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("魔子探しに旅に", "魔王を探す旅に出る勇者たち",
            he.come("戻って"),
            he.talk("これしかなかった"),
            he.have("彼女のブローチを"),
            he.talk("でもこれがあるってことはこの世界にいるってことだよね"),
            sol.talk("そうだよな"),
            yula.talk("ならなんで出てこないの？"),
            he.look(doing="スマフを見せる"),
            he.display(doing="アカウントが削除されていると表示"),
            he.talk("ほんとにいるんだろうか。あんなにこれに依存してたのに"),
            sol.talk("そうだな"),
            yula.talk("何かトラブルにあってるかもよ"),
            he.talk("そっか"),
            sol.talk("しゃーねーなあ。探しに行くか"),
            he.talk("あ。やっと旅立ち？"),
            sol.talk("魔王を探す旅だ"),
            sol.smile(),
            he.laugh(),
            yula.talk("全然ないけどね、金が"),
            he.talk("それもいいさ"),
            he.go(doing="出かける"),
            he.go(doing="初めての冒険に旅立った"),
            )

## episode
def ep_epilogue(w: World):
    return w.episode("エピローグ", "全てが無事に終わったはずだった",
            sc_afterworld(w),
            sc_vanishmako(w),
            sc_re_adventure(w),
            )
