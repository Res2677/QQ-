import adb
import pixel
import sys
import excel
import time
path = sys.argv[0].replace('C:','c:').strip('venv/run.py')
#print(path)
tupath = sys.argv[0].replace('C:','c:').strip('venv/run.py').replace('/','//')

adbpath = 'd://Microvirt//MEmu//adb.exe'
MEmu = 'd://Microvirt//MEmu//MEmu.exe'
file = '结果统计.xls'
excel.cj(file)

#adb.startMN(adbpath)
#time.sleep(30)
#adb.startQQ(adbpath)
#time.sleep(10)
#

while 1:
    adb.jieping(adbpath,path+'/liebiao.png')
    coor = pixel.clock_hb(tupath+'//liebiao.png','hongbao.png')
    print(coor)
    if coor != None:
        adb.clock(coor[0],coor[1])
        time.sleep(2)
        adb.jieping(adbpath,path+'/liaotian.png')
        coor = pixel.clock_gx(tupath+'//liaotian.png','gong.png')
        print (coor)
        adb.clock(coor[0],coor[1])
        time.sleep(3)
        adb.jieping(adbpath,path+'/money.png')
        mon = pixel.get_money(tupath+'//money.png','money.png')
        excel.set_xb_data(file,mon)
        adb.back1(adbpath)
        adb.back2(adbpath)
    else:
        pass

    time.sleep(2)
# coor = pixel.clock_gx(tupath+'//liaotian.png','gong.png')
# print(coor)





