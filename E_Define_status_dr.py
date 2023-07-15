'''
========================
敌人状态
========================
'''

def define_Define_status2(fls,sl,ob,xg):
    
    import random
    a = random.randint(1,4)
    if a==1:
        dr = fls
        print(dr.name)    
    
        b = random.randint(1,4)
        if b==1:
            dr.boss1()
            dr.hen=dr.hen+1000
            dr.henhen=dr.henhen+1000
        if b==2:
            dr.boss2()
            dr.hen=dr.hen+3000
            dr.henhen=dr.henhen+3000
        if b==3:
            dr.boss3()
            dr.hen=dr.hen+7000
            dr.henhen=dr.henhen-3000
        if b==4:
            dr.boss4()
            dr.hen=dr.hen+5000
            dr.henhen=dr.henhen+5000
        if b==5:
            dr.boss13()
            dr.hen=dr.hen+2999
            dr.henhen=dr.henhen+2999
    elif a==2:
        dr = sl
        print(dr.name)
        b = random.randint(1,3)
        if b==1:
            dr.boss5()
            dr.hen=dr.hen+3000
            dr.henhen=dr.henhen+3000
        if b==2:
            dr.boss6()
            dr.hen=dr.hen+6000
            dr.henhen=dr.henhen+6000
        if b==3:
            dr.boss7()
            dr.hen=dr.hen+9000
            dr.henhen=dr.henhen+9000
    elif a==3:
        dr = ob
        print(dr.name)
        b = random.randint(1,5)
        if b==1:
            dr.boss8()
            dr.hen=dr.hen-2000
            dr.henhen=dr.henhen+8000
        if b==2:
            dr.boss9()
            dr.hen=dr.hen+8000
            dr.henhen=dr.henhen-5000
        if b==3:
            dr.boss10()
            dr.hen=dr.hen+7000
            dr.henhen=dr.henhen+7000
        if b==4:
            dr.boss11()
            dr.hen=dr.hen+5000
            dr.henhen=dr.henhen+5000
        if b==5:
            dr.boss12()
            dr.hen=dr.hen+3000
            dr.henhen=dr.henhen+3000
    elif a==4:
        dr = xg
        print(dr.name)
        b = random.randint(1,50)
        if b<50:
            xgs(dr, b)
        else:
            dr.xg22()
            dr.hen=19999
            dr.henhen=19999
    dr.sui()
    dr.ji()
    dr.fang()
    return dr

def xgs(dr, b):
    if b==1:
        dr.xg1()
        dr.hen=dr.hen+5000
        dr.henhen=dr.henhen+2000
        dr.xg1() 
    if b==2:
        dr.xg2()
        dr.hen=dr.hen+3500
        dr.henhen=dr.henhen+3500
        dr.xg2()
    if b==3:
        dr.xg3()
        dr.hen=dr.hen+3500
        dr.henhen=dr.henhen+3500
    if b==4:
        dr.xg4()
        dr.hen=dr.hen+3500
        dr.henhen=dr.henhen+3500
    if b==5:
        dr.xg5()
        dr.hen=dr.hen+3500
        dr.henhen=dr.henhen+3500
    if b==6:
        dr.xg6()
        dr.hen=dr.hen+4000
        dr.henhen=dr.henhen+4000
    if b==7:
        dr.xg7()
        dr.hen=dr.hen+4000
        dr.henhen=dr.henhen+4000
    if b==8:
        dr.xg8()
        dr.hen=dr.hen+3500
        dr.henhen=dr.henhen+3500
    if b==9:
        dr.xg9()
        dr.hen=dr.hen+3500
        dr.henhen=dr.henhen+3500
    if b==10:
        dr.xg10()
        dr.hen=dr.hen+4000
        dr.henhen=dr.henhen+4000
    if b==11:
        dr.xg11()
        dr.hen=dr.hen+2000
        dr.henhen=dr.henhen+2000
    if b==12:
        dr.xg12()
        dr.hen=dr.hen+1000
        dr.henhen=dr.henhen+1000
    if b==13:
        dr.xg13()
        dr.hen=dr.hen+2000
        dr.henhen=dr.henhen+2000
    if b==14:
        dr.xg14()
        dr.hen=dr.hen+4500
        dr.henhen=dr.henhen+4500
    if b==15:
        dr.xg15()
        dr.hen=dr.hen+3000
        dr.henhen=dr.henhen+3000
    if b==16:
        dr.xg16()
        dr.hen=dr.hen+3000
        dr.henhen=dr.henhen+3000
    if b==17:
        dr.xg17()
        dr.hen=dr.hen+3000
        dr.henhen=dr.henhen+3000
    if b==18:
        dr.xg18()
        dr.hen=dr.hen+3000
        dr.henhen=dr.henhen+3000
    if b==19:
        dr.xg19()
        dr.hen=dr.hen+3000
        dr.henhen=dr.henhen+3000
    if b==20:
        dr.xg20()
        dr.hen=dr.hen+3000
        dr.henhen=dr.henhen+3000
    if b==21:
        dr.xg21()
        dr.hen=dr.hen+3000
        dr.henhen=dr.henhen+3000