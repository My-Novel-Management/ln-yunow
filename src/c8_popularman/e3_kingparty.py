# -*- coding: utf-8 -*-
"""Episode: 8-3.王宮でパーティなう
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
def sc_party(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    king, lina, minister, arnold = W(w.king), W(w.lina), W(w.minister), W(w.arnold)
    sold = W(w.soldier)
    return w.scene("王宮パーティ",
            hero.be("王宮へとやってきている"),
            sol.be(),
            inside.look("立食形式のパーティが開かれ、"),
            sol.talk("あいつらも一緒に来ればよかったのにな"),
            hero.talk("なんか$makoは用事があるって言ってたし、",
                "$yulaは城は勘弁だって"),
            sol.talk("あいつは一応元盗賊だからな",
                "そりゃ官憲様には弱いよ"),
            sol.talk("しかしもったいねえなあ",
                "こんなにご馳走が食える機会滅多にねえのによ"),
            sol.do("大きな肉を食っている$S"),
            lina.be("$Sは座っている"),
            lina.look("白を基調とした清楚なドレス"),
            hero.do("見とれている$S"),
            lina.talk("あの"),
            arnold.talk("何でございましょうか"),
            lina.talk("えっと"),
            lina.do("耳打ちをする"),
            arnold.talk("少しだけお待ち下さい"),
            arnold.do("やってくる"),
            arnold.talk("あの、$hero様", "$lina様がお呼びです"),
            lina.talk("あ"),
            arnold.talk("姫様は直接は下々の者とはお話できないため、$meが通訳をいたします",
                "ただいまのは『はじめまして』と仰られています"),
            hero.talk("ああ、ども"),
            arnold.talk("そういった失礼な言葉遣いはやめてください、と仰られています"),
            hero.talk("いや、今何も言ってなかっただろ？"),
            hero.do("何とか言いくるめて、姫とバルコニィに出る$S"),
            hero.talk("今日はおまねきいただき、どうも、ありがとうございます"),
            lina.talk("そんな改まらなくてもいいですよ",
                "いつも$arnoldには手を焼いてますの",
                "それよりもアレ見ました！"),
            hero.do("姫は興奮気味に実況動画のことを話す"),
            lina.talk("クエスト動画だけじゃなくて、全部見ました！",
                "大ファンなんです！"),
            hero.do("サインを求められて、適当に書く"),
            lina.talk("あの、今度はどんなクエストに挑戦されるのですか？"),
            hero.talk("ドラゴンの洞窟とか"),
            lina.talk("ドラゴン！"),
            lina.do("興奮して顔が赤い"),
            hero.talk("もしよかったら今度一緒にどうですか？"),
            lina.talk("あ、そういうのはいいです"),
            hero.do("即座に断られて苦笑"),
            sol.talk("あいつ、何やってんだ"),
            sol.do("$Sはとにかくご飯を食べていた"),
            )

def sc_changing(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("人生の転機",
            hero.do("それからは更に忙しくなった"),
            inside.look("部屋は散乱状態で、資料やらが散らばっている"),
            yula.talk("ちょっとこれ何なのよ"),
            yula.do("片付け始める"),
            yula.talk("そういえば最近$mako見ないけど、来てる？"),
            hero.talk("え？　連絡は取ってるけど、これで"),
            hero.do("$smaphを見せて、実況見たとか$w_msgが来ているのを見せる"),
            yula.talk("ま、いいけどさ",
                "なんか最近景気が良さそうだなって思って"),
            yula.do("$Sが持ってきたのは今度発売される新しい商品のパンフレット",
                "そこにはアイドルの$yuiと一緒に絵になっている$heroのにやついた顔が描かれていた"),
            yula.talk("$solは？"),
            hero.talk("なんかピンの企画で呼ばれてる",
                "大食い大会とか言ってたな"),
            yula.talk("へえ"),
            hero.talk("$yulaもよかったら声かけとくよ？"),
            yula.talk("$meは目立つのはあまり好きじゃないから遠慮しとく"),
            yula.think("なんか変わったな、と思って外に出ていく"),
            )

def sc_population(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    mam = W(w.mam)
    kiyoe = W(w.kiyoe)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("勇者大人気",
            hero.do("人気者になり、豪邸を借りてそこに移り住んだ"),
            mam.talk("あんたのお陰でまさかこんな場所に住めるようになるなんて！",
                "これであの人さえ帰ってきてくれたら"),
            hero.talk("一応それ、局の人に頼んで探してもらってるからすぐに見つかると思うよ"),
            mam.talk("まあ、なんて頼りになるんでしょう",
                "あんたを育てたかいがあったわ"),
            mam.do("にこにこで出ていく"),
            mako.come(),
            hero.talk("ああ、来たんだ",
                "すごいだろ、ここ！", "もうあの頃の$meとは違うんだ",
                "何でも買ってやれるぞ"),
            mako.talk("なんか、すごいね",
                "それでさ、いつ冒険に出るの？"),
            hero.talk("冒険はさんざん企画でやってるから、しばらくはいいよ",
                "あれは仕事だ"),
            mako.talk("そっか"),
            )

## episode
def ep_party_incastle(w: World):
    return w.episode("8-3.王宮でパーティなう",
            sc_party(w),
            sc_changing(w),
            sc_population(w),
            ## NOTE
            ##  - 招かれた王宮で、勇者は王から褒められる
            ##  - 姫から言い寄られたり、一気に人生が変わる
            ##  - 次々と出演依頼がきて、金も名声も手に入れた気分だった
            )
