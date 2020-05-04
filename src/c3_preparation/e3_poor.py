# -*- coding: utf-8 -*-
"""Episode: 3-3.貧乏なう
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
def sc_playgame(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("ゲームおもしろい",
            hero.do("何とか準備も整い、明日から旅立とうという夜"),
            hero.do("$Sはベッドに寝転がりながら、ぼんやりと$smaphを眺めていた"),
            hero.do("そこには世界中のあらゆることが投稿されている",
                "多くの人の$w_tweetが流れていく"),
            hero.do("その中に$w_gameというものが流れてくる"),
            hero.talk("何だこれ？"),
            hero.do("それは$smaphを使って架空の世界で遊ぶことができる、",
                "不思議な遊具のことらしい"),
            hero.do("試しに勇者になって冒険するという、まさに今の自分に似つかわしい$w_gameをやってみる"),
            hero.talk("おお、これすごい"),
            hero.do("まだ冒険に出たことのない$Sは、これで練習ができると楽しみになる"),
            hero.do("物語は朝起こされるところから始まった"),
            w.comment("DQ3ベースで"),
            hero.do("仲間を集めてから、冒険の旅に出る"),
            hero.do("最初は城の周辺で戦うといいらしい"),
            hero.do("初めての魔物との戦闘"),
            hero.do("そこで$Sは初勝利"),
            hero.talk("なんだ、簡単じゃん", "これなら魔王だって余裕で倒せそうだな"),
            )

def sc_numa(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("ゲームの沼",
            hero.do("しかしすぐに勝てなくなる"),
            hero.do("魔物はどんどん強くなるのに、こちらのレベルは上がらない"),
            hero.talk("なんだよ、これ"),
            hero.do("そんな時、お助けアイテムなどがもらえる$w_gachaというものがあった",
                "それをやると一定の確率で旅を助ける道具や武器防具、強力な仲間などが手に入るらしい"),
            hero.talk("よーし、頼む"),
            hero.do("$w_gachaにより、一気に旅が進む"),
            hero.do("しかしまたすぐに壁が現れた"),
            hero.talk("よし、$w_gachaだ"),
            hero.do("だが最初はいいものが引けたのに、次は全然出ない"),
            hero.talk("あれ？　次どうやったら$w_gachaできるんだ？"),
            hero.do("説明を見ると、課金すると$w_gachaの券が買えるらしい"),
            hero.talk("まあ一回くらいなら"),
            hero.do("やってみると強い武器が手に入り、あっという間に倒せてしまう"),
            hero.talk("なんだ、やっぱり楽勝じゃん！"),
            hero.do("しかしまた次のボスが倒せない"),
            hero.do("$w_gachaを引く。そして当てる"),
            hero.do("だが徐々に確率が悪くなり、簡単な武器やアイテムでは攻略できなくなってくる"),
            hero.talk("なんだよこれは！　面白くないよ！"),
            hero.do("$smaphを放り出して一旦寝そべるが"),
            hero.talk("まああと一回だけなら"),
            hero.do("こうして$Sは明け方まで続いた"),
            )

def sc_billcollector(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    geruon = W(w.geruon)
    mam = W(w.mam)
    return w.scene("支払いは",
            hero.be("眠りこけている"),
            mako.come(),
            mako.talk("$heroさま？"),
            sol.come(),
            sol.talk("おーい"),
            hero.do("$makoたちによって起こされた"),
            mako.talk("何してたんですか？"),
            mako.do("全く準備ができていないのを見て"),
            hero.talk("いやあ、なんか$w_gameってのを見つけちゃってさ",
                "それで遊んでたら知らないうちに気絶してた",
                "今から大急ぎで準備するわ"),
            hero.do("顔を洗いに部屋から出ようとするが、"),
            hero.hear("玄関をどんどんするのを聞く"),
            mam.talk("ごめんなさい", "今ちょっと手が離せないから出てくれる？"),
            hero.talk("仕方ないな"),
            hero.do("誰か見に行く"),
            geruon.talk("あー、ちょっとお尋ねしますが、こちらは$heroさんのお宅でよろしいですかね？"),
            hero.talk("ええ、$heroは$meですが"),
            geruon.talk("ああ、あなたが",
                "こちら、請求書になります"),
            hero.do("それは信じられない金額が書かれていた"),
            hero.talk("あの、なんですか、これ"),
            geruon.talk("だからあなたが使った$w_gachaの請求書ですよ",
                "口座に１$w_Gもないんだから当然全部借金な訳ですよ",
                "それが支払われないので、$meが来ました"),
            hero.do("それは借金の取り立てだった"),
            )

def sc_deadend(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    geruon = W(w.geruon)
    return w.scene("借金取り",
            hero.be(),
            hero.do("借金取りに追われて、逃げ出す"),
            hero.do("崖に追い詰められる"),
            geruon.be(),
            geruon.talk("で、払ってもらえますかね？"),
            hero.do("$Sは追い詰められて、崖から落下した"),
            )

## episode
def ep_poor(w: World):
    return w.episode("3-3.貧乏なう",
            sc_playgame(w),
            sc_numa(w),
            sc_billcollector(w),
            sc_deadend(w),
            ## NOTE
            ##  - ゲームを知る勇者。そこで冒険ができることを知った
            ##  - ゲームにはまり、準備資金が全部なくなる
            ##  - 借金取りに追われて、逃げているうちに崖から落ちて勇者は死んだ
            )
