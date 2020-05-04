# -*- coding: utf-8 -*-
"""Episode: 9-2.炎上
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
def sc_heroismaou(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside = W(w.inside)
    return w.scene("勇者が魔王",
            hero.do("$Sが魔王ということになり、世界中でデモが起こっていた"),
            hero.do("その様子がどんどん$smaphに流れてくるのを見て、$Sは震えている"),
            sol.talk("おーい、飯"),
            hero.do("毛布にくるまっている"),
            sol.talk("あのな、ここ$meが借りてる部屋なんだからな？"),
            hero.do("かくまってもらっていた"),
            hero.do("薬草屋の屋根裏に間借りしている$solに匿ってもらった"),
            inside.look("狭くて低い天井、窓はない"),
            mako.come(),
            mako.talk("一応お母様はホテルに避難してもらいましたけど、",
                "家は魔法でバリアを張って守っててもこのままだと炎上不可避です"),
            mako.do("何度も火をつけられたり、ゴミを投げ込まれたりしている"),
            hero.talk("$meが何したっていうんだよ！"),
            )

def sc_reporting(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    sold = W(w.soldier)
    doyle, candy = W(w.doyle), W(w.candy)
    return w.scene("通報しました",
            hero.do("目を覚ますと、一人しかいない"),
            hero.do("ドアのノックを聞いて「開いてるよ」というと、知らない人が入ってくる"),
            hero.talk("え？"),
            sold.talk("あなたに逮捕状が出ています"),
            hero.do("兵士に取り囲まれる"),
            hero.talk("いや、$me何もやってないから！"),
            candy.do("こわがって怯えている"),
            doyle.talk("すまんが通報させてもらった"),
            sol.talk("なんで$meまで？"),
            sol.do("捕まえられている"),
            )

def sc_becaught(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    sold = W(w.soldier)
    return w.scene("捕まる",
            hero.be(),
            sol.be(),
            hero.do("牢屋にぶちこまれた$Sと$sol"),
            sol.talk("なんで$meまで巻き添えなんだよ"),
            hero.talk("あ、でもここにいればひょっとしたら安全かも",
                "だって外歩いてて石投げられたりしないもんな"),
            sol.talk("ああ、そうか。飯ももらえるしな"),
            hero.do("しかし貧しい薄味スープだけ"),
            hero.talk("これじゃあ先に餓死する"),
            hero.think("でも死んだらまた教会からやり直せるかも、と考える"),
            hero.talk("なあ、$meを殺してくれないか？"),
            sol.talk("は？　お前ついにとちくるったか？"),
            hero.talk("やっぱいいわ"),
            hero.think("何とか脱出を考える"),
            sol.do("$Sがやってきた兵士を捕まえて首を締める"),
            sol.talk("これで脱出しよう"),
            sol.do("兵士の鎧を奪うが"),
            sol.talk("何してんだ？"),
            mako.come(),
            mako.talk("転移魔法できちゃいました", "一緒に逃げましょう",
                "あ、$solさんはその格好で表から出ます？"),
            sol.talk("なんでだよ！　$meも一緒に連れてけ！"),
            )

def sc_hideandseek(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("地獄のかくれんぼ",
            hero.do("$makoにより、近隣の森の中に連れてきてもらう"),
            yula.be("待っていて"),
            yula.do("$smaphで情報確認をしている"),
            yula.talk("$meが使ってた隠れ家があるんだけど、とりあえずそこに逃げるしかないね",
                "街は無理だ"),
            hero.do("$smaphを見ると、そこかしこで暴動が起こっている",
                "デモ隊と王宮の部隊がにらみ合いを続けている"),
            hero.do("どうやら勇者＝魔王は王が画策したものだという、とばっちりのようだった"),
            hero.talk("どうすりゃいいんだ！　もう$meが魔王ってことでいいんじゃないかな"),
            sol.talk("そんなことしたらお前つかまって死刑だぞ？"),
            hero.talk("死刑は嫌だ"),
            hero.do("あばれる$S"),
            yula.talk("とにかく黙ってて。バレたら殺されるわよ？"),
            hero.talk("はい"),
            )

def sc_runaway(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("逃げる",
            hero.do("森をみんなで抜ける"),
            hero.do("道中、いろいろと見つかりそうになる"),
            hero.do("$smaphの位置情報から特定されて、突撃される"),
            hero.talk("ああ、もうスイッチきるぞ！"),
            hero.do("みんなとはぐれて一人になり"),
            hero.talk("ん？　$mako？"),
            hero.do("そこで出会ったのは少女だった"),
            _.do("彼女は優しいふりをして、通報する"),
            _.do("大人たちが駆けつけ、取り押さえられる"),
            hero.talk("$meは無実だ！"),
            hero.do("そして$Sは死刑になった"),
            )

## episode
def ep_burnout(w: World):
    return w.episode("9-2.炎上",
            sc_heroismaou(w),
            sc_reporting(w),
            sc_becaught(w),
            sc_hideandseek(w),
            sc_runaway(w),
            ## NOTE
            ##  - 実は魔王だったとされ、炎上した勇者
            ##  - どこにいてもすぐ見つけられて通報される
            ##  - 遂には山に籠もるようになる
            )
