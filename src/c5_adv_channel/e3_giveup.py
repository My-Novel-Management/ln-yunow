# -*- coding: utf-8 -*-
"""Episode: 5-3.底辺配信者なう
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
def sc_challenging(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("チャレンジ",
            hero.do("配信を始めた$Sだったが、全く視聴数が増えない"),
            hero.talk("なんでなんだ？"),
            sol.talk("いや、見りゃ分かるだろ？",
                "何が面白いんだ？", "お前の家にあるもの紹介したり、",
                "隣のおっさん紹介したり、",
                "一体誰が見たい？"),
            hero.talk("だって$meが見たやつはそれでみんな爆笑だったし"),
            sol.talk("既に人気のやつがやるのと、無名のお前がやるんじゃ全然違うだろ？",
                "例えばあのアイドルの$yuiちゃんなら市場歩いてるだけでみんな見るよ",
                "そういうもんだ"),
            hero.talk("ああ、$meが$yuiちゃんだったらなあ"),
            hero.talk("そうだ", "$yuiちゃんになってみよう"),
            hero.do("$makoに服を借りて女装放送をしようとする"),
            mako.talk("流石にそれはやめてください"),
            hero.do("だが即座に否定された"),
            )

def sc_dangerousfood(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("危険な食べ物",
            hero.do("次の企画ということで『ゲテモノ食い』が上がった"),
            hero.talk("これ？"),
            hero.do("$makoに頼んで、世界のゲテモノを届けてもらう"),
            hero.do("目の前には$slime丼があった"),
            sol.talk("いや普通に美味そうじゃね？"),
            hero.talk("味は普通だが、食べるのは危険だってさ", "なんで？"),
            sol.talk("$slimeだからだな",
                "一応食用だってあるけど、あいつら基本は捕食して中で溶かすからな",
                "これ、ほんとに食えるのか？"),
            hero.do("目の前にはうねうね動く色とりどりな$slime丼が用意された"),
            sol.do("$Sはその様子を撮影している"),
            hero.talk("えー、本日はチャレンジゲテモノってことで、$slime丼に挑戦してみます"),
            hero.do("食レポをしながら、少し食べてみる"),
            hero.talk("意外といけますね……ん？"),
            hero.do("なぜか顔にはりついて囲まれる"),
            hero.talk("んー！"),
            hero.do("もがく"),
            sol.talk("おー、いいぞいいぞ", "今回はなかなか取れ高あるんじゃね？"),
            hero.do("だがもがいている。必死だ"),
            hero.do("そのまま息の根が止まってしまう"),
            hero.do("そして意識が遠くなった"),
            )

def sc_stopstreaming(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("そして配信をやめた",
            hero.be("目覚めると再び教会だった"),
            hero.do("もう$slimeは食わん！"),
            hero.do("家に戻ると、$solが待機していた"),
            sol.talk("今日はどうするんだ？", "全然視聴数増えないぞ"),
            hero.do("確認すると$slime丼を食べたことはなかったことになっていた"),
            hero.talk("もう$w_channelはいい",
                "自力で稼ぐ"),
            sol.talk("そんなこったろうと思ったぜ",
                "だから$meは最初から"),
            hero.think("案内所で言われたことを思い出す"),
            hero.talk("よし、$w_questを受ける！",
                "冒険者として稼ぐんだ！"),
            )

## episode
def ep_giveup(w: World):
    return w.episode("5-3.配信者はつらいなう",
            sc_challenging(w),
            sc_dangerousfood(w),
            sc_stopstreaming(w),
            ## NOTE
            ##  - 色々とチャレンジするが、失敗続き
            ##  - 何とか配信映えするようにとスライム丼食いに挑戦するが飲まれて死ぬ
            ##  - 結局配信をやめてしまった
            )
