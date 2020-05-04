# -*- coding: utf-8 -*-
"""Episode: 10-1.魔子の告白
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
def sc_makoconfess(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    return w.scene("$makoの告白",
            hero.be(),
            mako.be(),
            sol.be(),
            yula.be(),
            hero.talk("どういうことなんだ？"),
            hero.do("$makoに説明を求める"),
            mako.talk("$majuというのは、$w_webに集まった人間たちの憎悪が生み出した最悪の$w_majuのことです",
                "あれが生まれたら、もうこの世界は終わったも同然なんです"),
            sol.talk("なんでよ？", "魔王よりも怖いのか？"),
            mako.talk("魔王なんて、全然です", "あれは本物の最悪なんです",
                "そもそも、$smaphはあれを生み出すために作られたんです"),
            yula.talk("あんた、何を知っているんだ？",
                "そもそも最初からずっと思ってたんだけど、事情通すぎやしないかい？"),
            hero.talk("どうなんだ？"),
            mako.talk("もう、限界かな"),
            hero.do("じっと見る"),
            mako.do("端にいって、一人になり"),
            mako.talk("実は$me、魔王なんです"),
            sol.talk("はぁ？"),
            yula.do("$Sは黙り込む"),
            hero.talk("何言ってんだ？", "魔王が$makoな訳ないだろう", "なあ？"),
            mako.do("黙ったまま、手を差し出して、下で騒いでいる人間たちに向けて弾を放つ"),
            mako.talk("魔王族はね、呪文の詠唱なしに魔法が使えるんだ"),
            hero.talk("それって"),
            mako.talk("だって魔法は、もともと魔族が作ったものだから"),
            w.eventPoint("魔法", "魔族が作ったもの"),
            yula.talk("そうなの？"),
            mako.talk("じゃあ、今からここにモンスター呼べば$meが魔王だって証明できるかな？"),
            hero.talk("呼べるの？"),
            mako.do("$smaphで操作して連絡する"),
            hero.do("飛行型のモンスターが現れた"),
            mako.talk("ごめんね"),
            mako.do("光の弾で消してしまう"),
            mako.talk("これで$meが魔王だって信じてもらえたかな？"),
            sol.do("びびっている$S"),
            camera=w.hero,
            stage=w.on_castletown1,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_truth(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    return w.scene("この世界の真実",
            hero.be(),
            mako.be(),
            sol.be(),
            yula.be(),
            mako.talk("実はこの世界はね、お父様が$meの為に作った世界なんだ"),
            mako.do("彼女は語る", "彼女が生まれて、大魔王と闇の女王が彼女のために世界を作ったその話を"),
            mako.talk("最初、この世界には魔物だけがいたの",
                "人間は魔物の奴隷として作られた", "土人形だったのよ"),
            mako.explain("それから人間は徐々に自分たちで国を地上に作るようになった"),
            hero.think("思い出す",
                "かつて魔物たちがこの地上の支配者だった、という言説を"),
            mako.explain("その世界を、彼女は少し羨ましそうに見ていた",
                "けれど、お忍びで遊びにでかけた時にいじめられた"),
            _.talk("そんな時にかばってくれたのが、$hero様でした"),
            hero.talk("そんなことあったっけ？"),
            mako.talk("たぶん記憶はないんです", "だってその時に死んでしまったんですもの"),
            mako.talk("だから$meはお願いしたんです",
                "お父様に、蘇らせてほしいと",
                "そしたらこれをくれました", "この$rebuildboxで世界が再構築できると"),
            )

def sc_rebuilding(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    return w.scene("世界を再生すること",
            hero.be(),
            mako.be(),
            sol.be(),
            yula.be(),
            mako.do("$rebuildboxを見せて、それの説明をする"),
            mako.talk("これを使うことで、世界が最初から作り直される",
                "それも$meにとって都合のいいように",
                "$meはいつも$heroを殺さないようにと、邪魔なものを排除してきた"),
            hero.talk("え？　それじゃあ$meって何度も死んでるの？"),
            mako.talk("死んでる、というか、死んだ世界は一旦潰して、作り直しているんです",
                "だから死んだことそのものがなかったことになってるんです"),
            )

## episode
def ep_confess(w: World):
    return w.episode("10-1.魔子の告白",
            sc_makoconfess(w),
            sc_truth(w),
            sc_rebuilding(w),
            ## NOTE
            ##  - 魔子は自分が魔王だと告白する
            ##  - この世界は何度もリセットされ、自分に都合のいいように作り変えられてきたと
            ##  - ただそのやり直しの壺は後一回しか使えず、それを使い切ったら魔子は消える
            )
