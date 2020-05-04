# -*- coding: utf-8 -*-
"""Episode: 7-3.今度こそゴブリン退治なう
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
def sc_yula(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    return w.scene("$yulaを仲間に誘う",
            yula.talk("あんたら何してんのさ？"),
            hero.talk("$yulaさんは何してるんですか？"),
            yula.talk("$meはね……"),
            yula.do("背中に背負った袋"),
            sol.talk("こそ泥だよ"),
            sol.do("あまりいい顔をしていない"),
            yula.talk("こそ泥じゃないわよ",
                "やつらが奪ったものを取り返してあげてるだけじゃない？"),
            sol.talk("そこからいくらかすめ取るんだ？"),
            hero.do("$solと$yulaはいがみ合っている"),
            hero.think("$makoに話しかけようとして気づく"),
            hero.talk("あれ？　$makoがいない"),
            sol.talk("ほんとだな？"),
            yula.talk("あんたらと一緒にいた子って、たぶんこれだね"),
            yula.do("$Sは$smaphで位置情報を見せると、どんどん離れていっている"),
            yula.talk("さらわれたか"),
            hero.talk("え？"),
            )

def sc_rescuemako(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$makoを救出へ",
            hero.do("$yulaを仲間にして、奥へと進んでいく"),
            yula.talk("$meは危なくなったらすぐ逃げるから", "いい？"),
            sol.talk("逃げようってときには既に囲まれてるぞ、どうせ"),
            yula.talk("一人なら何とでも逃げようはあるわよ",
                "あんたらは自分で自分の命守りなさいってこと"),
            hero.talk("$yulaさんて強いんですね！"),
            yula.talk("死ぬようなへまな選択はしないってだけ",
                "この世は生き延びたやつが強いのよ",
                "自分の強さを誇ろうなんてのは馬鹿のすることだから"),
            sol.talk("なんで$meを見て言うんだ？"),
            yula.talk("脳筋っぽいなと思っただけ"),
            sol.talk("脳筋て何だ？"),
            yula.talk("さっさと先に行くわよ"),
            yula.do("ランタンを持った$yulaを先頭に進んでいく"),
            hero.do("やがて広い空間に出た"),
            )

def sc_surrounded(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    hob = W(w.hobgoblin)
    return w.scene("囲まれる",
            hero.talk("あ、いた"),
            hero.do("巨大な水槽のようなものの前に、$hobgoblinと$makoがいる",
                "その周囲には他の$goblinはいない",
                "囚われているようには見えない"),
            hero.talk("助けなきゃ"),
            yula.talk("どうすんのよ", "周りだけで五十匹はいるわよ"),
            yula.do("自分の位置情報アプリを見せて"),
            sol.talk("それなら$meたちも逃げようがないだろ？"),
            yula.talk("あの水、外の川と繋がってるから、",
                "泳いでいけば外に出られるわ"),
            sol.talk("悪い", "$me、泳ぎは"),
            yula.talk("苦手なの？", "そのなりで"),
            sol.talk("うるせーよ"),
            sol.talk("それよりどうすんだ？　……って、おい$k_hero",
                "お前、何勝手に"),
            sol.do("見れば一人で階段を降りていき、向かっている"),
            yula.talk("あの子バカなの？"),
            sol.talk("ああ、バカだな"),
            )

def sc_negotiation(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    hob = W(w.hobgoblin)
    return w.scene("交渉する",
            hero.do("$makoたちのところに一人で向かう"),
            hero.talk("$mako！　今助けるよ！"),
            mako.talk("あ……$hero様"),
            mako.do("何故か気まずそうな顔"),
            mako.talk("来ないで！"),
            hob.talk("ど、どうされましたか？"),
            hob.do("何故か慌てて"),
            mako.talk("こっちに来ると$meを殺すと言ってます！",
                "そのまま近づかないでください", "大丈夫ですから"),
            hob.talk("え？"),
            mako.do("自分から$hobgoblinに近づき、その首に手をやらせる"),
            hero.talk("$mako！"),
            mako.talk("$meは大丈夫です",
                "$meが人質になりますから、$hero様たちは今すぐここを出て行ってください"),
            sol.do("$solと$yulaも$heroの後ろにやってくる"),
            yula.talk("ああ言ってるけど、どうするの？"),
            hero.talk("そんなの決まってるだろ", "助ける一択だよ！"),
            hero.do("$shortswordを抜いて襲いかかる"),
            mako.talk("あー、$hero様じゃ無理だから！", "こうなったら"),
            mako.do("$makoの手が光る"),
            hero.talk("え？"),
            hero.hear("巨大な爆音"),
            hero.talk("うわぁぁぁ！"),
            hero.do("天井が崩れる",
                "溜まっていた大量の水が流れ出し、大洪水を引き起こした"),
            )

def sc_escape(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    gob = W(w.goblin)
    return w.scene("脱出",
            hero.do("急いで崩壊する要塞から逃げ出す$Sたち"),
            hero.talk("なんであんなところで魔法使ったんだよ？"),
            mako.talk("ごめんなさい。つい"),
            sol.talk("ついで崩壊させるのやめてくれ！", "$meは暗いところと崩れる場所にトラウマがあんだよ！"),
            mako.talk("埋まればよかったのに"),
            sol.talk("何か言ったか？"),
            yula.talk("喧嘩してないで、あそこだよ"),
            hero.do("最初に掘られていた横穴を見つけ、そこに飛び込んだ"),
            )

def sc_no_reward(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("報酬はない！",
            hero.do("街に戻り報告したが、大惨事で怒られる"),
            hero.talk("そんな、報酬なしなんて……"),
            )

## episode
def ep_destroy(w: World):
    return w.episode("7-3.ゴブリンの巣破壊なう",
            sc_yula(w),
            sc_rescuemako(w),
            sc_surrounded(w),
            sc_negotiation(w),
            sc_escape(w),
            sc_no_reward(w),
            ## NOTE
            ##  - さらわれた？魔子を救出に向かう
            ##  - 魔子はゴブリンに囲まれていた
            ##  - ゴブリンの巣でボスと話し合いをしていた魔子の魔力が暴発して施設が崩れ去った
            )
