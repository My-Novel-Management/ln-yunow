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
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$makoの告白",
            hero.be("$goblin遺跡の見張り台から、遠くの土煙を眺めていた"),
            mako.be(),
            sol.be(),
            yula.be(),
            outside.look("遠くの景色",
                "南側の港の方、海の上に現れたゴジラよろしく巨大な魔物の姿",
                "空は暗い（夕方）"),
            inside.look("元$goblinの巣である、今は古くなった遺跡",
                "そこの頂上部分から遠くを眺めやっていた"),
            hero.talk("どういうことなんだ？"),
            hero.look("変装のために着ていた兵士の服装から、兜を脱ぎ捨て、甲冑だけになっている$S"),
            hero.do("あれを『$maju』と呼んだ$makoに説明を求める"),
            hero.do("$makoを見た"),
            mako.look("普段の黒ずくめとは異なり、変装で街の花売りに扮していたので、金髪のウィッグにミニスカート、タイツというエロ可愛い感じ"),
            mako.do("いつもみたいな子供っぽい喋り方ではなく、真面目なトーンで大人の話し方をする$S"),
            mako.talk("$majuというのは$w_webに集まった人間たちの憎悪が生み出した最悪の$w_majuのことで、",
                "この$smaphを人間界に配ったのも、あれを生み出すのが目的だったんです",
                "あれは世界を滅ぼす最終兵器なんですよ"),
            sol.talk("なんで$k_makoはそんなになんでもかんでも知ってるんだよ",
                "まさか本当に本物の魔王だとか、そんなこと言い出すんじゃないだろうな？"),
            mako.do("何故か黙り込む$S"),
            sol.talk("お、おい", "冗談だろ？", "なんで黙んだよ？",
                "$meたちが探してた魔王がすぐそばで、しかも仲間だったとか、しゃれにもならねえぜ？"),
            yula.talk("ちょっとー、何話してんのよ？",
                "$meも上がってっていいの？"),
            mako.talk("とにかく、一旦部屋に戻りましょうか"),
            mako.do("いつもとは全然違う調子で言った"),
            camera=w.hero,
            stage=w.on_gobtower,
            day=w.in_birthmaju, time=w.at_evening,
            )

def sc_confess2(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("魔王の告白",
            hero.come("はしごから降りてくる"),
            mako.come(),
            sol.come(),
            yula.be(),
            yula.do("戻ってきたみんなの様子が変と気づく"),
            yula.talk("何よ？　その$majuってのがどうかしたの？"),
            yula.do("$smaphには沢山の$w_tweetがあり、そこに魔獣の$w_gazouが投稿されていた"),
            hero.talk("なあ$mako", "さっき言ったことは、本当なのか？"),
            sol.talk("$k_mako！", "$meたちに分かるようにちゃんと説明してくれ！",
                "でないと$meは……$meはお前を、許せねえ！"),
            yula.talk("何があったのよ……"),
            # TODO
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
            stage=w.on_gobtowroom_int,
            time=w.at_night,
            )

def sc_truth(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    inside, outside = W(w.inside), W(w.outside)
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
    inside, outside = W(w.inside), W(w.outside)
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
            sc_confess2(w),
            sc_truth(w),
            sc_rebuilding(w),
            ## NOTE
            ##  - 魔子は自分が魔王だと告白する
            ##  - この世界は何度もリセットされ、自分に都合のいいように作り変えられてきたと
            ##  - ただそのやり直しの壺は後一回しか使えず、それを使い切ったら魔子は消える
            )
