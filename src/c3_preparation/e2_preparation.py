# -*- coding: utf-8 -*-
"""Episode: 3-2.買い物なう
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
def sc_visitmarcket(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    candy, doyle = W(w.candy), W(w.doyle)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("市場を見て回る",
            hero.come(),
            sol.come(),
            mako.come(),
            hero.do("翌朝、三人で市場へとやってきた"),
            outside.look("市場の情景",
                "城下町の中央部の広場に露店がたくさん出て賑わっている",
                "ただ以前に比べて半分の数になり、寂しい"),
            outside.look("広場の中央には噴水、掲示板があり、そこには国王からの様々なおふれが書かれている"),
            outside.look("綺麗に石畳が整備されている",
                "人通りは少ないものの、それなりに活気がある"),
            hero.do("昔はもっと人が多くて賑やかだったと騙る"),
            hero.look("昨日と同じ服装",
                "布のブーツ、布の上着"),
            sol.look("下着だけ変えた",
                "背が高く、ぼさぼさの赤髪が目立つ",
                "大きな剣も目立つ"),
            mako.look("黒い地味なマントの衣装",
                "でも帽子のラインはピンクで、持ってきた鞄もピンク",
                "ソックスもミントとピンクの縞模様"),
            hero.talk("魔王が現れてから、色々と物が入ってこなくなったりして、困ってるみたいなんだ"),
            sol.talk("これでもまだマシな方だ",
                "一度立ち寄った街なんか、誰も家に閉じこもって出てこないんだよ",
                "なんでも一度魔物が大量に街に入ってきて沢山死者が出て、",
                "それ以来買い物すら配達頼りだって"),
            mako.do("花屋を見て、それを買ってとねだる"),
            hero.talk("花なんて冒険に必要ないだろう？"),
            mako.talk("でも綺麗ですよ？"),
            hero.talk("そりゃ、昔は花の街って言われてたくらいだからね",
                "$meもよく……"),
            w.eventPoint("$heroの過去", "小さい頃に花畑で誰かと会った記憶"),
            mako.talk("どうかしました？"),
            hero.talk("いや、なんでも"),
            hero.do("見て歩くが、露店には欲しいものはあまりない"),
            hero.do("それでも食い物を買ってやる$S"),
            mako.talk("ありがとうございます"),
            hero.talk("$hotdogは庶民の食い物だからな！"),
            stage=w.on_centralsquare,
            day=w.in_shopping1, time=w.at_midmorning,
            )

def sc_visitmarcket_herbshop(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    candy, doyle = W(w.candy), W(w.doyle)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("薬草屋にて",
            hero.do("薬草屋に立ち寄る"),
            w.eventPoint("人物紹介", "$candy紹介"),
            w.eventPoint("人物紹介", "$doyle紹介"),
            candy.be(),
            doyle.be(),
            inside.look("木の棚がたくさん並ぶ店内",
                "そこに皿に乗った薬草が沢山ある",
                "店内は様々な匂いが充満している"),
            candy.look("エプロン姿",
                "小柄でそばかす目立つ", "低い鼻"),
            doyle.look("中肉中背ずんぐりむっくり",
                "太い腕と右目の大きな傷",
                "昔は船乗りだったとか",
                "口元は布で覆っている"),
            hero.do("薬草を見ている"),
            doyle.do("店の奥で薬草をせんじながら、娘が相手するのをあまりよく思ってない"),
            candy.talk("へー！　$heroさんたち冒険に出るんですか！"),
            candy.look("$makoと同じくらいの背丈だが、二十歳を超えていて合法"),
            hero.talk("そうなんだよ", "$herbならここのが一番ってことで"),
            candy.talk("そうね。うちのはこの国一って言ってもいいくらいだと思う",
                "ね、お父さん"),
            doyle.talk("買うのか買わねえのか、はっきりしろ"),
            doyle.do("睨みつける$S"),
            hero.talk("は、はい。買いますって"),
            hero.talk("$doyleさんいつも怖いんだよ"),
            sol.talk("そういえば$k_makoは？"),
            hero.talk("なんか好きなもの見てくるって"),
            hero.do("$candyと親しげに話している$S"),
            stage=w.on_herbshop1,
            )

def sc_expensive(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("みんな高額",
            hero.come("$solと二人で装備品などを見に武器屋を訪れていた"),
            sol.come(),
            inside.look("＜それぞれの店の簡単な内装や置かれている商品＞"),
            hero.do("その後、装備品やキャンプ用品を見て回るが"),
            hero.talk("なんだこの値段……"),
            sol.talk("いいのはこんくらいすんのよ",
                "まあ$meらの持ち合わせだとこっちだな"),
            sol.do("$Sが見ていたのは一番しょぼい寝袋だ",
                "ただの布を縫い合わせただけに見える"),
            hero.talk("これで寒さ防げるの？"),
            sol.talk("お前な、何もない野原で寝ると思ってたのか？",
                "洞窟とか、そういう場所を探して、地べたに寝なくていいように、",
                "これを使うだけだぞ？"),
            hero.talk("え？"),
            sol.talk("野宿の何もしらないみたいだから、冒険に出たら$meがみっちり教え込んでやるよ",
                "如何にこの世界が人間の暮らす環境になっていないか",
                "如何に屋根がある、壁があるってことが幸せかな"),
            hero.do("震え上がる$S"),
            stage=w.on_weaponshop1,
            )

def sc_pickedmoney(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    mam = W(w.mam)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("金を失った",
            hero.come(),
            sol.come(),
            mako.be(),
            mam.be(),
            hero.do("結局散財して帰ってきた$Sたち"),
            mako.talk("あ、おかえりなさいませ", "どうでしたか？"),
            mako.do("$mamと一緒にくつろいでいる"),
            mam.talk("おかえり、$k_hero"),
            hero.talk("なに二人で仲良くしてんの？"),
            mako.talk("せっかくなのでベッドメイクしておきました"),
            inside.look("部屋を覗くと様子が一変している"),
            hero.talk("これどうしたの？"),
            mako.talk("だから$meが色々と飾っておきました",
                "いいでしょう？"),
            inside.look("花柄の壁紙とかすごいメルヘンチックになっている"),
            hero.talk("これも？"),
            hero.do("サイドテーブルの上のドクロの置物を見て"),
            mako.talk("それは$meの趣味です", "あまりこういうの置かないようにしたんですけど"),
            hero.talk("いや、そういう問題じゃなくて"),
            mako.talk("だって魔王退治したら結婚してここが新居になる訳でしょう？",
                "ね"),
            inside.look("狭い部屋には不釣り合いなキングサイズのダブルベッド"),
            hero.talk("いや、あの、あれはね"),
            sol.talk("まあいいじゃねえか",
                "一度は口から出した言葉だ、男なら引っ込めないだろう？"),
            hero.talk("$solまで！"),
            hero.do("なんとか準備を整えた$Sたちは、明日の朝ここを発つことに決めて、わかれた"),
            stage=w.on_herohome_int,
            time=w.at_afternoon,
            )

def sc_thinkadventure(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    mam = W(w.mam)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("冒険に思いを馳せる",
            hero.be("自室にいる"),
            hero.do("ベッドに寝転び考えていた"),
            hero.think("夢にまで見た冒険の旅"),
            hero.talk("しかしこれを手に入れてから人生変わったよなあ"),
            hero.do("$smaphを見ていると、何かの宣伝が流れてくる"),
            hero.talk("ん？　$w_game？"),
            stage=w.on_heroroom_int,
            time=w.at_night,
            )

## episode
def ep_shopping(w: World):
    return w.episode("3-2.買い物なう",
            sc_visitmarcket(w),
            sc_visitmarcket_herbshop(w),
            sc_expensive(w),
            sc_pickedmoney(w),
            sc_thinkadventure(w),
            ## NOTE
            ##  - 市場にやってくる
            ##  - 色々と見て回るがみんな高い
            ##  - 財布をだましとられ、大事な金を失う
            )
