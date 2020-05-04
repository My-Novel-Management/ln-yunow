# -*- coding: utf-8 -*-
"""Episode: 1-1.勇者なう
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
def sc_invitecastle(w: World):
    hero = W(w.hero)
    king, lina, arnold = W(w.king), W(w.lina), W(w.arnold)
    minst = W(w.minister)
    inside, outside = W(w.inside), W(w.outside)
    mam, dad = W(w.mam), W(w.dad)
    return w.scene("お城に呼ばれる",
            hero.come("城へとやってきて"),
            king.be(),
            lina.be(),
            minst.be(),
            arnold.be(),
            inside.look("豪華な部屋に王や兵士が揃っている"),
            hero.do("緊張気味に膝をつけて、頭を下げている",
                "普段なら謁見することすら叶わない"),
            king.talk("頭を上げてよいぞ"),
            inside.look("カーテンの向こう側から声が"),
            arnold.talk("頭を上げなさい"),
            hero.do("呼び出しにきた秘書の男性が、声をかけて、顔を上げる"),
            hero.talk("えっと、あの$meって、今日なんで呼ばれたんですか？"),
            king.talk("説明しておらんのか？"),
            arnold.talk("い、いえ、ちゃんと説明して来てもらったのですが"),
            arnold.talk("今日は$hero様が$smaphの懸賞に当選されて、それでお呼びしたのです"),
            hero.talk("あー！　マジで？"),
            arnold.talk("マジ、で？"),
            hero.talk("えっと、本当ですか？"),
            arnold.talk("はい", "まずは王の言葉を"),
            king.talk("まさかあの英雄$dadの息子が選ばれるとは思うておらなんだが、",
                "これもまた何かの宿縁であろう",
                "これを使い、魔王を探し出し、お主にはなんとしても世界の平和を取り戻してもらいたい"),
            hero.do("$smaphを手に入れる"),
            hero.talk("これが、念願の$smaph……"),
            hero.think("みんなが憧れる$w_magicitemを手にして感動している"),
            king.talk("よろしく頼んだぞ、$w_Yよ！"),
            camera=w.hero,
            stage=w.on_castletown1,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_aboutsmaph(w: World):
    hero = W(w.hero)
    king, lina, arnold = W(w.king), W(w.lina), W(w.arnold)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$smaphについての注意事項",
            hero.come("城のホールに戻ってくる"),
            arnold.come(),
            arnold.talk("こちらの使い方ですが、すべて$smaphで見られるようになっております",
                "$smaphのご経験は？"),
            hero.talk("いや、初めてですよ"),
            w.eventPoint("$smaphについて", "$arnoldから$smaphの使い方があると教わる"),
            arnold.do("$Sは自身の$smaphを見せながら、旅の手引きがあると教える"),
            hero.talk("おー！　すげー！"),
            hero.do("とにかく見ることなすこと何でも凄いと言う$S"),
            arnold.talk("こちらに全部書いてあります",
                "困ったら必ず読むようにして下さい"),
            arnold.talk("あと、現金は用意できませんでしたが、",
                "冒険資金としてこちらに$w_paypayで十万$w_Gほど用意いたしましたので、",
                "役立てていただければと"),
            hero.talk("じゅ、十万も！"),
            arnold.talk("旅の資金としては心もとないと思いますが、",
                "わが国も魔王が現れて以降、他国との貿易もままならず、",
                "これだけ準備するのがやっとで"),
            hero.do("他にも証明書の類も一緒にもらった"),
            hero.talk("これがあればどこも使い放題ですか？"),
            arnold.talk("わが国限定ですが、王族や上級貴族、軍人のみが使えるものです"),
            hero.do("いたれりつくせりに舞い上がっていた"),
            )

def sc_thisworld(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("この世界について",
            hero.come("城から出てくる"),
            hero.do("門番ににこにこと挨拶をして、とりあえず教会に向かおう"),
            )

def sc_yushanow(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("勇者なう",
            w.comment("ここで最初につぶやいてから、教会でセーブしたように見えるが、教会セーブは関係ないので、このままでいいです"),
            hero.do("$smaphに『勇者なう』と$w_tweetする"),
            hero.do("その$w_tweetはまたたく間に拡散され、画面には大量に「$w_Y？」の呟きが流れてくる"),
            hero.talk("ほー、これなんかすごいな！"),
            hero.think("こうして$w_Yは何をしたのかも分からないまま、増えていく数字を見て楽しんでいた"),
            )

## episode
def ep_start(w: World):
    return w.episode("1-1.勇者なう",
            sc_invitecastle(w),
            sc_aboutsmaph(w),
            sc_thisworld(w),
            sc_yushanow(w),
            ## NOTE
            ##  - 勇者は王宮に呼ばれて勇者に当選したからスマフをもらった
            ##  - 魔王退治を命じられる
            ##  - スマフをもらい、喜ぶ勇者
            )
