# -*- coding: utf-8 -*-
"""Episode: 6-2.ゴブリンの巣なう
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
def sc_saving(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    clerc, malta = W(w.clerc), W(w.malta)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("まずは教会で",
            hero.be(),
            hero.do("冒険に出る前に教会で祈りを済ませる"),
            sol.be("外で待っている"),
            mako.be("同じく外で"),
            hero.do("出てくる"),
            hero.talk("さあ、行こうか"),
            stage=w.on_church1_int,
            day=w.in_quest4, time=w.at_afternoon,
            )

def sc_goblinnest(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$goblinの巣",
            hero.come("荷物を背負い歩いている"),
            sol.come(),
            mako.come(),
            outside.look("初めて見た街道の風景"),
            outside.look("広々として、そこら中に低木が茂る",
                "遠方にくつろぐ軟体の野生の魔物がいる"),
            outside.look("街道は看板が立てられ、地道が伸びている",
                "城下町のメインストリートのような石畳ではない",
                "道の脇にぽつりぽつりと石が埋め込まれている"),
            hero.look("バックパックを背負い、新しい革のブーツ",
                "王から支給品の剣を腰につけている", "意外と重い"),
            sol.look("変わらない服装",
                "赤いぼさぼさ髪をバンダナで巻いて、背中の大剣",
                "肩にズタ袋を下げている", "そこには寝袋やキャンプ用品"),
            mako.look("黒の帽子とマント、ピンクの縞模様",
                "手にはステッキを持っている",
                "背中に小さなバックパック"),
            hero.do("準備を整えて街道を歩いて目指している$Sたち"),
            hero.talk("$goblinも群れてなきゃ大丈夫なんだよね？"),
            hero.think("大見得きったものの不安な$S"),
            sol.talk("はぐれ$goblinならよく出会うが、手慣れた旅人なら数撃の相手だよ",
                "そもそもやつら痛みにかなり弱いからな",
                "見た目こそ醜悪だが、あれで臆病で、一人だとほとんど襲いかかってこない",
                "だが自分たちの方が強いとか、集団が大きいとか、そういう時には容赦ないからな",
                "全く見た目通りに胸糞悪くなる奴らだよ"),
            sol.do("昔に仲間を殺されたことを思い出していた"),
            hero.do("街道を外れ、地図に沿って西側に向かう"),
            outside.look("遠くには山が見える"),
            hero.do("地図を眺めると森の中には湖もあるようだ",
                "そこに山からの川が流れ込んでいるらしい"),
            hero.talk("そういえば$goblinって綺麗な水に弱いんだっけ？"),
            mako.talk("$goblinだけじゃありませんよ",
                "基本的に魔族のものは綺麗な場所に弱いです",
                "だから人間の街って聖なるものを中心にして作られてるじゃないですか？",
                "あれは魔物を寄せ付けないようになっているんですよ"),
            w.eventPoint("魔族について", "魔のものは聖なるもの、綺麗なものに弱い"),
            hero.think("そういえばそうだな、と"),
            hero.do("森に入るところに$goblinがいるのが見えたが、すぐにこちらに気づいて逃げていった"),
            hero.talk("あ、逃げた"),
            stage=w.on_jihanpath,
            )

def sc_usingsmaph(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$smaphを使おう",
            hero.be(),
            sol.be(),
            mako.be(),
            sol.talk("まずいな", "あれ、すぐに仲間に連絡してるぞ"),
            hero.talk("ど、どど、どうしよう"),
            mako.talk("こんなときは、これですね"),
            mako.do("$Sは$heroたちに自分の$smaphを見せる",
                "相手の位置情報が表示されている",
                "$smaphを持っている者の場所が表示されるらしい"),
            mako.talk("$smaphは$w_denpaってもので$w_webと繋がってます",
                "それをとらえて表示するのがこの$w_apliです"),
            mako.do("位置情報特定$w_apliを見せる"),
            hero.talk("この赤い点がいっぱいあるけど"),
            mako.talk("全部$goblinですね",
                "最近はみんな持ってるみたいです"),
            hero.talk("こ、こんなにいるの？？"),
            mako.talk("そうですね", "でも巣っていうくらいだから普通ですよ？",
                "どうします？　焼きます？"),
            hero.talk("とにかくボスまで見つからないように潜みながら行動して、",
                "ボスだけ倒そう",
                "そうすれば統率とれなくなってみんな逃げ出すだろ？"),
            mako.talk("じゃあ、そういう戦略で"),
            stage=w.on_jihanforest,
            day=w.in_quest4, time=w.at_morning,
            )

def sc_intotheforest(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("森に入る",
            hero.do("$smaphを見ながら、相手があまりいない場所を選んで歩く"),
            sol.talk("$goblinにあまり会わないのはいいけどよ"),
            hero.do("道なき道を、分け入る"),
            sol.do("不満そう",
                "先頭を歩く一番図体のでかい$Sは、中古の$leatherguardが傷つきまくっている"),
            mako.talk("じゃあ全部一気に相手にしますか？"),
            sol.talk("わかってるよ", "言ってみただけだ",
                "それより$k_hero",
                "どうやってボスを見つけるんだ？"),
            hero.talk("この赤い点を見てると、定期的に同じ場所に向かうのがあるだろ",
                "きっとそこにボスがいるんだ",
                "この森の北のところ",
                "そこを背後から襲う"),
            hero.think("これで完璧だ", "そう考えていた"),
            )

def sc_surrounded(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("囲まれる",
            hero.do("もうすぐボスの位置だ、というところまであまり遭遇せずにきた"),
            hero.do("しかしそこで$makoがいないことに気づく"),
            hero.talk("あれ？", "$makoはどこ？"),
            sol.talk("気づいたら見えなくなってたな",
                "どこかではぐれたか？"),
            hero.do("慌てて$smaphで探してみる",
                "彼女のピンクの点は反対側にいる"),
            hero.talk("迷ったみたいだね", "なんか入り口の方に戻ってる"),
            hero.do("と、$goblinに遭遇する"),
            sol.talk("一匹か",
                "やるぞ"),
            hero.talk("ああ"),
            sol.do("$Sがぶちころす"),
            hero.do("しかしその裏に別のがいて、逃げていった"),
            hero.talk("まずいな"),
            hero.do("$w_apliで確認すると気づくとどこもかしこも囲まれて逃げ道がなくなっている"),
            sol.talk("何だよ、これは"),
            hero.talk("罠だったんだ", "やつら最初から$meたちをここに誘い込もうとしてたんだよ！"),
            hero.do("$makoから連絡が入っている"),
            hero.talk("$makoが燃やそうかだって",
                "どうも、あっちも囲まれてるらしい"),
            sol.talk("燃やしたら延焼して街も焼けるからやめろって言っとけ",
                "それより、来るぜ"),
            gob.do("茂みから数匹が現れる"),
            hero.talk("やるしかないか"),
            sol.talk("とにかくここを突破してさっさとボスやっちまおう"),
            hero.talk("いや、それは無理"),
            hero.do("見ると既にボスの前には$goblinが三十匹以上あつまり、壁となっていた"),
            )

## episode
def ep_goblin_nest(w: World):
    return w.episode("6-2.ゴブリンの巣なう",
            sc_saving(w),
            sc_goblinnest(w),
            sc_usingsmaph(w),
            sc_intotheforest(w),
            sc_surrounded(w),
            ## NOTE
            ##  - 街道に巣を作っているというゴブリン退治にやってきた
            ##  - スマフで位置情報を確認しながら、ボスだけ的確に殺そうという相談
            ##  - しかしゴブリンたちもスマフを持っていて、逆に取り囲まれてしまう
            )
