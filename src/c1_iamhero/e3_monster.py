# -*- coding: utf-8 -*-
"""Episode: 1-3.酒場なう
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
def sc_shutout(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("閉め出される",
            hero.come(),
            hero.do("どの店も開いていない",
                "というか、さっきは開いていた店がどんどん閉まっていた"),
            hero.talk("あれー？", "おかしいな"),
            hero.do("冒険の手引きを見て装備や仲間を揃えると書かれていたので、",
                "まずは市場を見て回ろうと思ったが、それも駄目"),
            hero.do("傭兵ギルドもなぜか「臨時休業」中だった"),
            hero.talk("どうなってんだ？"),
            )

def sc_strangemood(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("奇妙な雰囲気",
            hero.come("家に向かおうとする$S"),
            outside.look("街の空気がおかしい"),
            hero.talk("あれ？　今日って何かあったっけ？"),
            outside.look("広場の露店もなく、歩いているのは黒猫だけ"),
            _.look("どの店も閉まっている",
                "どの家も窓を閉め切っている"),
            hero.do("見張りの兵士すらいないのは、しかし奇妙だった"),
            )

def sc_emptyhome(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    berial = W(w.berial)
    return w.scene("空っぽの家",
            hero.come("家に戻る"),
            berial.be(),
            berial.look("黄金の皮膚を持つ大きな体の魔物"),
            berial.talk("よう？"),
            hero.talk("あの、どなたですか？"),
            hero.do("明らかに人間じゃないと分かる。魔物。それもかなり強い"),
            hero.do("同じ部屋にいるだけで震えていた"),
            berial.talk("お前、$w_Yなんだってな？"),
            hero.talk("え、違いますよ"),
            berial.talk("おいおい。そんなに謙遜しなくてもいいんだぜ？"),
            berial.do("$smaphを見せて、そこにある「勇者なう」の$w_tweetを見せる"),
            hero.talk("それ、$meのじゃないですから！"),
            berial.talk("全くよ", "手間かけさせやがって"),
            hero.talk("あの、$k_mamはどこですか？"),
            berial.do("顎で台所を示す"),
            inside.look("床に血が広がっている"),
            hero.talk("え……"),
            berial.talk("すぐに会えるさ、あの世でな"),
            berial.do("襲いかかってくる"),
            hero.do("拾ってきた黒猫が飛び出して、その間に逃げ出す"),
            berial.talk("くそっ！"),
            )

def sc_sorroundmonsters(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("魔物に囲まれた勇者",
            hero.do("中央広場まで逃げてくる$S"),
            hero.talk("何なんだよ。なんで街の中に魔物が？"),
            hero.do("$smaphが鳴る"),
            hero.do("見ると大量の通知がある"),
            hero.talk("なんだこれ？"),
            hero.do("どれもがフォロー通知ばかり"),
            hero.talk("どういうこと？"),
            hero.do("意味を理解していない$Sの前に、再び魔物たちが現れる"),
            outside.look("街には$hero以外は誰の姿もない", "魔物だけだ"),
            hero.talk("ちょっと！　誰か！　助けてよ！"),
            hero.do("と、$w_gazouが送られてくる",
                "見ると慌てている$Sの表情を撮影したもの"),
            hero.do("魔物の一匹が$smaphを構えてこちらに向けている"),
            hero.do("次々に送られてくる"),
            hero.do("$w_msgもいっぱいきて、どれもが解読不可能な言葉が並ぶ"),
            hero.talk("え？　ひょっとして"),
            hero.think("これは全部魔物なのではないかと気づいた"),
            hero.do("$w_iconにはどれも魔物が並ぶ"),
            hero.do("魔物たちは全員$smaphを手に近づいてくる"),
            hero.do("そのうちの一匹は言った「$w_Yころす」と"),
            hero.think("自分が$w_Yと呟いたばかりに、こんなことになったのだと理解した"),
            hero.talk("た、助けてくれ！"),
            hero.do("だが誰も助けてはくれない",
                "魔物たちによって囲まれ、世界は暗くなった"),
            )

## episode
def ep_bar(w: World):
    return w.episode("1-3.酒場なう",
            sc_shutout(w),
            sc_strangemood(w),
            sc_emptyhome(w),
            sc_sorroundmonsters(w),
            ## NOTE
            ##  - 酒場を訪れたが、何故か入る前に閉められる
            ##  - 街には人気がなくなり、モンスターが現れる
            ##  - モンスターたちもスマフを持っていて、勇者はたこなぐりにされて殺された
            )
