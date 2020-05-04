# -*- coding: utf-8 -*-
"""Episode: 4-1.困ったなう
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
def sc_retry(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    clerc = W(w.clerc)
    return w.scene("再び仲間とともに",
            hero.be("教会で目覚めた"),
            clerc.talk("どうかしましたか？"),
            hero.talk("いや、あの……なんでもないです"),
            hero.do("$smaphを確認して、そこにゲームの宣伝があるのを見つける",
                "思わず手が伸びそうになったが、必死に我慢して外に出ていく"),
            hero.do("家に戻ると$solたちがいた"),
            camera=w.hero,
            stage=w.on_castletown1,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_meeting(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("準備会議",
            hero.be(),
            sol.be(),
            mako.be(),
            sol.talk("で、どうするんだ？"),
            hero.talk("準備を整えるにもとにかく金がいる",
                "けど$meたちは金がないんだ",
                "まずはこの問題をどうにかしないといけない"),
            sol.talk("じゃあ働くしかないな",
                "日銭を稼ぐなら体を使うのが一番だぜ？"),
            sol.do("$Sはここまで畑仕事や土木作業を手伝いながら、日銭を稼いで旅をしてきたと話す"),
            w.eventPoint("$solの過去", "旅の道中を働きながら過ごしてきた"),
            hero.do("$solと自分を見比べて、無理だと思う"),
            hero.talk("そういうのは$solに任せるよ",
                "$meはもっと楽して稼ぐ方法を考えたいんだ"),
            sol.talk("楽して稼ぐだ？",
                "魔王を倒そうってやつがそんな考えでどうすんだよ",
                "魔王退治なんて誰もやりたがらない、この世で最も面倒くさくて大変なことだろうがよ？"),
            hero.talk("それはそれ、これはこれ",
                "楽できるところは楽しないと先が続かないものだよ、$sol君"),
            sol.talk("こいつ一回頭叩き割って中身引きずり出して洗ってやりたい"),
            hero.talk("はあ、どっかに金落ちてないかな"),
            mako.talk("ありますよ？"),
            hero.talk("え？"),
            mako.talk("だから金なら$meがいっぱい持ってますって"),
            )

def sc_richmako(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("$makoは金持ち",
            w.eventPoint("$makoの素性", "$makoは金持ちだと証言"),
            mako.talk("最初に言ったじゃないですか",
                "$meがいるからお金のことは考えなくていいですって"),
            mako.do("$smaphの$w_gazouを見せる",
                "そこには金塊の入った宝箱がいっぱい並ぶ部屋が映っている",
                "$makoが一緒に映っていた"),
            hero.talk("これどうしたの？"),
            mako.talk("パパのものなんですけど、ほとんど$meにくれました",
                "好きなことに使いなさいって"),
            sol.talk("なんだ$k_makoって金持ちの令嬢様だったのか？"),
            mako.talk("そんなこともないですけど、見直しました？"),
            sol.talk("おい、もう$k_heroは$k_makoとくっついちまえよ"),
            mako.talk("$meは$hero様がいいならいつでもウェルカムですよ！"),
            hero.talk("あ、それは遠慮します"),
            mako.talk("なんでー！"),
            hero.talk("それよりさ"),
            hero.do("知らない間に$Sの部屋が着飾られている",
                "ベッドもあるし、本棚には沢山の本",
                "紙は高価で、本も当然王立図書館にしかない"),
            hero.talk("これ、どうしたの？"),
            mako.talk("買いました", "いいでしょう？"),
            hero.talk("どこで？"),
            mako.talk("$w_amazonですよ", "知りませんか？"),
            mako.do("$Sは$smaphの画面を見せた"),
            )

## episode
def ep_trouble(w: World):
    return w.episode("4-1.困ったなう",
            sc_retry(w),
            sc_meeting(w),
            sc_richmako(w),
            ## NOTE
            ##  - 再び仲間を集めて家に戻った勇者
            ##  - 冒険準備の為の買い物を考えるが
            ##  - ゲームにハマってしまう
            )
