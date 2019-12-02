# -*- coding: utf-8 -*-
"""Story: the yusha now
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.yunow import config as cnf

## titles
ADV_BOOKS = (
        # NOTE: 個人情報編
        "冒険の書１　勇者なう！",
        "冒険の書２　特定なう！",
        "冒険の書３　mamazonなう！",
        # NOTE: 冒険準備編
        "冒険の書４　ゲームなう！",# NOTE: 重課金
        "冒険の書５　moucariなう！",
        "冒険の書６　配信なう！",
        # NOTE: 炎上編
        "冒険の書７　人気なう！",
        "冒険の書８　拡散なう！",
        "冒険の書９　炎上なう！",
        # NOTE: フェイクニュース編
        "冒険の書１０　フェイクニュースなう！",
        "冒険の書１１　陰謀論なう！",
        "冒険の書１２　魔王なう！",
        )

## scenes
### chapter 1
def sc_callcastle(w: wd.World):
    s = w.scene("城に呼び出された", "城に呼び出しを受けてやってきた少年は、王様を前に緊張する")
    return s

def sc_kingtalk(w: wd.World):
    s = w.scene("王の話", "王は少年に勇者の称号を与えると言い始める")
    return s

def sc_obtains(w: wd.World):
    s = w.scene("勇者の装備", "勇者となった少年は装備と金、念願のスマフを手に入れる")
    return s

def sc_outtotown(w: wd.World):
    s = w.scene("城下町に戻って", "上機嫌で城下町に戻った彼はまず教会に向かう")
    return s

def sc_church_and_lady(w: wd.World):
    s = w.scene("教会と女性", "教会で祈りを済ませた勇者は代役という女性からスマフの使い方を教わる")
    return s

def sc_accountentry(w: wd.World):
    s = w.scene("アカウント登録", "勇者は彼女に教わったように登録して呟いてみる")
    return s

def sc_webworld(w: wd.World):
    s = w.scene("魔ネット世界", "魔ネットは広大な情報の海だった。勇者はそれに驚く")
    return s

def sc_appeardaemons(w: wd.World):
    s = w.scene("仲間集めに", "冒険には仲間が必要と、酒場に向かった勇者の前に魔物が現れた")
    return s

### chapter 2
def sc_againchurch(w: wd.World):
    s = w.scene("また教会に", "気づくと教会にいた")
    return s

def sc_check_now(w: wd.World):
    s = w.scene("状況確認", "神父の話を聞いて、状況を確認する")
    return s

def sc_gotobar(w: wd.World):
    s = w.scene("酒場に行こう", "とにかく仲間集めと再び酒場に向かうことにする")
    return s

def sc_inthebar(w: wd.World):
    s = w.scene("酒場にて", "ガキということで見くびられつつ、店主たちから色々と教わる")
    return s

def sc_backwayhome(w: wd.World):
    s = w.scene("家に戻る途中で", "一旦家に戻ろうとした勇者だったが")
    return s

def sc_findlostcat(w: wd.World):
    s = w.scene("迷子猫発見", "迷子になったという猫を見つけるがそこには戦士がいた")
    return s

def sc_soldierreason(w: wd.World):
    s = w.scene("ソルの事情", "金稼ぎに出てきたという戦士")
    return s

def sc_gobackhome(w: wd.World):
    s = w.scene("帰宅", "一旦家に戻る")
    return s

def sc_visitorgirl(w: wd.World):
    s = w.scene("少女の訪問者", "謎の少女が勇者を訪ねてくるが、彼女はストーカーだった")
    return s

### chapter 3
### chapter 4
### chapter 5
### chapter 6
### chapter 7
### chapter 8
### chapter 9
### chapter 10
### chapter 11
### chapter 12

## episodes
""" NOTE: １話の基本構成を以下にする
        Avant story: 1000字程度でおさらいや、期待煽り
        Main A: Aパート。5000字以内。基本的に前半
        Main B: Bパート。5000字以内。基本的に後半
        Adding C: Cパート。必要な時に補足で入れる。1000字程度まで
