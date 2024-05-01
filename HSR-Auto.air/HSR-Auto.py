# -*- encoding=utf8 -*-
__author__ = "GamerNoTitle"

from airtest.core.api import *
#import os
#os.system(r'adb connect 127.0.0.1:7555')
#sleep(180)
auto_setup(__file__, devices=["Android://127.0.0.1:7555"])
# auto_setup(__file__)
# 当模拟器启动完成时，桌面有崩铁的字
exists(Template(r"tpl1714570238712.png", record_pos=(-0.171, 0.042), resolution=(1920, 1080)))
touch(Template(r"tpl1714571577114.png", record_pos=(-0.17, 0.009), resolution=(1920, 1080)))
sleep(120)
# 出现点击进入时说明已经可以进入游戏
wait(Template(r"tpl1714570996830.png", record_pos=(-0.003, 0.238), resolution=(1920, 1080)))
touch(Template(r"tpl1714571081312.png", record_pos=(-0.415, -0.243), resolution=(1920, 1080)))
sleep(60)
# 等待加载，找手机，领取邮件和每日委托奖励
wait(Template(r"tpl1714571211758.png", record_pos=(-0.472, -0.226), resolution=(1920, 1080)))
touch(Template(r"tpl1714571218604.png", record_pos=(-0.472, -0.227), resolution=(1920, 1080)))
sleep(3)
wait(Template(r"tpl1714571242170.png", record_pos=(0.464, -0.104), resolution=(1920, 1080)))
touch(Template(r"tpl1714571248212.png", record_pos=(0.464, -0.104), resolution=(1920, 1080)))
sleep(3.0)
if exists(Template(r"tpl1714571298338.png", record_pos=(-0.206, 0.232), resolution=(1920, 1080))):
    touch(Template(r"tpl1714571303461.png", record_pos=(-0.205, 0.232), resolution=(1920, 1080)))
    touch(Template(r"tpl1714571360547.png", record_pos=(0.461, -0.254), resolution=(1920, 1080)))
touch(Template(r"tpl1714571360547.png", record_pos=(0.461, -0.254), resolution=(1920, 1080)))
# 因为领取了奖励以后有一个覆盖层，所以要点多一次

# 若每日委托是完成的状态

touch(Template(r"tpl1714571452279.png", record_pos=(0.376, -0.048), resolution=(1920, 1080)))
if exists(Template(r"tpl1714571467506.png", record_pos=(-0.316, 0.241), resolution=(1920, 1080))):
    touch(Template(r"tpl1714571467506.png", record_pos=(-0.316, 0.241), resolution=(1920, 1080)))
    touch(Template(r"tpl1714571532485.png", record_pos=(0.162, 0.212), resolution=(1920, 1080)))
    touch(Template(r"tpl1714571485296.png", record_pos=(0.462, -0.254), resolution=(1920, 1080)))
touch(Template(r"tpl1714571485296.png", record_pos=(0.462, -0.254), resolution=(1920, 1080)))
    
    # 退出每日委托
    
# 往下滑找地图按钮
swipe(Template(r"tpl1714577070679.png", record_pos=(0.253, 0.086), resolution=(1920, 1080)), vector=[-0.13, -0.2714])
sleep(2)

touch(Template(r"tpl1714571795246.png", record_pos=(0.375, 0.045), resolution=(1920, 1080)))
# 点击星图
touch(Template(r"tpl1714571806915.png", record_pos=(0.455, -0.206), resolution=(1920, 1080)))
sleep(5)
# 点击匹诺康尼
touch(Template(r"tpl1714571815666.png", record_pos=(0.06, -0.069), resolution=(1920, 1080)))
sleep(5)
# 向上滑，先点到观景车厢（因为如果已经在此地图的话，它的底色不一样
swipe(Template(r"tpl1714577157428.png", record_pos=(0.328, 0.047), resolution=(1920, 1080)), vector=[-0.1295, 0.3384])
touch(Template(r"tpl1714571837524.png", record_pos=(0.246, -0.105), resolution=(1920, 1080)))
# 向下滑，找到稚子的梦，找一个锚点回血
swipe(Template(r"tpl1714577975108.png", record_pos=(0.324, 0.045), resolution=(1920, 1080)), vector=[-0.1425, -0.2799])
touch(Template(r"tpl1714572059835.png", record_pos=(0.244, 0.013), resolution=(1920, 1080)))
for i in range(0,7): # 点7次缩小按钮
    # 将地图缩小到最小
    touch(Template(r"tpl1714571940900.png", record_pos=(-0.218, 0.235), resolution=(1920, 1080)))
    
touch(Template(r"tpl1714572090272.png", record_pos=(-0.099, -0.085), resolution=(1920, 1080)))
touch(Template(r"tpl1714572097861.png", record_pos=(0.328, 0.224), resolution=(1920, 1080)))
sleep(10)
wait(Template(r"tpl1714571211758.png", record_pos=(-0.472, -0.226), resolution=(1920, 1080)))
touch(Template(r"tpl1714571218604.png", record_pos=(-0.472, -0.227), resolution=(1920, 1080)))
# 往下滑找地图按钮
swipe(Template(r"tpl1714577136919.png", record_pos=(0.252, 0.091), resolution=(1920, 1080)), vector=[-0.1267, -0.2474])
sleep(2)

