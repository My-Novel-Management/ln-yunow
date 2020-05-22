# -*- coding: utf-8 -*-
"""Episode: 9-3.ヘイトの魔獣誕生
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
def sc_runaway(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("逃げ惑う勇者",
            hero.be("目覚めたら、森の中"),
            outside.look("古い女神像が見える"),
            yula.talk("何してんの？　さっさと行くよ"),
            hero.talk("は、はい"),
            hero.do("再び逃げていた"),
            hero.do("今までみたいに教会に戻らない",
                "なんだか徐々に戻れる時間が短くなっている気がしていた"),
            w.eventPoint("死に戻り", "徐々に巻き戻る時間が短くなっている"),
            hero.talk("どうしたんだ$mako", "顔色が悪いが"),
            mako.talk("大丈夫ですよ。ちょっと疲れてるだけです",
                "それより、あそこみたいです"),
            hero.do("$yulaの隠れ家が見えてくる"),
            stage=w.on_jihanforest,
            day=w.in_reset6, time=w.at_morning,
            )

def sc_hideout(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$yulaの隠れ家",
            hero.come("隠れ家にやってくる"),
            yula.talk("ほんとは誰にも見せたくなかったんだけどね"),
            inside.look("洞窟の奥に蟻の巣のようになった空間に、家具などが配置されている"),
            yula.talk("昔に師匠が使ってた場所で、たぶんモンスターが巣として使っていた跡だろうって話"),
            hero.think("おそらく最初の$goblinたちの巣なのだろうと思ったが、口にしない"),
            sol.come(),
            sol.talk("一応これ持ってきたけど"),
            sol.do("$Sの手には食べ物、パンなどが入った籠"),
            yula.talk("ここにも保存食の備蓄はあるけど、いつまで耐えれるか",
                "あんたたちの$smaphはここで使うんじゃないよ"),
            hero.talk("$yulaのは？"),
            yula.talk("こういう時に備えていくつも持ってるの"),
            yula.do("$smaphを見ながら作戦会議を"),
            stage=w.on_yulahideout_int,
            time=w.at_morning,
            )

def sc_meeting(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("作戦会議",
            hero.be("みんなで食事をしながら作戦会議"),
            hero.talk("どうすりゃいいんだよ"),
            yula.talk("炎上したときは大人しく黙っておくしかないの",
                "他の話題に移ればみんなそっちに注目するから"),
            sol.talk("正直に話すだけじゃだめなのか？",
                "だってあれって誰かが加工したものなんだろ？"),
            yula.talk("全部ウソだったらいいけど、あれって微妙に真実含んでるでしょ？",
                "そういうのは火に油になるから絶対にやめた方がいい"),
            mako.talk("別のフェイクニュース流しますか？"),
            hero.talk("たとえば？"),
            mako.talk("$meが魔王だったことにして、ほんとは魔王に騙されてるんだ、とか"),
            yula.talk("$makoが魔王だとか誰も信じないわよ",
                "それに今は$heroが魔王かどうかってよりも、王様と組んでいろいろやってたっぽいって思われてるのが一番いけなくて、",
                "この不況と圧政に苦しんでた民衆の一揆でもあるのよ"),
            mako.talk("めんどくさいですね、人間て"),
            hero.talk("じゃあ、全部王が悪いってことにして、$meだけ謝ろう！",
                "あいつと$meの関係を全部話すよ"),
            )

def sc_apology(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("勇者の謝罪",
            hero.do("みんなの制止を振り切り、謝罪動画を投稿する$S"),
            sol.talk("いいぞー"),
            hero.talk("えー、みなさん、こんにちは", "$Yです",
                "この度はこんな騒動になってしまい申し訳ありません"),
            hero.do("視聴者数が一気に上がっていく",
                "悪口ばかり書き込まれる中に、いくつか応援の声も"),
            hero.talk("ご存知のとおり、$meは英雄$dadの息子ですが、だからといってそれで$Yに任命された訳ではありません",
                "実はあれ、ただの抽選だったんです！",
                "$meは$smaphのプレゼントキャンペーンに応募しただけで、",
                "当選したといって城に呼ばれて、それでこれを受け取ったら無理やり$Yにされたんです！",
                "だから$meは無実だ！",
                "あいつとは何も関係ない！",
                "まして魔王だなんてそんな訳ない！",
                "魔王が誰かは知らないけど、父さんは行方不明になったまま、",
                "それを誰かが勝手に魔王だってことにしたんだ！",
                "だから$meは無実なんです！"),
            hero.do("それに対してコメントが嘘つけとか罵倒だらけ"),
            hero.talk("みんな、聞いてくれ！",
                "あれはフェイクニュースといって"),
            yula.talk("まずいね", "もう突き止められた"),
            hero.hear("外で騒ぐ声", "ドアが叩かれている"),
            hero.do("それでも訴えを続ける"),
            yula.talk("もう無理だ！　逃げるよ！"),
            yula.do("逃げ出す$S"),
            mako.talk("やっぱり人間どもなんて信用なりませんよ"),
            hero.talk("だから$meは無実だぁぁぁぁ！"),
            hero.do("ドアを開けて飛び込む$S"),
            mako.talk("$hero様！"),
            hero.do("その時、天が閃いた"),
            )

def sc_birthmaju(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    maju = W(w.maju)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("ヘイトの魔獣誕生",
            hero.do("空が真っ暗になり、暗黒の雷が大地に落ちるのをみんな見た"),
            hero.do("それぞれの$smaphが発光する"),
            hero.talk("な、何だよ、これ！"),
            yula.talk("壊れちゃったの！？"),
            mako.do("黙り込む"),
            sol.talk("持って無くてよかったぜ"),
            hero.do(""),
            maju.come("巨大な影が海上に現れる"),
            mako.talk("あ……"),
            sol.talk("なんだ？"),
            sol.do("目と勘のいい$Sはいちはやく気づいて、渦巻く空の下に何かを確認する"),
            mako.talk("$w_majuが、生まれた"),
            hero.do("呟いた$makoを見つめる"),
            )

## episode
def ep_birth_maju(w: World):
    return w.episode("9-3.ヘイトの魔獣誕生",
            sc_runaway(w),
            sc_hideout(w),
            sc_meeting(w),
            sc_apology(w),
            sc_birthmaju(w),
            ## NOTE
            ##  - 逃げ回っても魔王への鬱憤から勇者へのヘイトが収まらない
            ##  - 勇者は自分が魔王ではないから許してほしいと放送するが、更に炎上
            ##  - 遂にヘイトの魔獣が誕生した
            )
