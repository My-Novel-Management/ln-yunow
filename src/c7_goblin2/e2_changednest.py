# -*- coding: utf-8 -*-
"""Episode: 7-2.Re:ゴブリンの巣なう
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
def sc_intonest(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$goblinの巣に突入",
            hero.be(),
            sol.be(),
            mako.be(),
            hero.do("入り口の一つから中に入る$Sたち"),
            inside.look("綺麗に整備された洞窟の中のように、薄暗い",
                "そこを松明の明かりで進む"),
            hero.talk("こんな暗い中、いきなり襲われたらどうするんだ"),
            sol.do("びくついている$S"),
            sol.talk("$meは絶対に入らないって言ったのに、なんで勝手に入ってくんだ！"),
            mako.talk("大声出さないで下さいよ",
                "相手に気づかれますよ？"),
            mako.do("$smaphを見ながら、近くにモンスターがいると表示されている"),
            mako.talk("洞窟内だとうまく$w_denpaが拾えませんね",
                "ところどころで表示がきれます"),
            mako.talk("あ、これ$meたちの$smaph、完全に駄目っぽいですね"),
            hero.talk("え？　どういうこと？"),
            mako.talk("どうやら$w_denpaがモンスター専用みたいで、",
                "$meたちはパスワード盗まないと使えませんね"),
            hero.talk("じゃあなしでいくしかないのか"),
            hero.think("帰ろうかと考え始めていたが、"),
            sol.talk("帰らせちゃくれないようだぜ"),
            hero.do("目の前に松明を手にした$goblinが三匹、にやついていた"),
            stage=w.on_goblinnest_int,
            )

def sc_vs_goblin(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("vs$goblin",
            hero.be(),
            sol.be(),
            mako.be(),
            hero.do("狭くて暗い通路で、前も後ろも$goblinに囲まれている"),
            hero.talk("どうする？"),
            sol.talk("やるしかない"),
            mako.talk("もう魔法で燃やしちゃいましょうよ"),
            hero.talk("いや、火はまずいから"),
            hero.think("状況が違いすぎて困惑している",
                "考えていた作戦が全く使えないので、どうしようと"),
            sol.talk("$goblinくるぞ！"),
            gob.do("$Sが襲いかかってくる"),
            sol.do("腹を剣で殴りつけ、そのまま前に突進する"),
            hero.talk("強行突破？"),
            mako.talk("危ない！"),
            mako.do("魔法で燃やしてしまう"),
            hero.talk("あ"),
            mako.talk("大丈夫ですよ", "ちゃんと調整してますから",
                "$meだってここが崩れる可能性を考えない訳じゃありませんから"),
            sol.talk("おい、こいつらは$smaph持ってないからたぶん大丈夫だと思うけど、",
                "気づかれててもおかしくないからな"),
            sol.do("前の二体は$Sが倒してしまった"),
            hero.talk("ボスさえ倒せば何とかなるはずだから"),
            hero.do("奥に進む三人"),
            )

def sc_yula(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$goblinからカツアゲする盗賊",
            w.symbol("※"),
            yula.be(),
            gob.be(),
            yula.do("一方その頃、$Sはある部屋に忍び込んでいた"),
            yula.talk("あんたらこんだけ貯め込んで、どうなるか分かってるんでしょうね？"),
            gob.do("怯える$Sたち"),
            yula.do("一瞬でちまつりにしてしまう"),
            yula.talk("それじゃ遠慮なくいただくわね"),
            yula.do("目の前にある箱の中には金銀財宝が詰まっている",
                "他にも奪ってきた食料や衣類もある"),
            yula.talk("へえ、これは新品ね", "いくつか貰っとこうかしら"),
            yula.talk("だれ？"),
            yula.do("気配を感じて、ランタンを消した"),
            )

def sc_joinyula(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$yulaが仲間に",
            w.symbol("※"),
            hero.be(),
            sol.be(),
            mako.be(),
            hero.do("松明が消えそうになっている"),
            mako.talk("$meが魔法で明かりつけますよ。ほら"),
            hero.do("明るくなる"),
            hero.talk("でもこれだとすぐ見つかっちゃうんじゃない？"),
            mako.talk("じゃあ消します"),
            sol.talk("おい！　真っ暗になったぞ！"),
            hero.do("これは先に進めなくなる、と思った矢先に、明かりを見つけた"),
            hero.talk("ねえ、あれ"),
            sol.talk("$goblinのやつらか？"),
            hero.talk("いや、話し声聞こえない？"),
            hero.do("三人でその部屋に乗り込んでみる"),
            hero.do("いきなり部屋の明かりが消えた"),
            hero.talk("え？"),
            yula.talk("なんだ、人か"),
            mako.do("魔法で明かりをつける"),
            hero.do("そこには女盗賊$yulaが現れた"),
            hero.talk("あ、神官代理さん"),
            yula.talk("ああ、あんたか"),
            )

## episode
def ep_changed_nest(w: World):
    return w.episode("7-2.Re:ゴブリンの巣なう",
            sc_intonest(w),
            sc_vs_goblin(w),
            sc_yula(w),
            sc_joinyula(w),
            ## NOTE
            ##  - ゴブリンの巣に入り、スマフで互いの距離を確認する
            ##  - シーフのユラがゴブリンからカツアゲしていた
            ##  - シーフのユラを仲間にしたが、魔子の姿が消えていた
            )
