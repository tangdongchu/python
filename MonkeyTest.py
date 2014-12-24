#coding=utf-8

'''
Create on 2014-12-24
python 2.7 for window
@auther: tangdongchu
'''
import os
import sys
import time

class monkeyTest():
    
    def __init__(self):
        """ init """
            
    #monkey命令，packageName包名，interval间隔时间单位ms ，frequency执行次数
    def monkeyApp(self,packageName,interval,frequency):
        try:
            os.popen("adb shell monkey -p %s --throttle %s --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v %s >e:\monkeylog\monkeyScreenLog.log" % (packageName, interval, frequency),'r')
        except Exception,e:
            print e

    #导出日志
    def copyErrorLog(self):
        try:
            anr = "E:\\monkeylog\\anr"
            if not os.path.isdir(anr):
                os.makedirs(anr)
            dontpanic = "E:\\monkeylog\\dontpanic"
            if not os.path.isdir(dontpanic):
                os.makedirs(dontpanic)
            tombstones = "E:\\monkeylog\\tombstones"
            if not os.path.isdir(tombstones):
                os.makedirs(tombstones)              
            bugreports = "E:\\monkeylog\\bugreports"
            if not os.path.isdir(bugreports):
                os.makedirs(bugreports)                                            
            os.popen("adb pull /data/anr  E://monkeylog//anr",'r')
            os.popen("adb pull /data/dontpanic  E://monkeylog//dontpanic",'r')
            os.popen("adb pull /data/tombstones  E://monkeylog//tombstones",'r')
            os.popen("adb pull /data/data/com.android.shell/files/bugreports  E://monkeylog//bugreports",'r')
        except Exception,e:
            print e            
           
def main():
    print """"""
    
    
if __name__=="__main__":
    
    packageName = 'ctrip.android.view'  
    myApp = monkeyTest()   
    myApp.monkeyApp(packageName,500,100)
    #判断是否执行完成，执行完成后导出日志
    for i in range(1, 1000000):
        monkeylog = open('E:\monkeylog\monkeyScreenLog.log')
        try:
            temp = monkeylog.read( )
        finally:
            monkeylog.close( )
        if temp.count('Monkey finished')>0:
            myApp.copyErrorLog()
            break
        else:
            time.sleep(2)