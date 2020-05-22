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
    return w.scene("ギルド開いていない",
            hero.come("ギルド本部前にやってくる"),
            outside.look("静まり返った本部前の通り"),
            hero.do("周囲の店が開いていないのに気づいて、おかしいなと思う"),
            hero.talk("あれー？", "おかしいな"),
            outside.look("大きな建物",
                "広場から目立つ位置にある"),
            outside.look("巨大な三階建ての石造り",
                "玄関は扉がなく、そのまま潜って中に入れる"),
            hero.do("建物の中に入ると、色々なギルドが入った建物がいくつかある",
                "ただどれもドアが閉じられている"),
            hero.do("傭兵ギルドもなぜか「臨時休業」中だった"),
            hero.talk("どうなってんだ？"),
            stage=w.on_guildhead,
            )

def sc_strangemood(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("奇妙な雰囲気",
            hero.come("家に向かおうとする$S"),
            outside.look("街の空気がおかしい"),
            outside.look("中央通りから外れて、住宅街に入る"),
            outside.look("どこも扉が閉まっている"),
            hero.talk("あれ？　今日って何かあったっけ？"),
            hero.do("$smaphを見ると知らない間にどんどんフォロワー数が増えている"),
            hero.talk("何だろ、これ？"),
            outside.look("歩いているのは黒猫だけ"),
            hero.talk("お前は、しらないよな",
                "今日は国喪って訳でもないしな"),
            hero.explain("国の大事な人がなくなったり、大勢が戦争や災害で亡くなった時には一日から数日喪に服す",
                "その時には各家庭、黒い旗をかかげる習慣になっているが、それがない"),
            hero.do("見張りの兵士すらいないのは、しかし奇妙だった"),
            stage=w.on_street,
            )

def sc_emptyhome(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    berial = W(w.berial)
    return w.scene("空っぽの家",
            hero.come("家に戻る"),
            outside.look("何故か空が既に夕闇のように暗い"),
            outside.look("家の屋根には大量にカラスが止まり、帰ってきた$heroを見下ろしている"),
            hero.talk("何なんだよ、今日は"),
            outside.look("二階建てのボロ一軒家",
                "二階は窓が閉め切られている",
                "明かりが点いている",
                "ただ煙突から煙は出ていない"),
            hero.talk("あれ？　まだ帰ってないのかな"),
            hero.think("入ろうとして誰かの視線を感じて振り返るが、誰もいない"),
            hero.do("家の中に入る"),
            stage=w.on_herohome_ext,
            )

def sc_waitingberial(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    berial = W(w.berial)
    return w.scene("$berialが待っていた",
            hero.come("家の中に入ってくる"),
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
            stage=w.on_herohome_int,
            )

def sc_sorroundmonsters(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("魔物に囲まれた勇者",
            hero.come("通りに飛び出る$S"),
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
            stage=w.on_centralsquare,
            )

def sc_re_church(w: World):
    hero = W(w.hero)
    inside, outside = W(w.inside), W(w.outside)
    clerc = W(w.clerc)
    return w.scene("そして教会で目覚めた",
            hero.be("目覚める"),
            hero.talk("うわぁぁぁぁ！"),
            clerc.be(),
            _.talk("どうしたんですか、そんな大声出して",
                "またお祈りの最中に寝ていたのですか、$hero"),
            hero.talk("$clerc神父？"),
            hero.do("落ち着いてみると、そこは教会の中で、長椅子に座っていた"),
            stage=w.on_church1_int,
            day=w.in_reset1, time=w.at_afternoon,
            )

## episode
def ep_bar(w: World):
    return w.episode("1-3.帰宅なう",
            sc_shutout(w),
            sc_strangemood(w),
            sc_emptyhome(w),
            sc_waitingberial(w),
            sc_sorroundmonsters(w),
            ## NOTE
            ##  - 酒場を訪れたが、何故か入る前に閉められる
            ##  - 街には人気がなくなり、モンスターが現れる
            ##  - モンスターたちもスマフを持っていて、勇者はたこなぐりにされて殺された
            )
