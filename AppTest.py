#coding=utf-8

'''
Created on 2014-12-9
python 2.7 for window
@auther: tangdongchu
'''
import os
import re
import time
import sys
import threading

class appTest():
    
    def __init__(self):
        """ init """
        
    #检查是否连接
    def connectDevice(self):
        try:
            devices = os.popen('adb devices').read()
            device = re.findall('device', devices)
            for i in range(1, 10 + 1):
                if device.__len__() < 2:
                   print 'no device !'
                   print 'wait for connect'
                   time.sleep(5)
                   if i == 10:
                      print 'exit'
                      sys.exit(1) 
            else:
                print 'connect success !!'
        except Exception,e:
            print e
        except IOError,i:
            print i
            
    #启动应用
    def startApp(self,packageName):
        try:
            startout = os.popen('adb shell am start -W -n %s' % packageName).read()
            print startout
        except Exception,e:
            print 'no phone connect'
            print e
            
    #卸载应用
    def uninstallApp(self,packageName):
        try:
            os.popen("adb uninstall %s" + packageName)
        except Exception,e:
            print e
            
    #清除应用缓存
    def clearAppCache(self,packname):
        try:
            os.popen("adb shell pm clear %s" + packname)
        except Exception,e:
            print e            
           
    #获取当前终端中的进程ID
    def getPID(self):
        try:
            for PS in os.popen('adb shell ps','r').readlines():
                reList = re.sub('PS:','',PS)
                reList = reList.replace('\n','')
                result = re.search('ctrip.android.view', reList)
                #print reList
                if result != None :
                    tmp=reList.split().pop(0)
                    PID="100"+str(tmp[4:])
                    #print PID
                    return PID
                    break
        except Exception,e:
            print e    
                   
    #获取应用发送流量
    def getSendData(self):
        myApp = appTest()
        PID=myApp.getPID()
        try:
            for SendData in os.popen('adb shell cat /proc/uid_stat/%s/tcp_snd' % PID,'r').readlines():
                tmp = re.sub('SendData:','',SendData)
                tmp2=float(tmp)/1024.00
                data='%.2f'%  tmp2
                print "Total Send Data %s kb" % data
                fileFlowinfo.write("应用发送流量")
                fileFlowinfo.write(str(data))
                fileFlowinfo.write("kb")
                fileFlowinfo.write("\n")
        except Exception,e:
            print e            
    
    #获取应用接收流量
    def getReceiveData(self):
        myApp = appTest()
        PID=myApp.getPID()
        try:
            for ReceiveData in os.popen('adb shell cat /proc/uid_stat/%s/tcp_rcv' % PID,'r').readlines():
                tmp = re.sub('ReceiveData:','',ReceiveData)
                tmp2=float(tmp)/1024.00
                data='%.2f'%  tmp2
                print "Total Receive Data %s kb" % data
                fileFlowinfo.write("应用接收流量")
                fileFlowinfo.write(str(data))
                fileFlowinfo.write("kb")
                fileFlowinfo.write("\n")
        except Exception,e:
            print e    
            
    #获取android packageName列表
    def getCurrentPackages(self):
        try:
            for package in os.popen('adb shell pm list packages','r').readlines():
                reList = re.sub('package:','',package)
                reList = reList.replace('\n','')
                result = re.search('ctrip.android.view', reList)
                str(reList[4:6])
        except Exception,e:
            print e

    #获取当前电量
    def getCurrentBattery(self):
        try:
            for Battery in os.popen('adb shell dumpsys battery','r').readlines():
                reList = re.sub('Battery:','',Battery)
                reList = reList.replace('\n','')
                result = re.search('level', reList)
                if result != None :
                    List = reList.split()
                    level=List.pop()#删除第i个元素，并返回这个元素。若调用pop()则删除最后一个元素
                    print "battery level " + level + "%"
                    return level
                    break
        except Exception,e:
            print e

    #获取apk占用内存
    def getDumpsysMeminfo(self,adbShellMem,searchWord,fileMeminfo):
        try:
            for line in os.popen('%s' % adbShellMem).readlines():
                #print '%s' % line
                if re.search('%s' % searchWord, line):
                    print 'Meminfo:%s' % line
                    result = re.findall('[0-9]{1,9} ', line)
                    Headsize = result[-2]
                    HeadAlloc = result[-1]
                    size = 'headSize:%s ' % Headsize
                    alloc = 'headAlloc:%s' % HeadAlloc
                    log = str(self.getCurrentTime()) + str(' ') + size + alloc + '\n'
                    print log
                    fileMeminfo.write(log)
                    
        except Exception,e:
            print e
        except IOError,e:
            print e
    
    #获取apk占用cpu
    def getDumpsysCpuinfo(self,adbShellCpu,searchWord,fileCpuinfo):
        try:
            time.sleep(2)
            for line in os.popen('%s' % adbShellCpu).readlines():
                #print line
                if re.search('%s' % searchWord,line):
                    print 'Cpuinfo:%s' % line
                    result = re.findall('[/.0-9]{1,9}%', line)
                    if result:
                        cpu = 'cpu:%s ' % result[0]
                        userCpu = 'userCpu:%s' % result[1]
                        log = str(self.getCurrentTime()) +' '+ cpu + userCpu
                        print log
                        fileCpuinfo.write(log)
        except  Exception,e:
            print e
    
    #获取当前时间，用于计算应用启动时间
    def getCurrentTime(self):
        try:
            currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            #print currentTime
        except Exception,e:
            print e
        return currentTime
    
    def readTxt(self,fileName):
        try:
            print fileName
            readContent = open('%s' % fileName,'r')
            writeMeminfo = open('Meminfo.txt','w')
            readContent.seek(0)
            while 1:
                line = readContent.readline()
                if not line:
                    break
                else:
                    print line
                    if(re.search('TOTAL', line)):
                        print 'total:' + line
                        #content = re.sub(' ', '.', line)
                        result = re.findall('[0-9]{1,9} ', line)
                        #print 'start:'+ str(result.start(0))
                        #print 'end:' + str(result.end(0))
                        print 'result:%s' % result
                        print 'Head Size:%s' % result[-3]
                        print 'Heap allo:%s' % result[-2]
                        for number in result:
                            print 'size:%s \n' % (number)
                        
        except IOError,e:
            print e
            
    def getfileOjbect(self,fileName,mode):
        fileOjbect  = open('%s' % fileName,'%s' % mode)
        return fileOjbect
