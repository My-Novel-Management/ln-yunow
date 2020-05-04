# -*- coding: utf-8 -*-
"""Episode: 5-2.冒険者チャンネル開設なう
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
def sc_adventurechannel(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("冒険者チャンネル",
            hero.do("何か稼げないかと$smaphを見ていたら、",
                "そこにチャンネルを作ると稼げるというのを見つけた"),
            hero.talk("ねえ、$mako",
                "これって何なの？"),
            mako.talk("ああ、知りませんか、これ",
                "$w_dougaを流して、その再生数に応じて収益があるんです",
                "今だと、ほら、この$hikakinとか"),
            hero.do("見ると、訳のわからないものを$w_amazonで購入して開封して喋っているだけだ"),
            hero.talk("これのどこがお金になるの？"),
            mako.talk("こうやって商品の紹介になってるんですよ",
                "みんなどんなものか分からないと買うのに躊躇するでしょう？",
                "$meもよく参考にしてます",
                "他にも化粧方法とか紹介してますよ？"),
            hero.talk("へえ"),
            hero.think("これなら簡単に儲かるんじゃないかと考えた"),
            )

def sc_setup(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gando = W(w.gando)
    return w.scene("チャンネルの開設",
            hero.do("そこで$Sは近所で頼りになる大工の$gandoを呼んだ",
                "彼は昔から父の友人で、父がいなくなってからも何かと助けてもらっている"),
            gando.talk("おう、なんか妙なもんに興味出したな",
                "女ができるとやっぱ変わるか"),
            hero.talk("女？"),
            gando.talk("いやいや",
                "それより最近の若いやつら、みんなこれで遊んでばかりみたいだが、",
                "ちゃんと働く気はあるんかね",
                "うちのなんか友だちがみんな持っとるから買え買えってうるさくてな"),
            hero.talk("便利ですけど、$meも当たっただけなんで"),
            gando.talk("で、何がしたいんだ？"),
            hero.do("$Sはチャンネル開設がしたいのだと説明する"),
            gando.talk("$meも専門家じゃねえからちょっとわからねえところがあるが、まあできるだろ"),
            gando.do("$heroの$smaphを手に取り、それで聞きながらチャンネルを作ってくれる"),
            hero.talk("$gandoさんは$w_channelやらないんですか？"),
            gando.talk("$meはどうもこういうのは苦手でな",
                "結局あれだろ",
                "アイドルや芸人みたいに自分の人生を切り売りして稼ぐってこった",
                "それよりは地道に好きなことしつつ誰かの役に立ってる方がいいな"),
            gando.do("$smaphの操作を終えて、渡す"),
            gando.talk("これで始められるぞ"),
            )

def sc_firstchallenge(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("はじめてのはいしん",
            hero.do("部屋に$solを招き、$makoに見てもらいつつ、初めての配信を行う"),
            hero.talk("うまく撮ってくれよな"),
            sol.talk("そんなこと言うならお前が自分でやれ"),
            hero.talk("まあまあ、そういうこと言わないで",
                "これで儲かったら$solにもあげるから"),
            sol.talk("とりあえず、いくぞー"),
            hero.do("こうして自己紹介$w_dougaを撮ったが"),
            hero.talk("え、えっと、その"),
            sol.talk("自己紹介を"),
            hero.talk("は、はじめまして",
                "$heroと言います"),
            hero.do("がちがちで何も言えない"),
            hero.talk("まずはや、やってみたいことをリストにしてみました"),
            hero.do("用意しておいたものがテーブルから落ちて大惨事"),
            sol.talk("ストーップ！", "何やってんだ$k_hero"),
            mako.talk("なんか駄目っぽいですね"),
            mako.do("$Sは自分の$smaphで見ていたが、全く数字が増えない",
                "彼女が見ているだけのようだった"),
            )

## episode
def ep_setup_channel(w: World):
    return w.episode("5-2.冒険者チャンネル開設なう",
            sc_adventurechannel(w),
            sc_setup(w),
            sc_firstchallenge(w),
            ## NOTE
            ##  - 冒険者チャンネルで稼げると知る
            ##  - 何とか機材を揃えてチャンネル開設
            ##  - 初めての配信。何していいか分からず、ぶつぎり
            )
