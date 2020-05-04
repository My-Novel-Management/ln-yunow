# -*- coding: utf-8 -*-
"""Episode: 2-2.Re:酒場なう
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
def sc_re_bar(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    aida, gans = W(w.aida), W(w.gans)
    return w.scene("再び酒場へ",
            hero.come("$yulaに言われて酒場を訪れた$S"),
            hero.do("先程は開いてなかったのに、今は開いているようだ"),
            hero.talk("すみません"),
            gans.be(),
            gans.talk("何だ？", "ガキはかえんな"),
            hero.talk("あの、一緒に魔王退治をしてくれる仲間を探しているんです"),
            gans.talk("それなら傭兵でも雇ってくんな", "うちは単なる酒場だよ"),
            hero.talk("金がないって言ったら、酒場なら話を聞いてくれる物好きものいるだろうって"),
            aida.talk("いれてやんな"),
            gans.talk("けど姐さん"),
            aida.talk("どうせまだ客なんざ来ないよ"),
            hero.do("中に入れてもらう"),
            )

def sc_barmaster(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    aida, gans = W(w.aida), W(w.gans)
    return w.scene("酒場でからかわれる",
            hero.come(),
            aida.be(),
            gans.be(),
            inside.look("沢山の酒が置かれた棚",
                "店内は薄暗く、まだ椅子や机の整備がされていない"),
            aida.look("女店主で、妖艶",
                "胸元が大きく開いた黒や紫基調のドレス",
                "足を組み替えると腿が目立つ"),
            gans.look("大柄で筋肉質",
                "片手で樽を軽々担ぎ上げている"),
            hero.do("座るように言われて、縮こまって座る"),
            hero.do("はじめての酒場にきょろきょろと"),
            aida.talk("で、何か飲むかい？　酒しかないけど"),
            hero.talk("え"),
            aida.talk("冗談だよ", "$milk出してやんな"),
            gans.talk("おいっす"),
            gans.do("奥で$milkを注いで持ってくる"),
            aida.talk("それで、何だって魔王退治なんてだいそれたこと言ってんの？"),
            hero.talk("いろいろ事情があって",
                "でも一番の理由は$k_dadが英雄$dadだってことかな"),
            aida.talk("え？"),
            gans.talk("お前ふかしこいてんじゃねえだ！"),
            aida.talk("いや、確かにこの眉毛は似てるねえ",
                "あの融通きかない男にさ"),
            aida.do("舐めるように見つめる"),
            aida.talk("いいよ",
                "まあそういうことにしといてあげる",
                "で、仲間ってどんなの探してるの？", "多少なら口利きできるよ",
                "$meらも商売上がったりだからね、あの魔王のせいで"),
            hero.talk("一番強い仲間をお願いします！"),
            )

def sc_boysbecry(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    aida, gans = W(w.aida), W(w.gans)
    return w.scene("坊やは相手にされない",
            hero.do("店の外に放り出されて、戻ってくる"),
            hero.talk("何するんですか？"),
            aida.be(),
            gans.be(),
            gans.talk("何考えてものいってんだ？"),
            gans.do("でかい体で塞いでいる"),
            aida.talk("仲間ってのがどういうもんか、あんた全然分かってないだろ？",
                "仲間ってのはね、金で雇った傭兵とは違う",
                "いざって時には自分の命を預け合うような、そんな大切な存在なんだよ",
                "強さだけ求めたところで、あんたが苦しいときに守ってくれなかったら意味ないだろう？"),
            hero.talk("そういうのも都合のいい仲間いませんか？"),
            aida.do("無言での睨み"),
            gans.talk("さっさと家に帰ってママの$milkでも飲んでな"),
            hero.go("追い出された"),
            )

## episode
def ep_bar(w: World):
    return w.episode("2-2.Re:酒場なう",
            sc_re_bar(w),
            sc_barmaster(w),
            sc_boysbecry(w),
            ## NOTE
            ##  - 再び酒場を訪れると中に入れた
            ##  - 坊主だと相手にされないし、笑われる
            ##  - 酒場で仲間は見つけられず、妙なアプリに登録しただけだった
            )
