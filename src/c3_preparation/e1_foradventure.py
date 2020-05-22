# -*- coding: utf-8 -*-
"""Episode: 3-1.冒険準備なう
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
def sc_introducemako(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    mam = W(w.mam)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$makoの自己紹介",
            hero.be(),
            sol.be(),
            mako.be(),
            mam.be(),
            mako.talk("はじめまして"),
            mako.look("小柄でピンクの髪",
                "黒い衣装は魔法使い然としている"),
            inside.look("外は夜になっている",
                "部屋の明かりが扉の方へと漏れ出す",
                "奥のキッチンからは夕食を作る音が響く"),
            w.eventPoint("人物紹介", "$makoの紹介"),
            sol.talk("知り合いじゃねえの？"),
            hero.talk("えっと、全然", "初めて、ですよね？"),
            mako.talk("ほんとは初めてじゃないんです"),
            mako.do("$Sはそう言って自分の$smaphを見せる",
                "そこには大量に$heroの$w_gazouがある"),
            hero.talk("これは？"),
            mako.talk("ずっと見てました"),
            sol.talk("おい、この女ストーカーってやつじゃ"),
            hero.talk("ずっと？"),
            mako.talk("はい。ずっと"),
            mako.talk("$meと結婚して下さい"),
            mam.do("お茶を持って入ってきて"),
            mam.talk("あ、あら、そういうご関係だったの？",
                "母さん全然知らなくて"),
            hero.talk("ち、違うから！　とにかくそれ置いて出てって"),
            mam.talk("あとでちゃんと話、聞かせてよね？　$heroちゃん"),
            hero.do("嫌な汗をかいている"),
            camera=w.hero,
            stage=w.on_herohome_int,
            day=w.in_reset1, time=w.at_night,
            )

def sc_preparation(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    mam = W(w.mam)
    return w.scene("冒険の準備だ",
            hero.be(),
            sol.be(),
            mako.be(),
            hero.explain("$Sの部屋に三人でいる"),
            hero.do("なんとか$makoを説き伏せて、一緒に冒険して魔王を倒したら結婚するという約束で延命した"),
            sol.talk("で、どうすんの？"),
            mam.come("お茶菓子を持って入ってくる"),
            mam.talk("はい、どうぞ"),
            mako.talk("ありがとうございます"),
            hero.talk("え？　なんでそんなもん出してんの！？"),
            mam.talk("あら、$k_hero", "いつもお客様がいらした時には出してるでしょう",
                "もう嫌ねえ", "妙なこと言って"),
            hero.explain("そもそも友人がくることはなかったが、",
                "誰か来たとしてもお茶すら出さないのが普通だった"),
            mam.do("お茶などを持ってきて、$makoと仲良さそうにしている"),
            hero.talk("$k_mam！"),
            mam.talk("わかってるわよ。それじゃあね"),
            mam.do("既に$makoと打ち解けたよう",
                "部屋を出ていく"),
            mam.go(),
            hero.do("母親を追い出して、ほっとするが"),
            mako.do("$Sはにこにことしてじっと$heroを見つめている"),
            hero.talk("えっと、あの……さ"),
            mako.talk("なんでしょうか、$k_hero"),
            hero.talk("ちょっと離れてくれないかな？"),
            mako.talk("一メートルでいいですか？"),
            hero.talk("いや、もうちょっと"),
            hero.do("交渉して何とか一メートル半は離れてもらうことになった"),
            sol.talk("で、どうすんだ、これから",
                "$k_heroは本気で魔王を退治するつもりなのか？"),
            hero.talk("えっとさ、実は$me、$w_Yなんだわ"),
            w.eventPoint("勇者の名前", "$solに$w_Yと告白"),
            sol.do("本当か？　と疑いの視線"),
            sol.talk("お前それ、絶対他の人間に言うなよ",
                "頭おかしいって思われるぞ"),
            hero.talk("いやほんとなんだって！"),
            hero.do("$umarkを見せる"),
            sol.talk("マジかよ",
                "お前それオークションで手に入れたんだろ？"),
            hero.talk("いやそんなことしてないから！", "王様からもらったんだよ！",
                "$smaphと一緒にさ"),
            hero.explain("なんとか二人に経緯を話して了解してもらったが、",
                "$w_Yであることは黙っておこうということになった",
                "$Sとしてもその方が助かる"),
            hero.think("最初の時のあの金色の魔物が頭をよぎった"),
            sol.talk("ところで魔王退治っていうけどさ、",
                "魔王がどこにいんのか分かってんのか？",
                "それ以前に旅とかしたことあるのかよ？"),
            hero.talk("いや、全然"),
            sol.talk("旅なめんな！",
                "すぐそばに死神が転がってる世界だぞ"),
            hero.talk("けど$solはここまで来られたんでしょ？", "だったら$meだって大丈夫だよ"),
            sol.talk("どういうことだよ"),
            mako.talk("もう二人とも口論しないで下さい",
                "それで新婚旅行はどれくらいの予定なんですか？",
                "$meは一月くらいはゆっくり過ごしたいなって思ってるんですけど"),
            hero.do("二人して$makoを無言で見る"),
            mako.talk("もう、わかりましたよ", "一旦結婚の話は置いときます",
                "それでどうするんですか？"),
            sol.talk("あのな"),
            sol.do("そう言って$Sは一体旅に何が必要なのか説教を始めた"),
            stage=w.on_heroroom_int,
            )

def sc_fortrip(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("旅に必要なもの",
            hero.be(),
            sol.be(),
            mako.be(),
            sol.do("旅について熱弁している"),
            sol.talk("あのな、旅っていうのは基本、なるべく荷物を少なくすることが大事だ"),
            hero.do("それをあくびしながら聞いている",
                "$smaphを操作しつつ"),
            mako.do("$heroを見てにこにことしてお茶を飲んでいる"),
            hero.talk("準備に沢山必要なものがあるって言ったのに、逆じゃないか"),
            sol.talk("移動するのに常にどれくらい荷物を持てるか、考えたことあるか？"),
            hero.do("$solから色々と学ぶ"),
            )

def sc_gotomarcket(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("買い物に行こう",
            hero.be(),
            sol.be(),
            mako.be(),
            sol.talk("という訳だよ"),
            hero.think("話が長い、と思いつつ"),
            hero.talk("じゃあ、必要なものはメモったから、とりあえず市場に行くか"),
            hero.do("相談して、とりあえず必要なものを翌日市場に買いに行こうということになった"),
            )

## episode
def ep_ready(w: World):
    return w.episode("3-1.準備をするなう",
            sc_introducemako(w),
            sc_preparation(w),
            sc_fortrip(w),
            sc_gotomarcket(w),
            ## NOTE
            ##  - 魔子の自己紹介
            ##  - 仲間と一緒に冒険の準備を考える
            ##  - 必要なものを買い出しに行く
            )
