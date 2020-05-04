# -*- coding: utf-8 -*-
"""Episode: 7-1.Re:ゴブリン退治なう
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
def sc_retry(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    return w.scene("再度$goblin退治に",
            hero.be("教会で目覚める"),
            hero.talk("またか"),
            hero.do("何か話しかけようとする神官を放って、外に出ていく"),
            hero.do("待ち構えていた$solたちと合流し、",
                "そのまま出かけようとする彼らに「ちょっと待って」と言う"),
            sol.talk("何だよ$k_hero、怖気づいたか？"),
            hero.talk("ち、違うよ",
                "ただ、もう少し準備をした方がいいってことに気がついたんだ"),
            hero.do("$Sは$solたちに$goblinの巣について、前に得た情報を知らせる"),
            sol.talk("それって確かな情報なのかよ？"),
            hero.talk("一応、ほら"),
            hero.do("あの時は信じていなかった自分のフォロワーの$maniaさんの書き込みを見せる",
                "そこには$goblin情報が網羅されていた"),
            mako.talk("なんかこの人、", "一人$w_wikiみたい"),
            hero.do("相手が$smaphを持っていることに対してどう対策すればいいか、という相談を始めるが、"),
            sol.talk("まあ所詮は$goblinだ", "沢山で一気にこられなきゃ何とかできるべ"),
            mako.talk("だから$meの魔法で全焼させますって"),
            hero.talk("いや、今回は火は絶対に使わないでくれ"),
            mako.do("何故？　という顔"),
            hero.talk("とにかく火はまずい", "うまく忍び込めれば"),
            camera=w.hero,
            stage=w.on_castletown1,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_bignest(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    return w.scene("巨大な要塞",
            hero.come("三人で地図をあてにしてやってくる"),
            sol.come(),
            mako.come(),
            sol.talk("なんだよ、これは！"),
            hero.do("見れば橋がかかっていたはずの場所に巨大な石の建造物が立っていた"),
            hero.talk("嘘だよね？", "これなの？"),
            hero.do("クエストの地図を確かめるが、場所は間違いない"),
            hero.talk("えっと、帰るか、一旦"),
            sol.talk("そ、そうだな"),
            mako.talk("あの、あれ見てください"),
            hero.do("$makoに指摘された方を見ると、一人の女シーフが潜入していくのが見えた"),
            mako.talk("先にクエスト達成されちゃったらお金にならないんですよね？"),
            sol.talk("そ、それはまずいな", "どうするよ$k_hero"),
            hero.talk("あの人、一人で大丈夫なのかな？"),
            mako.talk("どうでしょうか", "もし情報が確かなら$smaphで連携されて囲まれると強い戦士でもかなり苦戦しますし"),
            hero.talk("助けに行こう"),
            )

def sc_thief(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    return w.scene("潜入するシーフ",
            w.symbol("※"),
            yula.come("ひっそりと要塞に近づく"),
            yula.think("ここが$goblinの巣かと思いながら周囲を確認する"),
            _.do("この中に周辺の村から奪った宝物がごっそり集められるという情報を手に入れてやってきていた"),
            yula.do("見張りの一匹を倒して、こっそり侵入する"),
            yula.do("女盗賊だった"),
            )

## episode
def ep_retry(w: World):
    return w.episode("7-1.Re:ゴブリン退治なう",
            sc_retry(w),
            sc_bignest(w),
            sc_thief(w),
            ## NOTE
            ##  - 再び教会に戻った勇者は仲間と共に再度、ゴブリン退治に赴く
            ##  - しかしやってきたゴブリンの巣は見るも巨大な城塞になっていた
            ##  - 巣に潜入するシーフの姿を見て、その後をつけて裏口から入り込む
            )
