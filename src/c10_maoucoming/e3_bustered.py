# -*- coding: utf-8 -*-
"""Episode: 10-3.魔獣退治
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
def sc_maju_and_game(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("魔獣とゲーム",
            hero.be(),
            mako.be(),
            sol.be(),
            yula.be(),
            maju.do(),
            hero.do("$majuの前に巨大な$smaphが落とされる"),
            maju.do("$smaphを拾って、それの操作を始める"),
            sol.talk("マジでやってるよ"),
            hero.talk("ここまでは計算通りさ", "問題はこっからだ"),
            mako.talk("ゲーム起動させて"),
            hero.talk("まずは覚えさせる", "$meがはまったみたいに、沼に引きずり込んでやる"),
            yula.do("SNSの監視をしている"),
            yula.talk("ねえ、全然ヘイト減ってないよ",
                "魔王と勇者のヘイトばかりが流れてくよ"),
            hero.do("見ていると$majuの背中が膨らむ"),
            hero.talk("今は気にするな", "このままはまってくれればいける"),
            maju.do("動きが止まる"),
            mako.talk("$w_majuがゲーム見つけました"),
            yula.talk("どうするんのよ、どんどんヘイト増えてるってカンストしちゃう"),
            hero.talk("動きがとまった", "今説明読んでるんだ", "ついに始まるぞ"),
            hero.do("$Sは$makoに指示を出して、ゲームを優位に進めてもらう"),
            hero.think("自分がゲーム沼、ガチャ沼にはまったことを思い出す"),
            hero.talk("お前もはめてやるよ、ガチャっていう沼にな！"),
            )

def sc_gacha(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("魔獣ガチャ",
            hero.be(),
            mako.be(),
            sol.be(),
            yula.be(),
            maju.do(),
            hero.do("みんなで静観している"),
            maju.do("ゲームに熱中し、$goblinの要塞跡に腰掛けている$S"),
            yula.talk("ヘイト、完全に止まったね"),
            maju.do("動きが変わる"),
            mako.talk("今ガチャまわし始めたみたい"),
            hero.talk("最初はいいの当てて、どんどん難しくしていくんだ"),
            mako.talk("わかってますよ、元々は$meの会社が作ったんですから"),
            yula.talk("あ、ヘイトが減ってきた"),
            hero.talk("やっぱりあれはこの$smaphが増幅していたんだ"),
            yula.talk("あれ？　でもちょっと待って",
                "途中で逆に増え始めた。どんどん増える"),
            hero.talk("ガチャでヘイトが溜まってるんだ"),
            mako.talk("どうするんですか！"),
            hero.talk("詫び石配って！"),
            mako.talk("そんな急に"),
            hero.talk("とにかく回させて、いい思いをさせるんだ"),
            maju.do("延々とガチャし続ける"),
            )

def sc_bustermaju(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("魔獣消える",
            maju.do("どんどん縮んでいく"),
            sol.do("$w_majuを倒しに向かうが"),
            hero.talk("もう、いいんだ"),
            hero.talk("ごめんな", "$meが悪かったんだ"),
            hero.do("$majuを抱きしめる"),
            maju.do("その凶悪な顔から憎悪が消えて、"),
            maju.do("光になって存在が消えてしまった"),
            hero.talk("ありがとう"),
            hero.do("$Sは見送った"),
            )

## episode
def ep_bustered(w: World):
    return w.episode("10-3.魔獣退治",
            sc_maju_and_game(w),
            sc_gacha(w),
            sc_bustermaju(w),
            ## NOTE
            ##  - 魔獣にUR引かせる為に魔子はゲーム会社に要請する
            ##  - 魔獣が止まっている間に勇者は自分が魔王ではないと配信する
            ##  - 魔獣は遂にガチャを引き当てて昇天して消えた
            ## TODO:
            ##  ガチャしてるだけだと単調なので、何か他に驚異を設定する（魔物軍団が街を襲っているのをみんなで協力して阻止する、ソルが陣頭指揮等）
            ##  もう少しスマフをうまく利用する
            )
