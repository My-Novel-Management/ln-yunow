# -*- coding: utf-8 -*-
"""Episode: 8-1.バズる
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
def sc_nextquest(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    rucca = W(w.rucca)
    return w.scene("次のクエストを探せ",
            hero.be(),
            mako.be(),
            sol.be(),
            yula.be(),
            rucca.be(),
            hero.explain("四人でギルド本部に集まり、次のクエストの相談をしていた"),
            inside.look("ギルドの受付には結構人が並んでいる",
                "それをさばいている$rucca"),
            sol.talk("てか、なんでお前いるんだよ？"),
            yula.talk("お前って何さ",
                "$meには$yulaって名前があるのよ"),
            sol.talk("名前のことじゃなくてだな、なんで$meたちと一緒にいるんだ？"),
            hero.talk("折角知り合ったからみんなで一緒にやった方が楽しいかなって"),
            yula.talk("え？　そんなつもりないわよ",
                "あんたら$meに貸しがあるんだから、ちゃんとお金返してよね"),
            yula.do("$Sは$smaphを見せて、そこにメモした使用料、助けたお金など"),
            sol.talk("お前は鬼か"),
            yula.talk("きっちりしてるって言ってよね"),
            mako.talk("それより、どうするんですか"),
            mako.do("何故か機嫌悪そう"),
            rucca.do("咳払いをして、じっと見てる"),
            sol.talk("もうモンスターは懲り懲りだぜ",
                "それよりやっぱ肉体労働だろ？", "この護岸改修工事とかどうだ？"),
            yula.talk("何が悲しくてクエスト板見て肉体労働しなきゃならないのよ",
                "探すならもっと楽して稼げるやつに決まってるでしょ"),
            hero.talk("山に巣食うお化けカラスの群れ退治か"),
            mako.talk("$hero様はまたモンスター退治がしたいんですか？",
                "また死にそうになったらどうするつもりなんです"),
            hero.talk("ああ、それは何とかなるからいいんだ",
                "せっかく$Yなんだからもっと人助けっぽいことしないとな",
                "ついでに金を稼いで、魔王退治の旅費にする",
                "これぞ$Yイズムじゃね？"),
            mako.do("呆れる$S"),
            camera=w.hero,
            stage=w.on_guildhead_int,
            day=w.in_nextgob, time=w.at_midmorning,
            )

def sc_gobackhome(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    mam = W(w.mam)
    return w.scene("自宅に戻って",
            hero.come(),
            sol.come(),
            mako.come(),
            yula.come(),
            mam.be(),
            hero.explain("一通り見たあとで、一旦自宅に戻ってくる"),
            mam.talk("$k_heroおかえ……り？"),
            mam.do("$yulaを見て驚く母"),
            yula.talk("どうも。おじゃまします"),
            mam.talk("あ、はい"),
            mam.talk("ねえ、どうしたのよ", "あんな大人な女性連れてくる子じゃなかったでしょ"),
            hero.talk("な、仲間だよ", "別に恋人とかそ、そんなじゃないから！"),
            stage=w.on_herohome_int,
            )

def sc_goblinvideo(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("ゴブリン退治動画",
            hero.come(),
            sol.come(),
            mako.come(),
            yula.come(),
            hero.do("全くいいクエストなかったと思ってベッドに倒れ込む"),
            sol.talk("なあ、これちょっと見てくれよ"),
            hero.talk("何勝手にひとの$smaph触ってんだよ"),
            sol.talk("かてーこと言うなよ", "それよりこれ",
                "一応この前の動画、ツテに頼んで編集してもらったんだ",
                "割とよくないか？"),
            sol.do("意外と$w_dougaにはまっている$S"),
            hero.do("それは二度目のゴブリン退治のものだった",
                "要塞を$makoの爆撃で破壊して、ダムになっていた建物が崩れ、",
                "下流域が大災害にあったあれだ"),
            hero.talk("なんでいつも勝手にやってるんだ、$solは"),
            sol.talk("まあまあ", "それよりこれ、見てくれよ"),
            hero.do("そこに表示されている数字がどんどん増えていく"),
            hero.talk("何だ？"),
            sol.talk("これって数字増えるほど儲かるんじゃなかったっけ？"),
            hero.do("確かにそう聞いている"),
            hero.talk("じゃあこれって……"),
            yula.come(),
            yula.talk("ね、あんたらちょっと話題になってるわよ", "知ってる？"),
            yula.do("情報の早い彼女は既にゴブリン退治実況動画を知っていた"),
            hero.talk("いや、今みたらすごいことになってて"),
            hero.do("知らない間にフォロワーが増えて、コメントもがんがん寄せられる"),
            hero.talk("これ、どうすればいいの？"),
            yula.talk("よっぽど受けがよかっただけで、そんなに何度もモンスター退治クエストなんてやってられないでしょ",
                "見る方もただ倒していくだけなんてつまらないし、かといってアクシデントが毎回起こる？",
                "それこそやらせを疑われるわよ",
                "こういうのは手を出さない方がいいって……言ってるそばから"),
            hero.do("$solと二人で相談している"),
            hero.talk("とりあえず$slimeを退治に向かう二人"),
            stage=w.on_heroroom_int,
            time=w.at_afternoon,
            )

def sc_less_popular(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("動画の視聴数増えないな",
            hero.be(),
            sol.come(),
            sol.talk("どんな調子だ？"),
            hero.do("二人で$slimeをいじめて捕獲した実況動画を上げてみたが"),
            hero.talk("駄目だな、これ"),
            sol.talk("$meなんか装備もってかれたんだぞ！",
                "あんだけ苦労してなんでたったの十三なんだよ！"),
            hero.do("$smaphの画面にその様子が出ている"),
            yula.talk("だから言ったでしょ？", "そう簡単に増えないんだって",
                "たまたまアレが面白かっただけで、あんたらが面白い訳じゃないの",
                "これに懲りたらもう二度とあれで稼ごうとか思わないことね"),
            mako.come(),
            mako.talk("$hero様、次はどうしますか？",
                "例の動画で多少収入あったでしょ？", "それで準備して冒険に出ちゃいます？"),
            mako.do("$Sは早く一緒に旅をしたくて仕方ないみたいだ"),
            hero.talk("そうだな",
                "このままだとここで一生終わりそうだし、そろそろ"),
            day=w.in_nextslime, time=w.at_midmorning,
            )

def sc_requestappear(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    kiyoe = W(w.kiyoe)
    mam = W(w.mam)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("出演依頼",
            hero.be(),
            mam.be(),
            hero.explain("更に十日ほど、色々とやってみたが、何もバズることはなかった"),
            hero.talk("あー、もう無理だー", "このままだと冒険に出られないまま終わる"),
            hero.do("そこに、母親から来客が告げられる"),
            hero.talk("はいはい"),
            kiyoe.come(),
            kiyoe.talk("あのー、あなたが今話題の勇者さん、ですよね？"),
            kiyoe.look("ショートヘアの女性"),
            kiyoe.do("涼し気な笑みだが、どこか単純ではない感情が含まれていた"),
            stage=w.on_herohome_int,
            day=w.in_request1, time=w.at_midmorning,
            )

## episode
def ep_buzz(w: World):
    return w.episode("8-1.バズる",
            sc_nextquest(w),
            sc_gobackhome(w),
            sc_goblinvideo(w),
            sc_less_popular(w),
            sc_requestappear(w),
            ## NOTE
            ##  - ゴブリン退治して多少稼いだ金はガチャに消え、次のクエストを探していた
            ##  - 知らない間にゴブリン退治動画の視聴者数が増えていて、人気者に
            ##  - 城下町放送局から出演依頼がくる
            )
