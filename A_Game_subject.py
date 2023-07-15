'''
========================
主体(待做：战斗系统变为选项！！！)
========================
'''
from D_Define_status_wo import define_Define_status
from E_Define_status_dr import define_Define_status2
from F_WenZi import WenZi
from G_battle import battle
from C_heroes import define_heroes
fls,bjt,swk,sl,ob,bll,swf,xg = define_heroes()
wo = define_Define_status(bjt,swk,bll,swf)
wz = WenZi()
dr = define_Define_status2(fls,sl,ob,xg)
print(" ")
zd = battle(fls,sl,ob,bjt,swk,bll,swf,dr,wo)