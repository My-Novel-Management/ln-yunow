# -*- coding: utf-8 -*-
"""Demo: chapter 06
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_collapsed(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("巣の崩壊", "かくてゴブリンの巣は崩壊した",
            he.run("逃げ出して"),
            # 全員それに倣う
            sol.talk("もうちょっと加減できねえのかよ！"),
            ma.talk("別にいいじゃないですか。やっちゃえって言ったの$n_solだろ"),
            yula.talk("お宝も全部埋まっちゃったじゃないの！"),
            ma.talk("$meだって爆薬があるなんて知ったらもっと手加減してましたー"),
            he.talk("とにかく依頼達成なんだから！"),
            he.look("地面がクレーター状になって崩れるのを"),
            sol.talk("まるでアリの巣だな。どうやってここまででかくなったんだ"),
            he.talk("でもみんな喜んでるぞ、すげーって"),
            he.look("スマフを"),
            he.be(doing="拡散されていくゴブリンの巣の崩落映像。だが衝撃写真として拡散中だ"),
            yula.talk("さすがにやっちゃったって感じ"),
            sol.talk("あ……"),
            sol.look("遠くの山が一つ、沈むのを"),
            sol.talk("お、$meは知らんからな"),
            he.talk("まあ、必要経費ってことで？"),
            he.do("そこに町長から連絡を受けて"),
            he.do("どうなってるんだ！　と叱られている"),
            he.talk("あ、いや、これには話すと長い事情が……"),
            )


## episode
def ep_demo_bustergoblin(w: World):
    return w.episode("ゴブリン討伐", "そして勇者たちはゴブリンの巣を壊滅させた（やりすぎ）",
            sc_collapsed(w),
            )