def main():
    print """"""
    
    
if __name__=="__main__":
    #global variable 
    
    packageName = 'ctrip.android.view'
    startActivity = '/.home.CtripSplashActivity'
    packNameStartActivity = packageName + startActivity
    #fileMeminfo = open('meminfo.txt','w')
    #fileCpuinfo = open('cpuinfo.txt','w')
    fileFlowinfo = open('flowinfo.txt','w')
    filepackageinfo = open('packageinfo.txt','w')
    #meminfo = 'adb shell dumpsys meminfo ctrip.android.view'
    #cpufinfo = 'adb shell dumpsys cpuinfo'    
    myApp = appTest()
    #fileObject = myApp.getfileOjbect('meminfo.txt', 'w')
    #fileObject.write("log")

    myApp.getPID()
    myApp.getCurrentPackages()
    myApp.connectDevice()    
    myApp.startApp(packNameStartActivity)
    myApp.getSendData()
    myApp.getReceiveData()
    myApp.getCurrentBattery()
    fileFlowinfo.close()
    filepackageinfo.close()

    #myApp.getDumpinfo()  
    #myApp.getDumpsysMeminfo(meminfo,'TOTAL',fileMeminfo)
    #myApp.getDumpsysCpuinfo(cpufinfo,'ctrip.android.view',fileCpuinfo)
    #print myApp.getCurrentTime()