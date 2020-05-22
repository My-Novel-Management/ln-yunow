# -*- coding: utf-8 -*-
"""Episode: 4-2.mamazonなう
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
def sc_usemamazon(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$w_amazonを使う",
            hero.be(),
            sol.be(),
            mako.be(),
            hero.do("$makoに教わって$w_amazonを使ってみることにした"),
            mako.talk("ここにいっぱい並んでる商品が、全部買えるんです",
                "買ったら自動的に配達までしてくれるんですよ",
                "旅先でも使えてほんと便利なんで"),
            sol.talk("よく場所が分かるな"),
            mako.talk("それぞれの$smaphの場所が特定できるので、これで注文することが重要なんです"),
            hero.do("とりあえず旅に必要な$herbから注文してみる"),
            hero.do("と、すぐにドアが叩かれ、表に箱が着ていた"),
            hero.talk("おお！　マジで$herbだ", "これすごいな！"),
            mako.talk("でしょう？"),
            mako.talk("どんどん頼んじゃっていいですよ"),
            hero.talk("けど支払いはどうなってるの？"),
            mako.talk("全部口座から落とされますよ"),
            hero.talk("じゃあ、そこにお金が入ってなかったら？"),
            mako.talk("さあ", "よくは知りませんけど、取り立てとかくるんじゃないですか？"),
            hero.talk("あのさ、$me、口座に今何もないんだわ"),
            sol.talk("１$w_Gも？"),
            hero.talk("うん"),
            mako.talk("$hero様の口座、教えて下さい"),
            hero.talk("え？　なんで？"),
            mako.talk("とりあえず送金しておきます",
                "気になるんだったら魔王退治した賞金で返してくれればいいですから"),
            hero.talk("ああ、そういうことなら"),
            hero.do("こうして口座を教えた"),
            stage=w.on_heroroom_int,
            time=w.at_night,
            )

def sc_variousorder(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("無茶苦茶な注文",
            hero.be(),
            sol.be(),
            mako.be(),
            hero.talk("よし、これで何でも注文できるぞ！"),
            hero.do("高級な道具、キャンプ用品などをまとめて注文する"),
            hero.do("続々と商品が家に届く"),
            hero.talk("おー！　これでいいじゃん！"),
            sol.talk("でもよ、これ、全部持っていくの大変じゃね？"),
            hero.do("見る間に積み上がった大量の箱"),
            mako.talk("じゃあ次の街までまとめて送ればいいですよ",
                "$w_sagawaでいつも送ってます"),
            hero.talk("すごいな", "$smaphで何でもできるじゃないか"),
            )

def sc_finishready(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("準備完了",
            hero.be(),
            sol.be(),
            mako.be(),
            hero.do("荷物を送り、準備完了して、ほっとしている"),
            mako.talk("おつかれさまです", "はい、紅茶をどうぞ"),
            hero.do("いつの間にか部屋は貴族風に"),
            mako.do("お茶をいれてきた$S"),
            hero.do("二人はすっかり準備が済んだと、優雅にくつろいでいる"),
            sol.do("それを見て、呆れる$S"),
            sol.talk("お前らそんなんで厳しい旅ができると思うな！"),
            hero.do("だがそう忠告する$solを、二人はゴミを見るような目で見る"),
            sol.talk("何だよ？"),
            hero.talk("$sol君、$meたちはこの$smaphという最強の$w_magicitemを手に入れたんだよ？",
                "買い物に行かなくてもアイテムは手に入るし、",
                "そのうち冒険に行かなくても冒険できるかも知れない",
                "時代遅れな話はやめてくれたまえよ"),
            sol.talk("そんなもん、魔王の前なら意味ねえだろ？",
                "力こそパワーだぞ？"),
            hero.do("$Sは$w_amazonで辞書を注文する"),
            hero.talk("$sol君はこれでも読んで言葉の意味を勉強したらどうかね？"),
            sol.talk("間違ってるならわざわざそんなことせずに、今すぐここで指摘してくれよ！"),
            )

## episode
def ep_mamazon(w: World):
    return w.episode("4-2.mamazonなう",
            sc_usemamazon(w),
            sc_variousorder(w),
            sc_finishready(w),
            ## NOTE
            ##  - ママゾンの使い方を教わり、色々と注文する
            ##  - ママゾンで何でも揃えられるからと無理な注文もする
            ##  - ママゾンでものが揃ったので、翌朝冒険に出発することに決めた
            )
