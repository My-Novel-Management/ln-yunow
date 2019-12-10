# -*- coding: utf-8 -*-
"""Demo: chapter 10
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def sc_confession(w: World):
    hero, mako, sol, yula = w.hero, w.mako, w.sol, w.yula
    return w.scene("魔子の告白", "魔子は自分が魔王だと勇者たちに話す",
            w.talk(mako, "$meが魔王なんです"),
            w.act(hero, "驚く$Sたち"),
            # NOTE: 魔子が魔王の石を使って戻さないと世界が消される
            #   ヘイトによって生み出されたヘイトの魔獣。それが世界を滅ぼす
            w.talk(hero, "$meが犠牲になれば助かるんだろ？"),
            w.think("どうせまた蘇るだろうし、と思っている"),
            w.talk(mako, "それは勇者の力じゃないんだ"),
            w.look("彼女が手にした魔王の石"),
            w.talk("これが世界を再構成していただけなんだ"),
            w.talk("これを使う"),
            w.talk(yula, "それ使ったらあんたが消滅するって言ってたじゃない"),
            w.talk(hero, "そうなのか？"),
            w.act(mako, "頷く"),
            w.talk(hero, "だったら$meが消えた方が何倍もマシだ"),
            w.act("取り戻した勇者の剣を構える"),
            w.look("ヘイトの魔獣は彼をやっと探し当てた"),
            w.talk("こっちこいよ！　$meが相手だ"),
            w.talk(mako, "$n_hero様がいくら消えてもその魔獣は消えないんです！"),
            w.talk(hero, "え？"),
            w.talk(mako, "もうあそこまで大きくなったらどうしようもない。みんなを飲み込んでどんどんふくれあがり、やがてこの大地をすべて覆い尽くしてしまう"),
            w.talk("だからコレを使うしかないんです。全部なかったことにして、元のような世界に戻すしか"),
            w.talk(hero, "$meはそれでも！"),
            w.move("向かっていく"),
            w.act("だが魔獣の小さな火の玉ひとつで焼かれる"),
            w.talk(sol, "何やってんだよ！"),
            w.talk(hero, "やっぱ無理！"),
            w.talk(hero, "そうだ！　課金だよ！"),
            w.talk(sol, "ついに頭くるったのか？"),
            w.talk(hero, "あれって人の心が増幅したものなんだろ？　だったらUR出れば解消するって！"),
            w.act("誰もが呆れた顔だが"),
            w.talk(yula, "いけるかもね"),
            w.look("スマフを見て、そこに流れる憎悪の中にフェイクで大量に詫石配布の告知をいれたらそれに食いつく人が多数いる"),
            w.talk(yula, "結局は何かしらストレス発散対象探してるだけだから"),
            w.talk(mako, "え？　じゃあ"),
            w.talk(hero, "$n_makoは魔王。つまりこのゲームの運営会社のボスみたいなもんだろ？　詫び石配布、いけるんじゃないか？"),
            w.talk(mako, "ちょっと待ってね"),
            w.act("連絡を取っている"),
            w.talk(mako, "年末年始イベント向けに準備してたの、あるって！"),
            w.talk(hero, "だったらそれでいける！"),
            w.act("$n_makoが連絡を取り、詫び石大量配布が始まった"),
            w.look("ヘイトの魔獣の動きが止まる"),
            w.look("ガチャを回し始めた"),
            w.look("当たったらしい。少し小さくなる"),
            w.talk(hero, "もっと配るんだ！"),
            w.look("大きくなったり、縮んだり"),
            w.look("そしてURを引いて、発光した"),
            w.look("魔獣が消える"),
            w.talk("やったぞ！"),
            )


## episode
def ep_demo_confess(w: World):
    return w.episode("魔王の告白", "魔子は魔王だと告白するが",
            sc_confession(w),
            )
