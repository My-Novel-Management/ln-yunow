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
            hero.do("手にした$smaphを触りながら、王の話を聞き流している"),
            hero.look("袖のちぎれた上着に、穴の空いたブーツ",
                "まだ少年の顔立ち"),
            hero.talk("おおー！　なんだこれ"),
            arnold.do("咳払いをし「$hero殿、ただいま王様のお言葉を賜っている途中ですから」と注意を促す"),
            hero.talk("いやでも、マジでこの$smaph、もらっていいんすか？",
                "最新型ですよね？"),
            inside.look("赤いカーテンが敷かれ、その向こう側から声がする"),
            king.talk("おい、$arnold"),
            arnold.do("はい、と声を響かせ、カーテンの向こう側に"),
            arnold.do("王からぶつくさ愚痴られている"),
            arnold.do("表に出てきて、一旦$smaphを取り上げて、話が終わってから返すと言う"),
            hero.talk("わーったよ"),
            lina.do("その様に、愛らしい女性の声"),
            hero.do("気にするが、$arnoldに咳払いをされた"),
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
            w.eventStart("魔王退治"),
            w.comment("簡単に魔王によって世界が闇に包まれ、魔物が跋扈して、人々の生活が苦しくなっていることを言っておく"),
            king.talk("まさかあの英雄$dadの息子が選ばれるとは思うておらなんだが、",
                "これもまた何かの宿縁であろう",
                "これを使い、魔王を探し出し、お主にはなんとしても世界の平和を取り戻してもらいたい"),
            hero.do("$smaphを手に入れる"),
            hero.talk("これが、念願の$smaph……"),
            hero.think("みんなが憧れる$w_magicitemを手にして感動している"),
            king.talk("よろしく頼んだぞ、$w_Yよ！"),
            hero.do("$arnoldから城の兵士への支給品一式と、$umarkを貰う"),
            hero.talk("$me、がんばります！"),
            hero.think("$w_Yの称号がうれしくて顔がにやけて仕方ない"),
            camera=w.hero,
            stage=w.on_audienceroom_int,
            day=w.in_invite1, time=w.at_afternoon,
            )

def sc_aboutsmaph(w: World):
    hero = W(w.hero)
    king, lina, arnold = W(w.king), W(w.lina), W(w.arnold)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$smaphについての注意事項",
            hero.come("城のホールに戻ってくる"),
            inside.look("赤絨毯の階段を降りてきて"),
            inside.look("玄関の大ホールには、沢山の兵士や官吏（制服）が行き交っている"),
            hero.do("手にした$smaphを楽しそうにいじっている"),
            hero.talk("てか、これどうすればいいんだ？"),
            hero.do("画面を触って色々と動くが、元に戻ってしまい、何をしたらどうなるのか分からないでいる"),
            arnold.come(),
            arnold.talk("こちらの使い方ですが、すべて$smaphで見られるようになっております",
                "$smaphのご経験は？"),
            hero.talk("いや、初めてですよ",
                "てか、これって何でもできるんですよね？"),
            arnold.talk("何ができるかは$w_apli次第になります",
                "$meも詳しい技術は分かっておりませんが、",
                "技官に云わせればはるか太古、まだ人間が存在しなかったころの魔道の技術らしいです"),
            hero.talk("へー"),
            _.think("内心よくわからんと思っている"),
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
            stage=w.on_hall1_int,
            )

def sc_thisworld(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("この世界について",
            w.comment("ここで初めて外なので、外の空気感をよく見せておく"),
            hero.come("城から出てくる"),
            outside.look("城の表の大門",
                "立派な石造りの門構え",
                "門番の兵士が二人、槍を手にして立っている"),
            outside.look("空は雲が覆っていて薄暗い"),
            outside.look("空をくるくる旋回している飛行型の魔物"),
            outside.look("堀にかかった丸太で組まれた大きな橋"),
            hero.do("橋を渡る"),
            hero.do("門番ににこにこと挨拶をして、とりあえず教会に向かっていく"),
            stage=w.on_gate1,
            )

def sc_yushanow(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("勇者なう",
            w.comment("ここで最初につぶやいてから、教会でセーブしたように見えるが、教会セーブは関係ないので、このままでいいです"),
            hero.come("城下町に戻ってくる"),
            outside.look("中央広場には噴水を囲むようにして花壇があり、",
                "露店が連なる",
                "ただかつてほどの活気はない",
                "誰もが怯えるようにして、ほそぼそとやっていた"),
            outside.look("広場には大きな掲示板もあり、",
                "そこには増え続ける魔物に対処する為に兵士増員で募集がかけられている、",
                "その貼り紙などがある"),
            hero.do("$Sはじっと手元の$smaphを見つめている"),
            _.do("$w_manualを読んでいるが、わからない"),
            hero.do("$smaphに『勇者なう』と$w_tweetする"),
            hero.do("その$w_tweetはまたたく間に拡散され、画面には大量に「$w_Y？」の呟きが流れてくる"),
            hero.talk("ほー、これなんかすごいな！"),
            hero.think("こうして$w_Yは何をしたのかも分からないまま、増えていく数字を見て楽しんでいた"),
            stage=w.on_centralsquare,
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
