# -*- coding: utf-8 -*-
"""Story: yusha now
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.yunow import config as cnf
from src.yunow import chapter01 as chap1
from src.yunow import chapter02 as chap2
from src.yunow import chapter03 as chap3
from src.yunow import chapter04 as chap4
from src.yunow import chapter05 as chap5
THM = cnf.THEMES


# scenes
# episodes

# outline
def story_baseinfo(w: wd.World):
    return [
            ("story", story(w), w.yusha, w.yusha),
            ] + chap1.story_baseinfo(w) \
                + chap2.story_baseinfo(w) \
                + chap3.story_baseinfo(w) \
                + chap4.story_baseinfo(w) \
                + chap5.story_baseinfo(w)

def story_outline(w: wd.World):
    return [
            ("story", story(w),
                w.yusha.deal(w.i.beat_maou),
                w.yusha.know(w.i.destroy_peace),
                w.yusha.deal(w.phone),
                w.yusha.go(w.i.trouble),
                True),
            ] + chap1.story_outline(w) \
                + chap2.story_outline(w) \
                + chap3.story_outline(w) \
                + chap4.story_outline(w) \
                + chap5.story_outline(w)

# main
def world():
    w = wd.World("Yusha now")
    w.set_db(cnf.CHARAS,
            cnf.STAGES,
            cnf.DAYS,
            cnf.ITEMS,
            cnf.INFOS,
            cnf.FLAGS,
            )
    return w

def story(w: wd.World):
    return (w.maintitle("勇者なう！"),
            chap1.story(w),
            chap2.story(w),
            chap3.story(w),
            chap4.story(w),
            chap5.story(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

