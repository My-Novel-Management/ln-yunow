# -*- coding: utf-8 -*-
"""Episode: 10-4.エピローグ
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
def sc_vanish_mako(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    clerc = W(w.clerc)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("消えた$mako",
            hero.be("教会で目覚める"),
            clerc.be(),
            clerc.talk("どうしました？"),
            hero.talk("あの、$me……いや、魔王はいますか？"),
            clerc.do("首を傾げている"),
            hero.do("見ると他には誰もいない"),
            hero.talk("すみません"),
            hero.do("外に駆け出ていく"),
            camera=w.hero,
            )

def sc_ally(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("仲間たち",
            hero.come("外に出て"),
            sol.be(),
            yula.be(),
            hero.do("$solたちを見つける"),
            hero.talk("おい、なあ、$makoはどこだ？　いるんだろ？"),
            sol.talk("はあ？　$makoって誰だよ？"),
            yula.talk("知らないわよ、そんな子"),
            hero.do("駆け出す"),
            )

def sc_lookformako(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$makoを探す",
            hero.come("叫びながら$makoを探して走り回る"),
            hero.do("しかしどこを探しても彼女はいない", "返事もない"),
            hero.do("街の中は破壊される前に戻っていて、神官たちも無事だ",
                "武器屋も道具屋も、防具屋や薬草店も", "何より母親も無事だった"),
            )

def sc_myhome(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    mam, dad = W(w.mam), W(w.dad)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("家に戻ると父がいた",
            hero.come("自宅に駆け込んでくる"),
            hero.talk("$mako知ってるよね？　うちにきてたストーカーの子！"),
            hero.do("だが家には姿を消していたはずの父の姿が"),
            hero.talk("父さん！"),
            dad.be(),
            mam.be(),
            dad.talk("おう我が息子よ", "どうしたんだ、そんな顔をして"),
            hero.talk("いつ帰ったんだよ？"),
            mam.talk("何言ってるの、この子ったら", "ずっと家にいたじゃない",
                "今日もお城に剣の稽古をつけに出てたのよ"),
            hero.talk("そんな", "それじゃあ"),
            hero.do("一体どうなっているのか", "父は魔王を退治しに出たまま消息不明になったはず"),
            hero.talk("魔王はどうしたの？"),
            dad.talk("魔王？　何の話だ？"),
            hero.explain("魔王がいないことになっていた"),
            )

def sc_no_maou(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    aida, gans = W(w.aida), W(w.gans)
    bcat = W(w.blacat)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("魔王のいない世界",
            hero.be("酒場で子ども用の$bottlejuiceを飲んでいる"),
            sol.be(),
            yula.be(),
            aida.be(),
            gans.be(),
            hero.talk("何だっていうんだよ！"),
            sol.talk("$k_heroさ、またゲームの中と混同してたってオチじゃねえのか？"),
            hero.talk("何言ってんだよ！　実際にいたんだよ",
                "$makoが魔王で、一緒に$majuを倒したじゃないか"),
            yula.talk("調べてみてるけどその$makoって女の子のことも$majuのことも、全然乗ってないわよ？"),
            hero.do("確かに見つからなかった",
                "まるで全てが綺麗に消されたみたいになっていた"),
            stage=w.on_townbar1_int,
            )

def sc_message(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    bcat = W(w.blacat)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$makoのメッセージ",
            hero.come("一人とぼとぼ帰る"),
            bcat.come("彼女には決して懐こうとしなかった黒猫が駆け出てくる"),
            hero.talk("あ、クロ"),
            hero.do("よく見ると、彼女が買って$Sがつけてやった首輪をつけていた"),
            hero.talk("やっぱり$makoはいたんだ！"),
            stage=w.on_street,
            )

def sc_newadventure(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    bcat = W(w.blacat)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("新たな旅に出発",
            hero.be(),
            sol.be(),
            yula.be(),
            bcat.be(),
            hero.explain("翌日、$Sは$solたちに声をかけ、どこかに消えてしまった$makoを探す為に旅立つ計画を話す"),
            hero.talk("待ってろよ！　魔王！"),
            hero.explain("こうして勇者たちは魔王退治ではなく魔王探しの旅に出ることになった"),
            )

## episode
def ep_epilogue(w: World):
    return w.episode("10-4.エピローグ",
            sc_vanish_mako(w),
            sc_ally(w),
            sc_lookformako(w),
            sc_myhome(w),
            sc_no_maou(w),
            sc_message(w),
            sc_newadventure(w),
            ## NOTE
            ##  - 目覚めると魔子が消えていた
            ##  - 城下町を探すが魔子はどこにもいなくなっていた
            ##  - 魔子を探すための冒険の旅に出ることにした
            )
