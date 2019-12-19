# -*- coding: utf-8 -*-
"""Episode: maou confession (chapter10)
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_worlddestruction(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    return w.scene("魔獣による世界破壊", "世界はどんどん破壊されていく",
            he.look("魔獣が世界を壊すのがスマフに映っているのを"),
            ma.talk("ついに、破壊が始まった"),
            ma.talk("もうこうなったらどうしようもないんだ"),
            ma.talk("お父様は最初からこれを狙ってたんだよ！"),
            he.talk("どういうことなんだ？"),
            ma.talk("実は$me、大魔王の子どもなんだ……"),
            )

def sc_confession(w: World):
    he, ma, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    return w.scene("魔子の告白", "魔子は自分が魔王だと勇者たちに話す",
            ma.talk("実は$me、大魔王の一人娘で"),
            he.talk("どういうこと？"),
            ma.talk("この世界を与えられて、適当に遊んでたら、色々滅んじゃって"),
            ma.talk("でもこの石があれば何度も作り直せるからって"),
            ma.have("小さなサイコロを"),
            ma.talk("そのうちに色々な世界を壊すのにも飽きて、$meはある日、世界を見て回ったんだ"),
            ma.talk("楽しそうな人たちがいて、それを見守るために、これを作った"),
            ma.look("手にしたスマフを"),
            yula.talk("それじゃあこれってもともと魔王軍が開発したものだったの？"),
            ma.talk("うん。だから人間には理解できない機能がいっぱいある"),
            ma.talk("そして人間たちがこれを使うということは、その使い方や生活のすべてをこれを通して魔王軍は監視できているってことなんだ"),
            yula.talk("え……"),
            ma.talk("そしてもう一つ。あれは人間たちの負の感情を集める装置でもあった"),
            he.talk("ってことは"),
            ma.talk("うん。結果的に君の炎上騒動がきっかけで、あれが生まれた。あれは人間の憎悪の化身なんだ"),
            he.look("魔獣を"),
            sol.talk("じゃあどうすりゃいいか分かるってことか？"),
            ma.nod(),
            ma.talk("最後のこれを使う"),
            ma.have("赤いサイコロを"),
            yula.talk("でもそれを使ったらあんたが……ほんとは魔王の力の根源なんでしょ？　知ってるから"),
            ma.talk("仕方ないよ。それが、魔王の宿命ってやつみたいなんだ"),
            )


## episode
def ep_confession(w: World):
    return w.episode("魔王の告白", "魔子は魔王だと告白するが",
            sc_worlddestruction(w),
            sc_confession(w),
            )
