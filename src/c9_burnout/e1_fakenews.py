# -*- coding: utf-8 -*-
"""Episode: 9-1.フェイクニュース
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
def sc_fakenews(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("フェイクニュース",
            hero.be(),
            mako.be(),
            sol.be(),
            yula.be(),
            hero.do("豪邸での暮らすようになって半月ほど、"),
            hero.do("お手伝いをはべらせ、玉座とまごう豪華な椅子に座っている"),
            inside.look("豪華な寝室",
                "床は絨毯が敷かれている",
                "大きなモニタには放送が流れている",
                "特注の$tabletがある"),
            hero.talk("これまっずいな", "次"),
            hero.do("お手伝いが次々に各地の産物を差し出す"),
            yula.talk("$hero様、お仕事の予定ですが"),
            yula.do("$Sはマネージャーを務めている"),
            hero.talk("今日は何だ？"),
            yula.talk("午前中に雑誌インタビューが十件と、グッズ開発会議、あと午後からは"),
            hero.talk("アイドルと合コンしたい"),
            yula.talk("今調整中です"),
            hero.talk("なあ", "忙しすぎると思うんだ",
                "$meはもっと楽をして稼げると思ってたんだが、どうしてこうなった？"),
            yula.talk("何言ってるんですか！",
                "稼げるときに稼いどかないと旬なんてあっという間なんですよ！"),
            hero.talk("わかったよ",
                "ところで$makoたちは？"),
            hero.do("$Sは自分の$smaphでゲームをしながら尋ねる"),
            yula.talk("そうですね"),
            yula.do("自分の$smaphで確認し"),
            yula.talk("これ何だろう"),
            yula.do("そこに流れてきた一本のニュースに目を留める",
                "そこには『勇者の悪事まとめ』とあった"),
            yula.think("どうせやっかみだろうと、無視して削除する"),
            camera=w.hero,
            stage=w.on_heromansion_int,
            day=w.in_richdays, time=w.at_afternoon,
            )

def sc_worker(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    cedo = W(w.cedoros)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("労働者",
            w.symbol("　　　　※"),
            mako.come("一方$Sは$heroと決別した$solに会いに来ていた"),
            sol.be(),
            cedo.be(),
            mako.talk("あ、いた"),
            cedo.talk("おーい！　危ないから勝手に入んな！"),
            sol.talk("あー、親方すんません", "$meの知人すわ"),
            mako.do("$solは今までみたいに土木作業で汗を流していた"),
            sol.talk("おう、$k_makoか", "何度誘っても無駄だから",
                "$meはな、ああいうくっちゃべったりしてるだけで金が湧いてくるみたいなのは好きじゃねえんだ",
                "やっぱ人間こうして体を動かしてなんぼだと思ってる",
                "そもそも$k_heroはもう魔王退治はする気ないのか？"),
            mako.talk("どうなんですかね",
                "$meは別に$hero様が楽しく暮らしてくれていればそれでいいんですけど"),
            sol.talk("何だよ、その顔"),
            mako.do("$Sは自分の$smaphを見せる",
                "そこには勇者への悪口がいっぱい書かれている"),
            sol.talk("何だこりゃ？"),
            mako.talk("嫉妬とかだと思うんですけど、でもこれは"),
            mako.do("そこにはゴブリンと仲良さそうに話したりしている勇者の映像が出回っていた"),
            sol.talk("どういうことだ？"),
            stage=w.on_constfield,
            )

def sc_burnout(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("動画炎上",
            hero.come("自宅に戻ってくる"),
            hero.do("ある日のことだった"),
            hero.talk("ん？　何だ？"),
            outside.look("大きな門扉、そこの前に大量のゴミ",
                "壁にも落書きがある"),
            hero.do("自宅に戻ってきた$Sは玄関先にゴミをぶちまけられているのを見た"),
            hero.talk("何だこれは？"),
            yula.talk("すぐに片付けさせます"),
            hero.do("部屋に戻り、$smaphを確認すると通知で埋まっている"),
            hero.talk("なんだこれは！"),
            hero.do("そこには悪口ばかりが投げつけられている"),
            hero.do("別の日"),
            hero.do("歩いていると石を投げつけられた"),
            hero.talk("誰だ？"),
            hero.do("通行人たちは知らんぷり"),
            hero.do("子どもが「バーカ」といって石を投げて逃げていく"),
            hero.talk("一体何なんだよ、もう"),
            hero.do("部屋に戻ると、そこに$makoがいた"),
            mako.come(),
            hero.talk("おお$mako", "最近来てなかったけどどうしてたんだ？"),
            mako.talk("これ、見て下さい"),
            mako.do("自分の$smaphを見せて説明する"),
            _.talk("$Sが魔王ということにされているんですよ"),
            hero.talk("え？　$me魔王じゃないよ？"),
            stage=w.on_heromansion_ext,
            day=w.in_burnout, time=w.at_afternoon,
            )

def sc_Iammao(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    haru = W(w.haru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("自分が魔王？",
            hero.be(),
            mako.be(),
            haru.be(),
            inside.look("執務室",
                "沢山の革製の本が並ぶ本棚",
                "マホガニーのどっしりした執務机"),
            mako.do("$heroに説明しているが、気になって仕方ない"),
            mako.talk("あの、これ誰なんですか？"),
            haru.talk("お手伝いの$Sです"),
            hero.talk("ああ、身の回りの世話を頼んでいるんだ。気にしないで"),
            mako.think("むちゃくちゃ気になるが仕方なく"),
            w.eventPoint("フェイク動画", "前に$heroに恨みを持った職人が作った"),
            mako.talk("たぶん人気に嫉妬した誰かが作ったんです"),
            hero.do("動画には沢山の文句が書かれている"),
            hero.do("それを読んでいて顔が青ざめてくる"),
            hero.talk("ひょっとしてこれ、みんな信じちゃってるの？"),
            mako.talk("そうですよ"),
            hero.talk("じゃあ、石投げられたのも？"),
            mako.talk("そうです"),
            hero.talk("マジかよ！"),
            hero.do("窓を開けてバルコニィに出る"),
            hero.talk("$meは魔王なんかじゃない！　ほんとだぞ！"),
            hero.do("思い切り罵声やものが投げつけられる"),
            hero.do("いつの間にか家の前には人が大挙している"),
            hero.talk("ほんとにほんとなんだ！　誰かが悪戯しただけなんだって！"),
            hero.do("しかし誰も聞く耳もたない"),
            hero.talk("あー、くそ"),
            hero.do("部屋に逃げ込む"),
            stage=w.on_herooffice_int,
            )

## episode
def ep_fakenews(w: World):
    return w.episode("9-1.フェイクニュース",
            sc_fakenews(w),
            sc_worker(w),
            sc_burnout(w),
            sc_Iammao(w),
            ## NOTE
            ##  - 人気者になった勇者だったがその日、勇者が実は魔王だったという動画が上がる
            ##  - 動画はまたたくまに世界中に拡散され、知らない間に家に石が投げ込まれたりする
            ##  - 理由を調べるとどうやらフェイクニュースにより勇者が魔王だったという話になっていた
            )
