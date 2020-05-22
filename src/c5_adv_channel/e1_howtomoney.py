# -*- coding: utf-8 -*-
"""Episode: 5-1.金を稼ぐなう
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
def sc_nomore_mamazon(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    clerc = W(w.clerc)
    malta = W(w.malta)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$w_amazonは懲り懲り",
            hero.be("教会で目覚める$S"),
            inside.look("見慣れた女神像、教会の内装"),
            malta.be("一番うしろにいる"),
            w.comment("ここ、内装が毎回少しずつ変化している方が面白い",
                "完全に修正できる訳じゃないことの証明"),
            malta.look("着ている服が少し豪華になっている"),
            clerc.be(),
            clerc.talk("どうかしましたか？"),
            hero.talk("あ、いえ",
                "失礼しました"),
            hero.go("また戻されたのだと分かり、一旦家に戻る"),
            camera=w.hero,
            stage=w.on_church1,
            day=w.in_reset3, time=w.at_afternoon,
            )

def sc_re_ally(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    mam = W(w.mam)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("仲間と合流",
            hero.come("家に戻ってくる"),
            sol.be("玄関の前で座り込んでいる$S"),
            outside.look("木造二階建て、明かりが灯っている",
                "その明かりで影が伸ばされている"),
            hero.do("家で$solが待っていた"),
            sol.talk("よう"),
            hero.do("もう説明すらなく、待っている$sol"),
            hero.go("家に入っていく"),
            stage=w.on_herohome,
            time=w.at_night,
            )

def sc_mam_and_mako(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    mam = W(w.mam)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("母親と$mako",
            hero.come("入ってくる"),
            sol.come(),
            mako.be(),
            mam.be(),
            inside.look("家の中で$makoと母親が二人で楽しそうにお茶を飲みながら談笑"),
            mako.talk("あ、おかえりなさい、$k_hero"),
            mam.talk("おかえり、$k_hero"),
            hero.talk("なんで二人して仲良くしてんの？"),
            mam.talk("この$k_makoがね"),
            mam.explain("家にやってきて仲良くなった経緯を説明してくれた"),
            w.br(),
            mako.talk("という訳なんですよ"),
            hero.talk("わかった", "とりあえず部屋に"),
            mako.talk("いいんですかぁ！"),
            hero.talk("妙な勘違いしないでくれ……"),
            stage=w.on_herohome_int,
            time=w.at_night,
            )

def sc_planformoney(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("金策",
            hero.come("お茶を手に、部屋に入ってくる$S"),
            mako.be(),
            sol.be(),
            hero.do("二人とも部屋でくつろいでいる"),
            hero.talk("これ、持ってけって"),
            mako.talk("$meが$w_amazonで注文したやつですよ",
                "美味しいんで、是非おすそ分けって思って"),
            hero.do("$macaronというお菓子らしい",
                "小さい月のような形のお菓子が並んでいる"),
            hero.do("みんなでそれを食べながら旅の準備を騙る"),
            mako.talk("だから$k_hero、買い物なら$w_amazonで"),
            hero.talk("いや、いい"),
            hero.think("大魔王の悪夢を思い出してすぐ否定する"),
            mako.talk("え？"),
            hero.talk("それは今はいい",
                "準備は何とか自分たちでするよ"),
            mako.do("なんで？　という表情"),
            sol.talk("やっぱ地道に働くしかねえと思うぜ？"),
            hero.talk("$meも働いて金貯めようと思うんだ",
                "$sol、仕事を紹介してくれないかな？"),
            sol.talk("ああ、いいぜ"),
            stage=w.on_heroroom_int,
            )

def sc_hardwork(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    cedo = W(w.cedoros)
    return w.scene("肉体労働",
            hero.come("翌日、$solについて作業現場にやってくる"),
            outside.look("西側の砦の改修工事",
                "煉瓦を積み上げて三メートルほどの砦に改修する"),
            cedo.be("屈強な男が現場を仕切っている"),
            cedo.look("上半身むきむきの男性"),
            outside.look("むさい男たちが黙々と運んだり、積み上げたりの作業をしている"),
            sol.talk("今日の現場の$cedorosさんだ"),
            hero.talk("え？　これをやるの？"),
            sol.talk("そうだよ",
                "ここに運んだ煉瓦を言われた通りに積み上げていくんだ"),
            hero.explain("それは補修作業だった",
                "まだ街のあちこちが魔族の襲来を受けて以来、ずっと補修が続いている"),
            w.br(),
            hero.do("時間がたち、疲れて座り込んでしまっている$S"),
            sol.talk("おい、何休んでるんだよ？"),
            hero.talk("なあ、これ一日やっていくら稼げるんだ？"),
            hero.do("金額をきいて驚く"),
            sol.talk("十日も働けば一月くらい旅出る資金集まるだろ",
                "地味に稼ぐっていうのはこういうことだ"),
            hero.talk("いや、もっと楽して稼ごう"),
            stage=w.on_constfield,
            day=w.in_working1, time=w.at_midmorning,
            )

def sc_findjob(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    mashu = W(w.mashu)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("職探し",
            hero.come(),
            sol.come(),
            mako.come(),
            hero.explain("翌日、三人揃ってギルド本部にやってきた"),
            inside.look("ギルド本部の建物",
                "そこの一つに人の列ができている",
                "職業案内所だ"),
            hero.do("$meは肉体労働を除いた何か仕事を探そうと職安にやってくる"),
            mashu.be(),
            mashu.look("事務員の一人",
                "頭がはげていて、気難しそうな顔",
                "首から眼鏡代わりの拡大鏡を下げている"),
            mashu.talk("で、どんな職業探してるの？"),
            hero.talk("えー、楽に稼げて、さっさと冒険に旅立てるような"),
            mashu.talk("ない",
                "というか、あんたまだ若いでしょ？",
                "金を稼ぐとかどうこうじゃなくて、何が自分に合っているか、",
                "色々と見聞を深めるのが先だと思いますがね"),
            hero.talk("なりたいのは$w_Y"),
            mashu.talk("は？　$w_Yになりたいとか言うのは初めて聞いたわ",
                "でもありゃなるもんじゃなくてな、",
                "称号みたいなもんだから、それこそ業績を上げて王様にでも認めてもらって、",
                "やっとなれるみたいな",
                "冒険者になりたいなら、それこそこっちじゃなくて、ギルドに張り出されているクエストを探してみたらいいんじゃないかね？"),
            hero.talk("てっとりばやく稼げますか？"),
            mashu.talk("（じっと見て）無理だな、あんたらじゃ"),
            hero.talk("じゃあ、何か簡単に稼げそうなものって"),
            mashu.talk("地道に働く以外にない"),
            stage=w.on_guildhead_int,
            day=w.in_working2, time=w.at_midmorning,
            )

## episode
def ep_howto_money(w: World):
    return w.episode("5-1.真面目に金を稼ぐなう",
            sc_nomore_mamazon(w),
            sc_re_ally(w),
            sc_mam_and_mako(w),
            sc_planformoney(w),
            sc_hardwork(w),
            sc_findjob(w),
            ## NOTE
            ##  - 金を稼がなければならないと気づき、仕事を探す
            ##  - 魔子に呆れられながらも肉体労働で汗を流す
            ##  - 真面目に稼いでいたら魔王退治に出かけられないことが判明する
            )
