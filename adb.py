import os
import time
adb = 'd://Microvirt//MEmu//adb.exe'
MEmu = 'd://Microvirt//MEmu//MEmu.exe'

def startMN(adb):
    cmd = MEmu
    os.popen(cmd)
    checmd = adb + ' devices'
    mm = os.popen(checmd).read()
    if '127.0.0.1' in mm:
        print('启动成功')
    # else:
    #     print('启动失败')

#startMN(adb)

def startQQ(adb):
    cmd = adb + ' shell am start -n com.tencent.mobileqq/com.tencent.mobileqq.activity.SplashActivity'
    os.popen(cmd)

def jieping(adb,out):
    jie = adb + ' shell /system/bin/screencap -p /sdcard/screenshot.png'
    copy = adb + ' pull /sdcard/screenshot.png ' + out
    os.popen(jie)
    time.sleep(1.5)
    os.popen(copy)
    time.sleep(1)
def back1(adb):
    cmd = adb +' shell input touchscreen tap 45 77'
    os.popen(cmd)

def back2(adb):
    cmd = adb +' shell input touchscreen tap 387 1132'
    os.popen(cmd)

def clock(x,y):
    cmd = adb +' shell input touchscreen tap ' +str(x)+' '+str(y)
    print(cmd)
    os.popen(cmd)
#jieping(adb)

def slider():
    cmd = adb +' shell input swipe 384 143 384 1200'
    os.popen(cmd)
#back2(adb)