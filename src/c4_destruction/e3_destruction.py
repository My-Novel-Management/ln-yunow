# -*- coding: utf-8 -*-
"""Episode: 4-3.全滅なう
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
def sc_ordertobuster(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    mam = W(w.mam)
    arnold = W(w.arnold)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("魔王退治を注文する",
            hero.be(),
            hero.do("翌朝、心地良い目覚めを迎えた"),
            hero.do("冒険に出る心の準備をして、二人を待った"),
            inside.look("朝日が差し込んでいる部屋",
                "用意が整ったバックパックが部屋の壁際に置いてある"),
            inside.look("テーブルの上のお菓子の空が散乱している"),
            hero.think("それすらも祭りのあとみたいに思えて、微笑む"),
            sol.come(),
            mako.come(),
            hero.do("二人がやってきて、では出発と意気込むが"),
            hero.talk("ちょっと聞きたいんだけどさ"),
            mako.talk("何ですか？"),
            hero.talk("ここ見てよ、ほら"),
            hero.do("そこには『魔王退治』とある"),
            hero.talk("これ注文したら、どうなるの？"),
            mako.talk("誰かの悪戯じゃないですか？",
                "$w_amazonって素人も出品できるんですけど、詐欺とかあるんで"),
            hero.talk("でももしこれ本物だったらさ、これで誰かが代わりに魔王退治してくれるってことなんじゃないの？"),
            mako.talk("仮にそうだとしても流石に安すぎませんか？"),
            hero.do("表示されている価格は一万$w_Gだ",
                "ちょっといい料理を頼めばそれくらいになる",
                "いい宿で宿泊したらこんな金額では無理だった"),
            hero.talk("まあ、ためしに注文してみるか"),
            hero.do("注文ボタンを押した"),
            hero.talk("あ、やっぱ何も起こらないな"),
            mako.talk("そうですよ", "そもそも魔王を倒そうだなんて"),
            hero.do("その時、空が晴れる"),
            sol.talk("どういうこった？　最近こんな天気見たことないぞ"),
            hero.do("魔王が現れて以来、ずっと空は淀んでいた",
                "雲に覆われ、僅かな晴れ間をみんなは貴重に思っていた"),
            hero.talk("あ……"),
            mako.do("$Sも自分の$smaphを注目している"),
            hero.do("そこには一斉に「魔王退治されたって？」という$w_tweetが流れていた"),
            hero.do("そこに城から使いがやってくる"),
            mam.be(),
            mam.talk("$k_hero、お客様よ"),
            arnold.come(),
            arnold.look("きっちりした制服、詰め襟",
                "金色の髪の毛が外まきロール"),
            arnold.talk("$hero様、王がお呼びです"),
            stage=w.on_heroroom_int,
            day=w.in_daimaou, time=w.at_morning,
            )

def sc_invitecastle(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    king, lina, mini, arnold = W(w.king), W(w.lina), W(w.minister), W(w.arnold)
    sold = W(w.soldier)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("王宮に招かれる",
            hero.come(),
            sol.come(),
            sold.be("沢山の兵士が並んでいる"),
            inside.look("謁見の間に沢山の人が並ぶ"),
            sol.do("緊張している"),
            sol.talk("$me、城なんて入ったことないよ"),
            hero.talk("何緊張してんだよ"),
            hero.do("城へとやってくる$Sたち"),
            hero.do("どうやら本当に魔王が倒されたらしい",
                "そういう報告があったと説明される"),
            king.talk("よくぞ魔王を倒してくれた、$w_Yよ！"),
            hero.talk("あー、はい"),
            hero.think("本当は何もしていないが、とりあえず黙っておこうと"),
            king.talk("こんなにめでたいことはない",
                "今夜は盛大な祝宴会を催そうと思っておるが、当然参加してもらえるだろうな？"),
            hero.talk("それはもう喜んで"),
            sol.talk("おい、賞金の話は？"),
            hero.talk("ああ、そうだった",
                "あの、王様", "それで魔王退治の賞金の話なんですが"),
            king.talk("手続きがあるので、また明日にでも秘書から話があると思う",
                "とにかく、これで世界に平和が戻った",
                "ありがとう"),
            hero.do("$makoの姿はなかった"),
            stage=w.on_audienceroom,
            time=w.at_midmorning,
            )

def sc_party(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    king, lina, mini, arnold = W(w.king), W(w.lina), W(w.minister), W(w.arnold)
    sold = W(w.soldier)
    daimaou = W(w.daimaou)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("宴会",
            hero.be(),
            sol.be(),
            hero.explain("その夜、城の舞踏会用のホールでは盛大な宴が開かれた",
                "芸人やアイドル、歌手など、様々な人が呼ばれ、みんなで楽しんだ"),
            inside.look("鳳凰の間と呼ばれる一番最上クラスのホール",
                "金や銀を使った意匠を凝らした壁の模様、柱飾り"),
            sol.talk("$k_makoも来ればよかったのにな"),
            hero.talk("なんかあれだって、城みたいに人がいっぱいのところは苦手だとか"),
            hero.do("$Sは$smaphにメッセージを残して消えた$makoのことを気に掛けながらも、",
                "あてがわれた美人たちに鼻の下を伸ばしている"),
            inside.look("王様や姫様もいて、賑やか",
                "沢山の貴族や家臣は壁際に並び、立食と歓談を楽しんでいる"),
            lina.be(),
            king.be(),
            lina.look("淡いピンクのドレス姿で、長い金髪を丁寧に編み込みしてある"),
            hero.do("姫を見て見とれている",
                "初めてその顔を見ている"),
            lina.do("見返して口元を隠して笑っている"),
            hero.talk("いやあ、かわいいな"),
            sol.talk("なにデレデレしてんだ？", "$k_makoが怒るぞ"),
            hero.talk("いやでもさあ"),
            sol.do("$Sは飯をごちそうになっていた"),
            hero.do("と、突然、雷鳴が届く"),
            daimaou.voice("$meは$S",
                "この世界の全てを闇へと返すものなり",
                "お前ら人間の存在は許さぬ",
                "これより全てを無に返す作業に入る"),
            hero.do("その声に続いて、悲鳴が上がる"),
            hero.go("外に出る"),
            stage=w.on_hall2,
            time=w.at_night,
            )

def sc_daimaou(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("大魔王",
            hero.come("街に出てくる"),
            outside.look("空が真っ暗になっている",
                "だがそれは大量の飛空型の魔物の姿だと気づく"),
            hero.do("街に出ると、そこかしこで人が襲われていた"),
            hero.do("大魔王が現れて、空から大量の魔物が襲いかかってくる"),
            hero.do("地上のあちこちで死霊が湧き出し、人々は発狂して逃げ惑った"),
            hero.do("こうして世界は闇に葬り去られた"),
            stage=w.on_castletown1,
            )

## episode
def ep_destruction(w: World):
    return w.episode("4-3.禁断の注文なう",
            sc_ordertobuster(w),
            sc_invitecastle(w),
            sc_party(w),
            sc_daimaou(w),
            ## NOTE
            ##  - ママゾンに「魔王退治」とあるから遊びで注文してみる
            ##  - 魔王が退治されたと報告がきて、城に招かれる
            ##  - しかしそこで大魔王が出現し、世界は滅ぼされた
            )
