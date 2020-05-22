# -*- coding: utf-8 -*-
"""Episode: 10-2.ヘイトの魔獣
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
def sc_destroymaju(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("魔獣による街の破壊",
            hero.be(),
            mako.be(),
            sol.be(),
            yula.be(),
            maju.come("巨大な$w_majuが襲っている"),
            sol.talk("おいおいおい", "街が壊されてるぞ"),
            mako.talk("全部を無に返すんです", "憎悪という感情がこの世界をリセットするんです"),
            mako.do("映像を見せる"),
            hero.talk("酷い……"),
            hero.do("$makoが映し出した映像では、魔物も人間も無差別に$w_majuにより殺されていた"),
            hero.do("追い詰められた教会の屋根に登り、そこから見ている"),
            )

def sc_mako_desicion(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$makoの決意",
            mako.talk("あの、それでこの$rebuildboxを使えば、あの$majuが生まれない世界に戻せるんです",
                "もう二度と生まれない世界にできるんです"),
            sol.talk("それならもうそいつ使ってもらえばいいんじゃね？",
                "このままだと魔王どうこうでなく、世界が滅ぶんだろ？"),
            mako.talk("はい"),
            hero.talk("何とか倒せないの？　あれって",
                "だって$meたち人間が生み出したものなんだろ？"),
            mako.talk("倒せませんよ",
                "だって$w_majuはこの世界の外からやってきた存在なんですから",
                "この世界での死という概念がありません"),
            hero.talk("そんなのって"),
            mako.talk("だから$meがこれを使いますよ"),
            sol.talk("そうだな、頼むわ"),
            yula.talk("待って"),
            sol.talk("何だよ、$yula", "別に元に戻るだけで痛いことも何もないんだからいいだろ？"),
            yula.talk("違うよ",
                "$makoが言ってるの聞いたのよ",
                "それを使うと命の火が短くなる", "あと一回使えばもう$makoは消えてなくなってしまうって"),
            hero.talk("本当なの？"),
            mako.do("頷く"),
            hero.talk("じゃあ駄目だよ！", "なんで$makoを犠牲にしなくちゃいけないんだよ"),
            mako.talk("だって$meは、人間の敵で、魔王ですから"),
            )

def sc_heros_idea(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("勇者のアイデア",
            hero.do("黙り込むみんな"),
            sol.talk("あ、潰された"),
            yula.talk("どうやらあの$w_maju、世界中に出てるみたい",
                "ほら、他の街も潰されていってる"),
            hero.do("$yulaが$smaphで見ている"),
            mako.talk("それじゃあ$me、使いますね"),
            hero.talk("待って"),
            sol.talk("何だよ$k_hero"),
            hero.talk("別に倒さなくてもいい"),
            yula.talk("何言い出すの！"),
            hero.talk("$meに考えがあるんだ"),
            hero.do("自分の$smaphを見た"),
            hero.talk("$mako、この$smaphって魔族が作ったものだって言ったよね？",
                "だったらこれも、魔族で作ってるの？"),
            hero.do("ガチャでひどい目にあったゲーム画面を見せる"),
            mako.talk("そうですよ", "うちの会社で製作してます",
                "人間たちから欲望を吸い上げるのにすごくいいんです"),
            hero.talk("これを使って$majuを何とかできるかも"),
            mako.talk("え？"),
            )

## episode
def ep_hatedaemon(w: World):
    return w.episode("10-2.ヘイトの魔獣",
            sc_destroymaju(w),
            sc_mako_desicion(w),
            sc_heros_idea(w),
            ## NOTE
            ##  - ヘイトの魔獣は大きくなり、次々と街を襲う
            ##  - 魔子は世界のリセットを使おうとするが、勇者が待ったをかける
            ##  - 勇者は魔子に魔獣にガチャをさせることを提案する
            )
