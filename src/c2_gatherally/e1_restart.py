# -*- coding: utf-8 -*-
"""Episode: 2-1.Re:教会なう
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
def sc_re_church(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    clerc = W(w.clerc)
    return w.scene("再び教会にて",
            hero.be("教会で目覚める"),
            clerc.be("神父がいる"),
            clerc.look("正装である濃紺の衣を身にまとっている"),
            hero.talk("あれ？　ここって"),
            clerc.talk("お祈りはすみましたかな、$hero"),
            hero.talk("神父？　旅行に行ったんじゃ"),
            clerc.talk("いやいや", "腰をやってしまってな", "旅行は中止にしたんだよ"),
            hero.think("何か奇妙だと思う"),
            hero.do("自分の体や持ち物を確かめる",
                "特に問題がない"),
            hero.do("$smaphを見ると、そこには打ち込んだ$w_tweetが消えていた"),
            hero.talk("おかしいな"),
            clerc.talk("$hero君も$smaphを買ってもらったんだな",
                "最近若い子はみんな持っているよね", "随分と便利なんだろう？"),
            hero.talk("いや、まだよくわかんなくて"),
            hero.do("ひょっとしたらこれの力で復活したのか、とか考え始める"),
            hero.talk("とにかくありがとうございます"),
            clerc.do("にこやかに答えるが、意味が分からない様子"),
            hero.go("外に出ていく"),
            camera=w.hero,
            stage=w.on_castletown1,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_checkout(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    candy = W(w.candy)
    return w.scene("街を確認する",
            hero.come("教会を出て、街に戻る"),
            outside.look("街は変わらない様子",
                "市場にはわずかばかりの露店が並ぶ"),
            candy.come(),
            candy.look("小柄だが成人女性。金髪にそばかす"),
            candy.talk("あ、$heroさん。こんにちは"),
            hero.talk("ああ、$candyさん"),
            hero.do("$herb屋の娘だ"),
            candy.talk("それ、$smaphじゃないですか。どうしたんですか？"),
            hero.talk("う、うん。ちょっと懸賞に当選してね"),
            candy.talk("いいなー", "$meもおこづかい貯めて買いますから、その時は相互してくださいね"),
            hero.do("意味がわからないが頷く"),
            hero.do("$smaphを見ると、色々な機能がある",
                "流れていく$w_tweetは平和だが、魔王の驚異に怯える声も"),
            hero.talk("そうだ。$meは$w_Yなんだから、がんばらないとな"),
            )

def sc_gotogatherally(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("仲間集めに向かう",
            hero.do("何からやればいいのか考える"),
            hero.do("城で$arnoldに教わったものを思い出す"),
            hero.talk("あ、そういえば"),
            hero.do("$smaphのメモを思い出す",
                "確認すると『旅の手引き』があった"),
            hero.do("手引きを読み込む$S"),
            hero.talk("旅は過酷で、一人では大変危険だから、仲間をまず見つけることが肝心と"),
            hero.do("しかしどこで仲間を探せばいいのか書かれていない"),
            hero.do("戦闘のプロなら傭兵を雇うのがいいと、まずは傭兵ギルドに向かう"),
            )

def sc_mercenary(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("傭兵ギルド",
            hero.come("傭兵ギルドにやってくる"),
            inside.look("いかつい受付と、たむろしている男たち"),
            inside.look("その中に教会で見かけた彼女の姿があった"),
            hero.talk("あ！"),
            yula.be(),
            yula.talk("何さ？"),
            hero.talk("あの、さっき教会にいた人ですよね？"),
            yula.do("怪訝な顔"),
            yula.talk("いや"),
            hero.talk("傭兵なんですか？"),
            yula.talk("$meは違うよ", "あんた傭兵探してんの？"),
            hero.talk("傭兵っていうか、仲間を","魔王退治の冒険に行くんです"),
            hero.do("みんなから笑われる"),
            yula.talk("やめときな", "魔王どころかそこらの$slimeにだって相手になりゃしないよ、あんたなんて"),
            hero.talk("でも倒さないと困るんです", "強い仲間さえいれば"),
            yula.talk("金持ってないんでしょ？　だったら酒場にでもいって、あんたの力になってくれそうな人探しな"),
            )

## episode
def ep_re_church(w: World):
    return w.episode("2-1.Re:教会なう",
            sc_re_church(w),
            sc_checkout(w),
            sc_gotogatherally(w),
            sc_mercenary(w),
            ## NOTE
            ##  - 目覚めると教会で、神父がいた
            ##  - 外に出て確認する。怪物はいなかった
            ##  - とりあえず夢だったと思い、仲間探しに向かう
            )
