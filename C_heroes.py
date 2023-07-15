'''
========================
定义了所有的英雄
========================
'''
from B_character import boss,syr,xga
import random

def define_heroes():
    fls = boss()
    fls.name = "弗利萨"
    a = random.randint(3000, 10000)
    fls.age = a
    a = random.randint(5000,14000)#攻击
    fls.hen=a
    a = random.randint(10000,260000)#防御
    fls.henhen=a

    bjt  = syr()
    bjt.name = "贝吉塔"
    a = random.randint(1,1500)#年龄
    bjt.age=a
    a = random.randint(5000,17000)#攻击
    bjt.hen=a
    a = random.randint(10000,220000)#防御
    bjt.henhen=a

    swk  = syr()
    swk.name = "孙悟空"
    a = random.randint(1,1500)
    swk.age=a
    a = random.randint(5000,16000)#攻击
    swk.hen=a
    a = random.randint(10000,250000)#防御
    swk.henhen=a

    sl  = boss()
    sl.name = "沙鲁"
    a = random.randint(10000,30000)
    sl.age=a
    a = random.randint(5000,12000)#攻击
    sl.hen=a
    a = random.randint(10000,300000)#防御
    sl.henhen=a

    ob  = boss()
    ob.name = "布欧"
    a = random.randint(10000,30000)
    ob.age=a
    a = random.randint(5000,19000)#攻击
    ob.hen=a
    a = random.randint(10000,210000)#防御
    ob.henhen=a

    bll  = syr()
    bll.name = "布罗利"
    a = random.randint(1,1500)
    bll.age=a
    a = random.randint(5000,20000)#攻击
    bll.hen=a
    a = random.randint(5000,230000)#防御
    bll.henhen=a

    swf  = syr()
    swf.name = "孙悟饭"
    a = random.randint(1,500)
    swf.age=a
    a = random.randint(5000,20000)#攻击
    swf.hen=a
    a = random.randint(5000,250000)#防御
    swf.henhen=a

    xg  = xga()
    xg.name = "小怪"
    a = random.randint(1,1500)
    xg.age=a
    a = random.randint(5000,20000)#攻击
    xg.hen=a
    a = random.randint(5000,200000)#防御
    xg.henhen=a

    return fls,bjt,swk,sl,ob,bll,swf,xg