# -*- coding: utf-8 -*-
"""Demo: story no1
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def sc_confession(w: World):
    hero, mako = w.hero, w.mako
    return w.scene("魔子の告白", "魔子は勇者を助ける為に自分が魔王だと名乗った",
            w.talk(mako, "$meが魔王だから"),
            w.think(hero, "何言ってるんだ？"),
            w.talk(mako, "$meは大魔王の娘でこの世界を任された魔王なの"),
            w.talk("小さい世界だからお前がやってみろって"),
            w.talk("だから$meはまずここがどんなところか知ろうと思って……$t_phoneをばらまいた"),
            w.talk("もともと$t_phoneはお父様が軍事兵器として開発させたものだったんだ"),
            w.talk("そして、この世界が酷いことを知った"),
            w.talk("人間を滅ぼそうと決めた"),
            w.talk("でも君はそんな$meに、大切な人が失われる辛さを教えてくれた"),
            w.talk("それが愛なんだって気づいた"),
            w.talk("$meは君が好きだ"),
            w.talk("だから、君を助ける為、魔王の石を使うよ"),
            w.talk("これを使えば、またやり直せる。何度でも"),
            w.talk("また最初から、やり直せるんだ……"),
            w.talk(hero, "$n_mako？"),
            w.talk(mako, "お父様には敵わない。やがてこの世界は消えてしまう。そんなのは嫌だ"),
            w.talk("魔王の石、つまり、$meの生命力を、割るよ。これでまた……"),
            w.talk(hero, "やめろ！"),
            w.act(mako, "石を割る"),
            w.look(hero, "世界はリセットされ、光に満ちる"),
            w.symbol("◆"),
            w.be(hero, "気づくと教会だった。それも最初の教会だ"),
            w.talk(hero, "神父様、$me……"),
            w.look("外を見ると、季節外れの雪が降っていた"),
            w.talk(w.sol, "何しけた顔してんだ？"),
            w.talk(hero, "$n_makoは？"),
            w.talk(w.sol, "誰だそれ？"),
            w.talk(hero, "覚えてないのかよ！"),
            w.think("彼女は消えた。魔王という言葉も消えていた"),
            w.think("彼女を探し出すと決意する勇者だった"),
            )

## episode
def ep_demo(w: World):
    return w.episode("Demo", "勇者は魔子が魔王だと知った",
            sc_confession(w),
            )
