# -*- coding: utf-8 -*-
"""Episode: 2-1.Re:教会なう
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
def sc_re_church(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    clerc = W(w.clerc)
    malta = W(w.malta)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("再び教会にて",
            w.comment("目覚めたところの続き、ちょっとだけ前回振り返るやり取りを"),
            hero.be("教会で目覚める"),
            inside.look("見下ろす女神像、その裏側にはひび割れたステンドグラス",
                "木の板でツギハギされた壁、差し込む日差し",
                "同じ教会だとすぐ分かる"),
            w.eventPoint("人物紹介", "$clerc神父初登場"),
            clerc.be("神父がいる"),
            clerc.look("正装である濃紺の衣を身にまとっている"),
            w.comment("ここで簡単なこの世界の宗教と神様＝$w_godについて"),
            hero.talk("うわぁぁぁ！"),
            clerc.talk("何大きな声を出しているんですか、$hero"),
            hero.talk("え？　$clerc神父？"),
            inside.look("教会の内装",
                "ステンドグラスに女神像", "長椅子の最後尾には$malta婆さんが座っている"),
            hero.do("見慣れた光景だ",
                "しかしさっきいた代理の女性の姿はない"),
            hero.talk("あの、$yulaさんは？"),
            clerc.talk("誰でしょう", "信者さんの中には心当たりがありませんが"),
            hero.talk("いや、その女の人、旅行に行った神父の代理だって言ってたけど"),
            clerc.talk("旅行は中止になったんですよ", "恥ずかしい話だが先日腰をやってしまってね"),
            clerc.do("腰を擦る"),
            hero.think("何か奇妙だと思う"),
            hero.do("自分の体や持ち物を確かめる",
                "特に問題がない"),
            hero.look("＜簡単に格好とか＞",
                "膝までの布服を腰ベルトで留めている", "ズボンはところどころ破れをツギハギしている",
                "布の靴"),
            hero.do("$smaphを見ると、そこには打ち込んだ$w_tweetが消えていた",
                "まだ一言もない"),
            hero.think("$w_Yとバレてないことにほっとしている"),
            hero.do("日付を確認すると、まだ今日のままだ"),
            hero.talk("おかしいな"),
            clerc.talk("$hero君も$smaphを買ってもらったんだな",
                "最近若い子はみんな持っているよね", "随分と便利なんだろう？"),
            hero.talk("いや、まだ全然使い方よくわかんなくて"),
            clerc.talk("聞いた話ではそれを手にした者はどんな願いでも叶えられるとか、昔は云われておったな"),
            hero.do("ひょっとしたらこれの力で復活したのか、とか考え始める"),
            hero.think("落とした$smaphを拾ってあげたあの女の子が言っていたことを思い出す",
                "$smaphには持ち主を助ける不思議な力があるとか"),
            hero.talk("とにかくありがとうございます"),
            clerc.do("にこやかに答えるが、意味が分からない様子"),
            hero.go("外に出ていく"),
            camera=w.hero,
            stage=w.on_church1_int,
            day=w.in_reset1, time=w.at_afternoon,
            )

def sc_checkout(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    candy = W(w.candy)
    return w.scene("街を確認する",
            hero.come("教会を出て、街に戻る"),
            outside.look("街は変わらない様子",
                "市場にはわずかばかりの露店が並ぶ"),
            outside.look("石畳が敷かれたメインストリート"),
            outside.look("中央広場へと戻ってくる"),
            w.eventStart("迷子猫"),
            hero.do("$smaphを見ると、迷子猫を探していますと出る"),
            hero.talk("へえ、こういうのもあるのか",
                "可哀想になあ", "腹空かせてるだろうなあ"),
            w.eventPoint("人物紹介", "$candy初登場"),
            candy.come(),
            candy.look("小柄だが成人女性。金髪にそばかす"),
            candy.talk("あ、$heroさん。こんにちは"),
            candy.look("籠を手に抱えている",
                "そこは薬草を作る為の沢山の野草が入っている"),
            hero.talk("ああ、$candyさん"),
            hero.do("$herb屋の娘だ"),
            candy.talk("それ、$smaphじゃないですか。どうしたんですか？"),
            hero.talk("う、うん。ちょっと懸賞に当選してね"),
            candy.talk("いいなー", "$meもおこづかい貯めて買いますから、その時は相互してくださいね"),
            hero.do("意味がわからないが頷く"),
            hero.do("$smaphを見ると、色々な機能がある",
                "流れていく$w_tweetは平和だが、魔王の驚異に怯える声も"),
            hero.talk("そうだ。$meは$w_Yなんだから、がんばらないとな"),
            hero.do("口に出してしまってから慌てて周囲を見る",
                "特に誰も自分を気にしている様子がなく、安堵する"),
            stage=w.on_centralsquare,
            )

def sc_gotogatherally(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    bcat = W(w.blacat)
    return w.scene("仲間集めに向かう",
            hero.come("大通りを歩いている"),
            outside.look("どこも窓を閉めていて不穏",
                "舗装は石畳から地道に変わる",
                "やや貧民街になり、土埃も舞い始める"),
            hero.think("一体あれは何だったのかと考える"),
            hero.think("何故か街に大量の魔物が現れ、襲われた",
                "あの金色の魔物は$smaphで$w_tweetしたのを見たと言った"),
            hero.do("$smaphを見る",
                "あの時のようなフォロワー数はない"),
            w.eventPoint("最初のフォロワー", "$makoがフォローする（２）"),
            hero.do("と、通知音がしてフォロワーが増える",
                "$makoという名前だ"),
            hero.talk("これってまさかまた？"),
            bcat.come("黒猫が走り抜ける"),
            hero.do("じっと見ていたがそれ以上何か起こる気配はない"),
            sol.come("赤髪のよたよたと歩く大剣を背負った男が通り過ぎていく"),
            hero.do("見ればギルド本部も開いているようで、人が入っていく"),
            hero.do("他にも店は開いているし、変わった様子はないことにほっとするが"),
            hero.talk("とにかく家に戻ってみるか"),
            hero.go("まず家に向かって走った"),
            stage=w.on_street,
            )

def sc_nothingany(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    mam = W(w.mam)
    return w.scene("何もないよ",
            hero.come("自宅に戻ってくる"),
            outside.look("＜自宅の外観＞",
                "ところどころ板で補修してある",
                "どれも父親がやったものだ",
                "明かりは灯っていない"),
            hero.talk("$k_mam！"),
            mam.be(),
            hero.do("返事がないので、びくびくしながら覗く",
                "リビングには誰の姿もない"),
            hero.do("奥の台所を覗く"),
            inside.look("＜部屋の内装＞",
                "奥にそのままキッチンと食堂がある",
                "キッチンの前のテーブル"),
            mam.do("テーブルにふせっている"),
            mam.look("長い髪を括っている",
                "それがテーブルの上に伸びている",
                "服装は長い小豆色のワンピース",
                "いつもそればかりだ"),
            hero.talk("$k_mam？"),
            mam.talk("なによ、そんな大声出して"),
            hero.talk("あれ？　大丈夫なの？",
                "てか金色の魔物は？"),
            mam.talk("魔物が街に入ってくる訳ないじゃないの",
                "この街は$w_god様の加護によって守られているのよ？",
                "それよりもお城どうだった？"),
            hero.talk("あ、うん", "なんかすごかった"),
            mam.talk("あの人がいた頃は、よく呼び出されて通ってたものよ",
                "ほんと、どこほっつき歩いてんだか"),
            hero.do("父親の話になると暗い顔になる"),
            hero.talk("それより見てよ、これ"),
            hero.do("$smaphを見せる"),
            mam.talk("まあ、それどうしたの？"),
            hero.talk("なんか抽選で当たったんだってさ",
                "あ、そうそう", "$me、$w_Yに"),
            hero.do("言おうとしたところで通知音がする"),
            mam.talk("な、何だい？"),
            hero.talk("いや、なんか"),
            hero.do("王国のアカウントからフォローされた合図だった"),
            hero.talk("あ、そういや"),
            hero.do("思い出して旅の手引きを見る"),
            hero.talk("ちょっと出かけてくるわ"),
            mam.talk("どこに行くの？"),
            hero.talk("いや、王様から魔王退治頼まれちゃって"),
            mam.talk("何言ってんの？"),
            hero.talk("まー、そういうことだから", "とりあえずギルド行ってくる"),
            mam.talk("晩飯までに帰ってくるんだよ"),
            hero.go("出かける"),
            stage=w.on_herohome_int,
            )

def sc_mercenary(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("傭兵ギルド",
            hero.come("傭兵ギルドにやってくる"),
            outside.look("＜ギルド本部の建物＞",
                "赤レンガの堅牢な建物",
                "門をくぐり抜けるとそれぞれのギルド本部が入った棟が四つ建っている",
                "傭兵ギルドはそのうちの一つ"),
            inside.look("いかつい受付と、たむろしている男たち"),
            inside.look("その中に教会で見かけた彼女の姿があった"),
            hero.talk("あ！"),
            yula.be(),
            yula.look("＜一度目と同じ外見、服装＞",
                "大きなズタ袋を肩から下げている、金髪のすらりと長身の女性",
                "胸は大きい",
                "革製のベスト、青染のシャツ、ハーフパンツにストッキング、ブーツ"),
            yula.talk("何さ？"),
            hero.talk("あの、さっき教会にいた人ですよね？"),
            yula.do("怪訝な顔"),
            yula.talk("いや"),
            hero.talk("傭兵なんですか？"),
            yula.talk("$meは違うよ", "あんた傭兵探してんの？"),
            hero.talk("傭兵っていうか、仲間を","魔王退治の冒険に行くんです"),
            hero.do("みんなから笑われる"),
            yula.talk("やめときな", "魔王どころかそこらの$slimeにだって相手になりゃしないよ、あんたなんて"),
            hero.talk("でも倒さないと困るんです", "強い仲間さえいれば"),
            yula.talk("金持ってないんでしょ？　だったら酒場にでもいって、あんたの力になってくれそうな人探しな"),
            stage=w.on_guildhead_int,
            )

## episode
def ep_re_church(w: World):
    return w.episode("2-1.Re:教会なう",
            sc_re_church(w),
            sc_checkout(w),
            sc_gotogatherally(w),
            sc_nothingany(w),
            sc_mercenary(w),
            ## NOTE
            ##  - 目覚めると教会で、神父がいた
            ##  - 外に出て確認する。怪物はいなかった
            ##  - とりあえず夢だったと思い、仲間探しに向かう
            )
