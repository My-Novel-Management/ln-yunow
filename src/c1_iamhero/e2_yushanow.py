# -*- coding: utf-8 -*-
"""Episode: 1-2.教会なう
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
def sc_church(w: World):
    hero = W(w.hero)
    yula = W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("教会にて",
            hero.come("教会を訪れる"),
            inside.look("玄関の木戸を潜ると、そこには長椅子の並ぶホールが広がる"),
            inside.look("細長いステンドグラスには$w_godや、世界創生神話が描かれる"),
            w.eventPoint("人物紹介", "$yula初登場"),
            yula.be("神父の代わりに、知らない女性がいる"),
            yula.look("神父の衣装ではない",
                "長い金髪にすらりと背の高い女性",
                "まつげが長く、しゅっと切れ長の目",
                "涼し気な口元に濃い紅"),
            yula.look("肩からズタ袋を下げている"),
            yula.do("背を向けて立っている",
                "聖書を開いている"),
            hero.talk("あのー、$clerc神父は？"),
            yula.talk("あ、えっとね、神父なら今旅行中だから、$meが代行しているのよ"),
            hero.talk("そうなんですか"),
            yula.look("普通の服装", "長い金髪を後ろでくくっている", "美人でスリム",
                "胸は大きい"),
            hero.talk("あの、お祈りいいすか？"),
            yula.talk("ええ、どうぞ"),
            hero.do("祈りの言葉を唱えて、手を合わせる"),
            yula.talk("でも最近の若い子にしては珍しいわね",
                "何？　親が熱心なの？"),
            hero.talk("ああ、$me、父親が失踪してるんですよ"),
            hero.do("こう見えて$dadが失踪して以来、毎日帰ってくることを願って祈りを欠かさなかった"),
            yula.talk("そう", "それじゃあしっかり祈っときなさい"),
            yula.do("何故か$Sも一緒に女神像に祈る"),
            w.comment("$yulaと話しておく"),
            stage=w.on_church1,
            )

def sc_explainsmaph(w: World):
    hero = W(w.hero)
    yula = W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$smaphの使い方",
            yula.be(),
            hero.be(),
            yula.do("$smaphを触って何か確認している$S"),
            yula.talk("へえ、何かやたらと賑わってるわね", "何でだろ"),
            hero.talk("あのー、代理さん"),
            yula.talk("代理ってねえ、$meは$yulaって名前があるのよ",
                "で、何さ？"),
            hero.talk("これ、使い方って分かります？"),
            yula.talk("あんた$smaphも知らないの？"),
            hero.talk("いや、今日初めてなもんで"),
            yula.talk("最新型じゃない", "あんたひょっとして金持ちのぼんぼん？"),
            hero.talk("全然", "抽選で当たって"),
            yula.talk("うらやましいわ"),
            hero.do("$yulaから$smaphの使い方について少し教わる"),
            yula.talk("基本的には画面にいろいろ表示されるし、",
                "わからなければヘルプを見ればいい",
                "説明が出てるでしょ？"),
            hero.talk("これはどうやって出すんですか？"),
            yula.do("頭を抱えるが、一応教えてやる"),
            hero.talk("あー！", "これで$w_tweetすればいいのか！"),
            yula.talk("だからね、ここをこうして"),
            hero.talk("おお、すげえ！"),
            hero.do("画面にはずらずらと世界中の人の$w_tweetが流れてくる"),
            hero.do("その中にやけに「$w_Y」という文字が踊っている"),
            yula.talk("あれ？　なんかバズってるわね"),
            hero.talk("バズ？"),
            yula.talk("人気だってこと",
                "で、もういい？", "$meもそろそろ行かないと"),
            hero.talk("あ、どうもありがとうございました"),
            yula.go("出て行ってしまう"),
            hero.talk("あれ？　代行はいいの？"),
            )

def sc_followers(w: World):
    hero = W(w.hero)
    yula = W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("勇者のフォロワー",
            hero.come("教会を出て、とりあえず中央広場に戻ってくる"),
            outside.look("閑散として露店も何もなくなっている"),
            hero.talk("あれ？　どうしたんだろう",
                "今日って何かあったかな？"),
            hero.think("生まれる前は魔物が街に何度も押し入ってきて、その度に全員避難とかしていたらしい"),
            hero.do("警鐘も聞いていないし、と"),
            hero.do("閑散とした空気を感じる"),
            hero.do("黒猫一匹だけいるのを見て"),
            hero.do("と、$smaphに通知が"),
            hero.talk("何だこれ？"),
            hero.do("画面にはフォローされましたと出る",
                "名前は全然知らない。$makoとかいう文字が出ている"),
            hero.talk("何だこれ"),
            hero.talk("ま、いっか"),
            hero.do("旅の手引きを確認する$S"),
            w.eventPoint("旅の手引き", "手引きを見て仲間と準備が必要と知る"),
            hero.do("旅の手引きには仲間を集めることと、装備や薬草など、旅に必要なものを揃えてから出発するように書かれている"),
            hero.talk("仲間ってどこで集めればいいんだ？"),
            hero.do("よく旅の商人が傭兵を雇っていることを思い出して"),
            hero.talk("傭兵ギルドか"),
            hero.go("ギルド本部に向かう"),
            stage=w.on_centralsquare,
            )

## episode
def ep_church(w: World):
    return w.episode("1-2.教会なう",
            sc_church(w),
            sc_explainsmaph(w),
            sc_followers(w),
            ## NOTE
            ##  - 教会にやってきて祈ろうとする
            ##  - 教会は神父代理という女性がいた
            ##  - 祈りを済ませて外に出る。勇者のフォローが増えていて喜ぶ
            )
