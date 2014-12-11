#!/user/bin/env python
#coding=utf-8
import urllib
import urllib2
import sys
import cookielib
import time
import io,gzip
import os

class url_request():
#初始化cookie opener headlers,默认headlers为android Nexus 4
    def __init__(self):
        """Constructor"""
        self.cookie_jar = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        self.headlers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
     #test_LBSLocateCity        
    def send_post(self,url):
        reload(sys)
        sys.setdefaultencoding('utf8')
        #设置请求参数
        parameters = {'CountryName':'xx',
                      'ProvinceName':'xx',
                      'L1CityName':'xx',
                      'L2CityName':'x',
                      'TownName':'xx',
                      'Longitude':'xx',
                      'Latitude':'xx',
                      'Language':'xx'
                      }
        #格式化
        mydata = urllib.urlencode(parameters)
        mydata = mydata.encode('utf-8')
        #拼接请求体
        req = urllib2.Request(url,data=mydata)
        #增加header
        self.set_add_headers(req)
        #请求
        reqp = self.opener.open(req)
        #打印返回值
        print str(reqp.code) #200、404、503等
        print str(reqp.msg) #对应200、404、503，成功、找不到页面等等
        print '%s' % reqp.readlines()

        #buf = io.BytesIO(reqp.read())
        #f = gzip.GzipFile(fileobj=buf)
        #data2 = f.read().decode('utf-8')
        #print "response:%s" % data2
   
        
    def set_add_headers(self,req):
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
        req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19')
        req.add_header('Accept-Encoding', 'gzip,deflate,sdch')
        req.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6')
   

if __name__=='__main__':
    myRequest = url_request()
    #urls = open('sourceUrl.txt','r')
    #fileSuc = open('urlSuc.txt','w')
    #fileFai = open('urlFai.txt','w')
    #urls.seek(0)
    #post
    #myRequest.sendPost(urls,fileSuc,fileFai)
    #get
    #myRequest.send_get(urls,fileSuc,fileFai)
    #url = ' '
    URL = ' '
    #myRequest.test_Send_Post(url,fileFai)
    #调用send_post方法，传入URL
    myRequest.send_post(URL)
    #myRequest.closeFile()
