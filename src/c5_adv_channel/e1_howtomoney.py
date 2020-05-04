# -*- coding: utf-8 -*-
"""Episode: 5-1.金を稼ぐなう
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
def sc_nomore_mamazon(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    clerc = W(w.clerc)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$w_amazonは懲り懲り",
            hero.be("教会で目覚める$S"),
            clerc.talk("どうかしましたか？"),
            hero.talk("あ、いえ"),
            hero.do("また戻されたのだと分かり、一旦家に戻る"),
            hero.do("家では$makoたちが待っていた"),
            mako.talk("$hero様、買い物なら$w_amazonで"),
            hero.talk("いや、いい"),
            mako.talk("え？"),
            hero.talk("それは今はいい",
                "準備は何とか自分たちでするよ"),
            mako.do("なんで？　という表情"),
            sol.do("外から戻ってきた$solは汚れている"),
            mako.talk("あんた相変わらず汚いわね"),
            sol.talk("お前らと違って$meは地道に働いてるんだよ"),
            hero.talk("$meも働いて金貯めようと思うんだ",
                "$sol、仕事を紹介してくれないかな？"),
            sol.talk("ああ、いいぜ"),
            camera=w.hero,
            stage=w.on_castletown1,
            day=w.in_current, time=w.at_afternoon,
            )


def sc_hardwork(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("肉体労働",
            hero.do("翌日、$meは$solについて現場へとやってきた"),
            hero.talk("え？　これをやるの？"),
            sol.talk("そうだよ",
                "これ全部耕して、苗を植えるんだ", "お前が普段食ってるもんもこうやってできるんだぞ？"),
            hero.do("それは農場だった",
                "城の兵士用のものだが、一般にも出荷されている",
                "前王が戦争に備えて開発したものだった"),
            hero.do("$solと一緒にクワを手にして土を掘り返す",
                "すぐに顎が上がる",
                "肉体労働に慣れていない$Sは座り込んで休んでしまう"),
            hero.do("おじさんやおばさんに情けないなあと言われて"),
            sol.talk("これが働くっつうことだぞ？"),
            hero.talk("いや、もっと楽して稼ごう"),
            )

def sc_findjob(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    mashu = W(w.mashu)
    return w.scene("職探し",
            hero.do("$meは肉体労働を除いた何か仕事を探そうと職安にやってくる"),
            mashu.talk("で、どんな職業探してるの？"),
            hero.talk("えー、楽に稼げて、さっさと冒険に旅立てるような"),
            mashu.talk("ない",
                "というか、あんたまだ若いでしょ？",
                "金を稼ぐとかどうこうじゃなくて、何が自分に合っているか、",
                "色々と見聞を深めるのが先だと思いますがね"),
            hero.talk("なりたいのは$w_Y"),
            mashu.talk("は？　$w_Yになりたいとか言うのは初めて聞いたわ",
                "でもありゃなるもんじゃなくてな、",
                "称号みたいなもんだから、それこそ業績を上げて王様にでも認めてもらって、",
                "やっとなれるみたいな",
                "冒険者になりたいなら、それこそこっちじゃなくて、ギルドに張り出されているクエストを探してみたらいいんじゃないかね？"),
            hero.talk("てっとりばやく稼げますか？"),
            mashu.talk("（じっと見て）無理だな、あんたらじゃ"),
            hero.talk("じゃあ、何か簡単に稼げそうなものって"),
            mashu.talk("地道に働く以外にない"),
            )

## episode
def ep_howto_money(w: World):
    return w.episode("5-1.真面目に金を稼ぐなう",
            sc_nomore_mamazon(w),
            sc_hardwork(w),
            sc_findjob(w),
            ## NOTE
            ##  - 金を稼がなければならないと気づき、仕事を探す
            ##  - 魔子に呆れられながらも肉体労働で汗を流す
            ##  - 真面目に稼いでいたら魔王退治に出かけられないことが判明する
            )
