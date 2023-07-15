'''
========================
选英雄+状态
========================
'''

def define_Define_status(bjt,swk,bll,swf):
    import random
    
    print("=========================龙珠激斗=========================")
    print("请选择您的英雄")
    d=input("A贝吉塔 B孙悟空 C布罗利 D孙悟饭")
    if d=='A' or d=='a':
        wo = bjt
        print(wo.name)
        wo.daxue2()
    if d=='B'or d=='b':
        wo = swk
        print(wo.name)
        wo.daxue1()
    if d=='C'or d=='c':
        wo = bll
        print(wo.name)
        wo.daxue2()
    if d=='D'or d=='d':
        wo = swf
        print(wo.name)
        wo.daxue2()
    if wo != swf:
        a = random.randint(1,8)
        if a==1:
            wo.syr1()
        if a==2:
            wo.syr2()
            wo.hen=wo.hen-1000
            wo.henhen=wo.henhen+2000
        if a==3:
            wo.syr3()
            wo.hen=wo.hen+5000
            wo.henhen=wo.henhen-3000
        if a==4:
            wo.syr4()
            wo.hen=wo.hen+8000
            wo.henhen=wo.henhen-10000
        if a==5:
            wo.syr5()
            wo.hen=wo.hen+2000
            wo.henhen=wo.henhen+2000
        if a==6:
            wo.syr6()
            wo.hen=wo.hen+5000
            wo.henhen=wo.henhen+5000
        if a==7:
            wo.syr7() 
            wo.hen=wo.hen+2000
            wo.henhen=wo.henhen+10000
        if a==8:
            wo.syr8()
            wo.hen=wo.hen+2000
            wo.henhen=wo.henhen+10000 
    else:
        print("[神秘悟饭]悟饭专属角色技能-锁定形态")
        wo.syr9()
        wo.hen=wo.hen+7000
        wo.henhen=wo.henhen+5000
    wo.sui()
    wo.ji()
    wo.fang()
    return wo