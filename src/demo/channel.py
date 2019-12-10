# -*- coding: utf-8 -*-
"""Demo: chapter 04
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_retired(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("引退します", "あまりに閑古鳥なので勇者はユーチューバーを諦めた",
            he.look("何度も自分のチャンネルを"),
            he.talk("駄目だぁ……"),
            he.isa("全然数字が増えていないの"),
            sol.talk("まあこの手はそう簡単にはうまくいかないって"),
            yula.talk("だいたいなんで今更こんなせこい日銭稼ぎしなきゃならないの？"),
            he.remember("勇者の印を売り払ったことを"),
            he.talk("あ、いやさ、色々いりようでさ"),
            sol.talk("そ、そうだよな。勇者っつったってただの冒険者だからさ"),
            he.hear(doing="どちらの声も上擦っている"),
            he.talk("とにかくこれじゃ駄目だな"),
            ma.talk("別にいいじゃないですか。そもそも$fn_hero様は$meだけが見てればいいんですから"),
            he.talk("とにかく冒険は始まったんだ。まだまだこれからさ！"),
            he.walk(),
            he.look(doing="行く手には広大なフィールドが広がっていた"),
            )

## episode
def ep_demo_channel(w: World):
    return w.episode("冒険チャンネル", "勇者は金稼ぎの為に冒険チャンネルを始めた",
            sc_retired(w),
            )