"""
### chapter 1
def ep_getsmaph(w: wd.World):
    return w.episode("勇者なう", "城に呼び出され、勇者に任命される",
            sc_callcastle(w),
            sc_kingtalk(w),
            sc_obtains(w),
            )

def ep_church(w: wd.World):
    return w.episode("教会なう", "神父に会って使い方などを聞こうとするが知らない女性がいた",
            # NOTE: ユラは実は精霊神。全ての元凶であった
            sc_outtotown(w),
            sc_church_and_lady(w),
            sc_accountentry(w),
            )

def ep_identification(w: wd.World):
    return w.episode("特定なう", "仲間と情報集めに向かったところ魔王軍に襲われてボコられる",
            sc_webworld(w),
            sc_appeardaemons(w),
            )

### chapter 2
def ep_re_church(w: wd.World):
    return w.episode("Re:教会なう", "何故か復活して教会にいる勇者。またユラがいて文句",
            sc_againchurch(w),
            sc_check_now(w),
            )

def ep_bar(w: wd.World):
    return w.episode("酒場なう", "酒場にやってくるが、相手にされない。勇者と言おうとするが",
            sc_gotobar(w),
            sc_inthebar(w),
            )

def ep_lostcat(w: wd.World):
    return w.episode("迷子の子猫なう", "家に帰ろうとしたところで猫と戦士と遭遇",
            sc_backwayhome(w),
            sc_findlostcat(w),
            sc_soldierreason(w),
            )

def ep_stalker(w: wd.World):
    return w.episode("ストーカーなう", "ストーカー少女・魔子が現れる",
            # NOTE: Cパート
            sc_gobackhome(w),
            sc_visitorgirl(w),
            )

### chapter 3
def ep_girlfriend(w: wd.World):
    return w.episode("彼女なう", "勇者に恋した紆余曲折を説明する魔子",
            )

def ep_preparation(w: wd.World):
    return w.episode("冒険準備なう", "冒険するには準備が必要。",
            )

def ep_mamazon(w: wd.World):
    return w.episode("mamazonなう", "スマフで注文できるmamazonでは、何でも揃えられた",
            )

def ep_bustermaou(w: wd.World):
    return w.episode("魔王退治なう", "魔王退治を注文した結果……",
            )

### chapter 4
def ep_game(w: wd.World):
    return w.episode("ゲームなう", "勇者はスマフでできる仮想世界での冒険に傾倒していた",
            )

def ep_dependence(w: wd.World):
    return w.episode("依存症なう", "ゲーム依存症になってしまった勇者",
            )

def ep_heavybilling(w: wd.World):
    return w.episode("廃課金なう", "課金が恐ろしいことになる",
            # NOTE: 大量の請求書を見て驚くことに
            )

### chapter 5
def ep_re_preparation(w: wd.World):
    return w.episode("冒険準備なう", "金がないが何とか冒険準備をしようと相談",
            )

def ep_moneyplan(w: wd.World):
    return w.episode("金策なう", "何とか金を用意しよう",
            )

def ep_auction(w: wd.World):
    return w.episode("オークションなう", "魔ネットオークションに挑戦するが",
            )

### chapter 6
def ep_doga(w: wd.World):
    return w.episode("動画配信者なう", "儲かるという噂の動画配信を始めてみる勇者たち",
            )

def ep_challenge(w: wd.World):
    return w.episode("挑戦なう", "動画をバズらせるため、様々な挑戦を行うが",
            )

def ep_collect(w: wd.World):
    return w.episode("取り立てなう", "借金の取り立てに追い詰められ逃亡するが",
            # NOTE: 街の外には凶悪な怪物が何故か勇者を待ち構えていた
            )

### chapter 7
def ep_luckyman(w: wd.World):
    return w.episode("バズったなう", "何故か以前投稿した動画がバズってしまった",
            )

def ep_popular(w: wd.World):
    return w.episode("人気者なう", "動画投稿者として有名になり、城に呼ばれる",
            )

def ep_IamYusha(w: wd.World):
    return w.episode("勇者なう", "人気者となった勇者はいい気になり自分が勇者と告白する",
            )

### chapter 8
def ep_diffusion(w: wd.World):
    return w.episode("拡散なう", "勇者であることはまたたく間に拡散し、一大勇者ブーム到来",
            )

def ep_business(w: wd.World):
    return w.episode("事業展開なう", "勇者で一発当てようと事業を興す",
            )

def ep_bankruptcy(w: wd.World):
    return w.episode("倒産なう", "しかしあえなく倒産し、借金だけが残った",
            )

### chapter 9
def ep_sliptongue(w: wd.World):
    return w.episode("失言なう", "ある動画で失言してしまう",
            )

def ep_burning(w: wd.World):
    return w.episode("炎上なう", "失言から炎上し、批難の嵐",
            )

def ep_withdrawal(w: wd.World):
    return w.episode("引きこもりなう", "世界に出るのが怖くなり引きこもる勇者",
            )

### chapter 10
def ep_yushaisrogue(w: wd.World):
    return w.episode("悪勇者なう", "勇者は悪者という呟きを見つける",
            )

def ep_trickme(w: wd.World):
    return w.episode("悪戯なう", "勇者たちは次々に謎の悪戯被害を受ける",
            )

def ep_ficticiousclaim(w: wd.World):
    return w.episode("架空請求なう", "大量の謎の請求書被害",
            )

def ep_arrest(w: wd.World):
    return w.episode("逮捕なう", "勇者は逮捕されてしまった",
            )

### chapter 11
def ep_yushaismao(w: wd.World):
    return w.episode("お前が魔王なう", "勇者は何故か魔王にされてしまう",
            )

def ep_rescueyusha(w: wd.World):
    return w.episode("勇者救出作戦なう", "魔子たちは相談して勇者を城から救出する",
            )

def ep_trial(w: wd.World):
    return w.episode("裁判なう", "人質にされた母親のために裁判に挑む勇者たち",
            )

def ep_objection(w: wd.World):
    return w.episode("異議ありなう", "魔王のフェイクニュースに魔子はそれを否定する",
            # NOTE: 魔子がその魔王だった？
            )

### chapter 12
def ep_Iammao(w: wd.World):
    return w.episode("魔王なう", "魔王編。実は魔王の正体は魔子だった",
            )

def ep_findyusha(w: wd.World):
    return w.episode("勇者発見なう", "魔子は勇者をずっと監視していた",
            )

def ep_confession(w: wd.World):
    return w.episode("告白なう", "魔子は勇者に告白した",
            )

def ep_ourjurney(w: wd.World):
    return w.episode("Re:勇者なう", "そして旅は続く",
            # NOTE: 魔王の正体が魔子だったと判明するが、一緒に旅を続ける選択をする
            )

## chapters
def ch1(w: wd.World):
    return w.chapter(ADV_BOOKS[0],
            ep_getsmaph(w),
            ep_church(w),
            ep_identification(w),
            )

def ch2(w: wd.World):
    return w.chapter(ADV_BOOKS[1],
            ep_re_church(w),
            ep_bar(w),
            ep_lostcat(w),
            ep_stalker(w),
            )

def ch3(w: wd.World):
    return w.chapter(ADV_BOOKS[2],
            # NOTE: 冒険準備、mamazon登場
            # NOTE: 怪しげな人が配達
            ep_girlfriend(w),
            ep_preparation(w),
            ep_mamazon(w),
            ep_bustermaou(w),
            )

def ch4(w: wd.World):
    return w.chapter(ADV_BOOKS[3],
            ep_game(w),
            ep_dependence(w),
            ep_heavybilling(w),
            )

def ch5(w: wd.World):
    return w.chapter(ADV_BOOKS[4],
            ep_re_preparation(w),
            ep_moneyplan(w),
            ep_auction(w),
            )

def ch6(w: wd.World):
    return w.chapter(ADV_BOOKS[5],
            ep_doga(w),
            ep_challenge(w),
            ep_collect(w),
            )

def ch7(w: wd.World):
    return w.chapter(ADV_BOOKS[6],
            # NOTE: 動画配信で稼ごう
            ep_luckyman(w),
            ep_popular(w),
            ep_IamYusha(w),
            )

def ch8(w: wd.World):
    return w.chapter(ADV_BOOKS[7],
            ep_diffusion(w),
            ep_business(w),
            ep_bankruptcy(w),
            )

def ch9(w: wd.World):
    return w.chapter(ADV_BOOKS[8],
            ep_sliptongue(w),
            ep_burning(w),
            ep_withdrawal(w),
            )

def ch10(w: wd.World):
    return w.chapter(ADV_BOOKS[9],
            ep_yushaisrogue(w),
            ep_trickme(w),
            ep_ficticiousclaim(w),
            ep_arrest(w),
            )

def ch11(w: wd.World):
    return w.chapter(ADV_BOOKS[10],
            ep_yushaismao(w),
            ep_rescueyusha(w),
            ep_trial(w),
            ep_objection(w),
            )

def ch12(w: wd.World):
    return w.chapter(ADV_BOOKS[11],
            ep_Iammao(w),
            ep_findyusha(w),
            ep_confession(w),
            ep_ourjurney(w),
            )

## setting
def set_stages(w: wd.World):
    return w

# main
def world():
    w = wd.World(2)
    w.set_db(cnf.PERSONS, cnf.CHARAS,
            cnf.STAGES,
            cnf.DAYS, cnf.TIMES,
            cnf.ITEMS,
            cnf.WORDS)
    set_stages(w)
    return w

def story(w: wd.World):
    return w.story("勇者なう！",
            # NOTE: 内容は１巻相当
            #       ずっと最初の街の中で、色々とスマフと魔ネットを通じた物語
            #       ２巻から「冒険編」突入
            ch1(w),
            ch2(w),
            ch3(w),
            ch4(w),
            ch5(w),
            ch6(w),
            ch7(w),
            ch8(w),
            ch9(w),
            ch10(w),
            ch11(w),
            ch12(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

