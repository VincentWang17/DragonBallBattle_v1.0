def battle(fls,sl,ob,bjt,swk,bll,swf,dr,wo):
    import random
    import time 
    g=dr.henhen #敌方生命值
    n=dr.hen #敌方攻击力
    h=wo.henhen #我方生命值
    b=wo.hen #我方攻击力
    print(" ")
    a = random.randint(2,4)
    print("加载战场中")
    time.sleep(a)
    print("加载成功！")
    time.sleep(1)
    print("=========================开始战斗=========================")

    time.sleep(1)
    while g>0 and h>0:
        e=0
        print(" ")
        print("我方进行攻击")
        a = random.randint(1,10)
        if a==1  or a==5 or a==7 or a==9:
            print("重重一击！")
            a = random.randint(500,1000)
        elif a==3:
            print("发动技能!QIGONG WAVE!")
            print("敌人脑子晕晕的")
            a = random.randint(1000,2000)
        else:
            print("似乎没起到什么作用")
            a = random.randint(1,200)
        print(f"造成伤害 {b+a}")
        g=g-b-a
        if h<=0 or g<=0:
            break
        time.sleep(1.5)
        print(" ")
        print("敌方开始攻击")
        a = random.randint(1,10)
        if a==1  or a==5 or a==7 or a==9:
            print("重重一击！")
            a = random.randint(1000,3000)
        elif a==3:
            print("发动技能!YUANQI BULLET!")
            print("你的脑子晕晕的")
            a = random.randint(5000,7000)
        else:
            print("似乎没起到什么作用")
            a = random.randint(1,200)
        print(f"受到伤害 {n+a}")
        h=h-n-a
        if n>20000:
            if dr==sl:
                print("[自大]沙鲁被动技能-总体机能下降")
                g=g-500
                n=n-200
        elif n>15000:
            if wo==swk or wo==bll or wo==swf or wo==bjt:
                print("[生老病死]赛亚人被动技能-防御力下降")
                h=h-1000
            if dr==fls:
                print("[自大]冰冻恶魔被动技能-总体机能下降")
                g=g-500
                n=n-200
            if dr==sl:
                print("[完美攻击]沙鲁专属技能-攻击力飙升")
                n=n+500
        elif n>10000:
            if wo==swk or wo==bll or wo==swf or wo==bjt:
                print("[赛亚人的倔强]赛亚人专属技能-战斗力飙升")
                b=b+500
            if dr==fls:
                print("[古老的血脉]冰冻恶魔专属技能-战斗力飙升")
                n=n+500
        time.sleep(1.5)
        print(" ")
        if dr==ob and e%2==0:
            print("[无限吸收]布欧专属技能-防御力飙升")
            g=g+500
            print("[贪睡]布欧被动技能-攻击力下降")
            n=n-500
        e=e+1
    if g<=0:
        print("成功击退了敌方！")
    elif h<=0:
        print(wo.name+"在与"+dr.name+"的战斗中失利了...")    
    elif h<=0 and g<=0:
        print("两败俱伤！")