touch(Template(r"tpl1714571795246.png", record_pos=(0.375, 0.045), resolution=(1920, 1080)))
# 点击星图
touch(Template(r"tpl1714571910909.png", record_pos=(0.296, 0.076), resolution=(1920, 1080)))
for i in range(0,7): # 点7次缩小按钮
    # 将地图缩小到最小
    touch(Template(r"tpl1714571940900.png", record_pos=(-0.218, 0.235), resolution=(1920, 1080)))
sleep(2)
wait(Template(r"tpl1714572197481.png", record_pos=(-0.319, 0.114), resolution=(1920, 1080)))
# 传送到匹诺康尼同谐本

touch(Template(r"tpl1714572204094.png", record_pos=(-0.315, 0.081), resolution=(1920, 1080)))
touch(Template(r"tpl1714572215950.png", record_pos=(0.326, 0.224), resolution=(1920, 1080)))
sleep(10)
wait(Template(r"tpl1714571211758.png", record_pos=(-0.472, -0.226), resolution=(1920, 1080)))
touch(Template(r"tpl1714572251315.png", record_pos=(0.121, 0.054), resolution=(1920, 1080)))
battle = True
while battle:
    touch(Template(r"tpl1714572251315.png", record_pos=(0.121, 0.054), resolution=(1920, 1080)))
    for i in range(0,5):
        touch(Template(r"tpl1714572278298.png", record_pos=(0.453, 0.177), resolution=(1920, 1080)))
    touch(Template(r"tpl1714572477073.png", record_pos=(0.354, 0.233), resolution=(1920, 1080)))
    while exists(Template(r"tpl1714578748921.png", record_pos=(-0.001, -0.123), resolution=(1920, 1080))):
        touch(Template(r"tpl1714578755941.png", record_pos=(-0.134, 0.123), resolution=(1920, 1080)))
        sleep(1)
        if find_all(Template(r"tpl1714580140841.png", record_pos=(0.308, 0.172), resolution=(1920, 1080)))[0]['confidence']>0.9:
            battle = False
            break
        sleep(2)
        touch(Template(r"tpl1714578773008.png", record_pos=(0.156, 0.177), resolution=(1920, 1080)))
        touch(Template(r"tpl1714572477073.png", record_pos=(0.354, 0.233), resolution=(1920, 1080)))
    if not battle: break
    touch(Template(r"tpl1714572485095.png", record_pos=(0.391, 0.101), resolution=(1920, 1080)))
    touch(Template(r"tpl1714572492801.png", record_pos=(-0.368, 0.063), resolution=(1920, 1080)))
    touch(Template(r"tpl1714572497611.png", record_pos=(0.346, 0.236), resolution=(1920, 1080)))
    touch(Template(r"tpl1714572503080.png", record_pos=(0.341, 0.233), resolution=(1920, 1080)))
    while not exists(Template(r"tpl1714572607979.png", record_pos=(-0.158, 0.194), resolution=(1920, 1080))):
        sleep(1)
    touch(Template(r"tpl1714572610405.png", record_pos=(-0.159, 0.195), resolution=(1920, 1080)))
touch(Template(r"tpl1714582031337.png", record_pos=(0.462, -0.253), resolution=(1920, 1080)))
sleep(3)
touch(Template(r"tpl1714573801882.png", record_pos=(0.29, -0.251), resolution=(1920, 1080)))
while exists(Template(r"tpl1714573812821.png", record_pos=(-0.308, 0.169), resolution=(1920, 1080))):
    touch(Template(r"tpl1714573807035.png", record_pos=(-0.309, 0.17), resolution=(1920, 1080)))
touch(Template(r"tpl1714573827995.png", record_pos=(-0.189, -0.131), resolution=(1920, 1080)))
touch(Template(r"tpl1714578350384.png", record_pos=(-0.001, 0.196), resolution=(1920, 1080)))
sleep(2)
touch(Template(r"tpl1714573833739.png", record_pos=(0.462, -0.253), resolution=(1920, 1080)))
touch(Template(r"tpl1714579277821.png", record_pos=(0.183, -0.252), resolution=(1920, 1080)))
touch(Template(r"tpl1714579283343.png", record_pos=(-0.456, -0.116), resolution=(1920, 1080)))
if exists(Template(r"tpl1714579296719.png", record_pos=(0.332, 0.245), resolution=(1920, 1080))):
    touch(Template(r"tpl1714579305050.png", record_pos=(0.341, 0.245), resolution=(1920, 1080)))
sleep(3)
touch(Template(r"tpl1714579321040.png", record_pos=(-0.455, -0.19), resolution=(1920, 1080)))
sleep(3)
if exists(Template(r"tpl1714582489696.png", record_pos=(0.177, 0.241), resolution=(1920, 1080))):
    touch(Template(r"tpl1714582489696.png", record_pos=(0.177, 0.241), resolution=(1920, 1080)))
    touch(Template(r"tpl1714578350384.png", record_pos=(-0.001, 0.196), resolution=(1920, 1080)))
    sleep(2)

touch(Template(r"tpl1714579326813.png", record_pos=(0.463, -0.255), resolution=(1920, 1080)))


    
    
