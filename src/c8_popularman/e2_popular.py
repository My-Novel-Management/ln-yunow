# -*- coding: utf-8 -*-
"""Episode: 8-2.人気者なう
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
def sc_broadcast(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    kiyoe = W(w.kiyoe)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("番組放送",
            stage=w.on_brostation_ext,
            day=w.in_interview1, time=w.at_midmorning,
            )

def sc_broadcast2(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    kiyoe = W(w.kiyoe)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("番組放送",
            hero.come("放送局に一人でやってくる"),
            inside.look("綺麗に内装がされている",
                "石造りの貴族の別荘がレンタルにされているもの"),
            hero.do("受付の女性から入館証をもらって、緊張気味に入っていく"),
            hero.talk("へー、ここで番組作ってんのか"),
            inside.look("きっちりと組まれた石ブロックの通路を進む"),
            kiyoe.talk("お待ちしてました",
                "こちらに座ってもらって、いろいろとインタビューさせてもらいます",
                "撮影はあちらの$cameraでとったものを、編集して$w_webに流します"),
            hero.talk("は、はい"),
            hero.do("緊張しながらきょろきょろと"),
            inside.look("たくさんのスタッフと、機材"),
            inside.look("歩いていく中にアイドルの$yuiを見つけて"),
            hero.talk("おー！　$yuiちゃんじゃないか！"),
            hero.do("興奮している$S"),
            hero.think("$solたちも来ればよかったのに、と思っている"),
            kiyoe.talk("じゃあ、段取りを説明していきますね"),
            hero.do("こうして番組の準備が始まった"),
            stage=w.on_brostation_int,
            )

def sc_popularman(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    kiyoe = W(w.kiyoe)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("人気者に",
            hero.be(),
            sol.be(),
            mako.be(),
            hero.do("配信を何度も繰り返して見ている$S"),
            sol.talk("もう見たろ？", "いい加減にしとけよ"),
            hero.talk("いいだろ、何度見たってさ",
                "それよりここさ、もっと面白く喋れたよね？"),
            mako.talk("そんなことより、ほんとに今度$yuiとかっていう小娘と共演するんですか？"),
            mako.do("その話を聞きつけ、嫉妬している$S"),
            hero.do("寛いでいたらそこに来客"),
            kiyoe.come(),
            kiyoe.talk("どうも、勇者さん"),
            hero.talk("え？"),
            hero.do("誰にも言ってないのに、何故バレたと固まる"),
            kiyoe.talk("ああ、すみません",
                "放送後に視聴者のみなさんが$heroさんのことを$w_Yと呼ばれてるんですよ",
                "ほら"),
            kiyoe.do("自分の$smaphを見せながら教える",
                "そこには確かに沢山の$w_Yコメントがある"),
            kiyoe.talk("そこで相談なんですが、またご出演願えないかと思いまして"),
            hero.talk("あ、いいすよ"),
            sol.talk("即答かよ"),
            kiyoe.talk("今度の企画はこちらなんですが"),
            hero.do("見せてきたのは、世界の果てまでモンスター退治だった"),
            hero.talk("え、これってどういうことですか？"),
            kiyoe.talk("やはりみなさんが期待されてるのは、$w_Yさんによるモンスター退治、はては魔王討伐みたいで、",
                "うちとしましてはそれを密着取材させていただくという形で",
                "どうでしょうか"),
            sol.talk("おいおい", "無理だから断れって"),
            hero.talk("ああ、じゃあ、お願いします"),
            sol.talk("なんでだよ！"),
            hero.do("こうして近所まででかけては弱いモンスターを退治するという企画がスタートした"),
            stage=w.on_heroroom_int,
            day=w.in_afterbroadcast, time=w.at_afternoon,
            )

def sc_invitation(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    arnold = W(w.arnold)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("招待状",
            hero.come("家に戻ってきて、荒い息"),
            hero.talk("なんでクエストでもないのにモンスター退治してるんだろう"),
            sol.come(),
            mako.be(),
            sol.talk("$k_heroが自分で蒔いた種だろ！",
                "お陰でこっちはひどい目だ"),
            mako.talk("おかえりなさいませ！"),
            arnold.come("そこに城から使いがやってくる"),
            arnold.look("上質な仕立ての黒を貴重にした服"),
            arnold.talk("あなたが$heroさんですね？"),
            hero.talk("誰？"),
            arnold.talk("$meは首相秘書官の$Sと申します",
                "この度、お城で開かれるパーティにあなた方をお招きしたいと王が言われるので、",
                "それを伝えに参りました",
                "参加していただけますね？"),
            hero.do("城からの招待状を見せられた"),
            stage=w.on_herohome_int,
            day=w.in_request2, time=w.at_afternoon,
            )

## episode
def ep_popular(w: World):
    return w.episode("8-2.人気者なう",
            sc_broadcast(w),
            sc_broadcast2(w),
            sc_popularman(w),
            sc_invitation(w),
            ## NOTE
            ##  - 番組に出演して緊張の勇者たち。何故か魔子は参加しなかっ
            ##  - 更に人気になり、色々な人から声が掛かるようになり、金が稼げる
            ##  - 遂には王宮からパーティへの招待状が届いた
            )
