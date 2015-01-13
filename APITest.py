#!/user/bin/env python
#coding=utf-8
import requests
import json

class url_request():
    def __init__(self):
            """ init """    

if __name__=='__main__':

    #get类型
    #r = requests.get('https://github.com/timeline.json')
    #post类型
    #r = requests.post("http://httpbin.org/post")
    #put类型
    #r = requests.put("http://httpbin.org/put")
    #delete类型
    #r = requests.delete("http://httpbin.org/delete")
    #head类型
    #r = requests.head("http://httpbin.org/get")
    #options类型
    #r = requests.options("http://httpbin.org/get")
    #打印返回值，也可以用r.text
    #print r.content
    
    #URL传递参数，示例为http://m.ctrip.com/webapp/tourvisa/visa_list?salecityid=2&keyword=日本
    #payload = {'keyword': '日本', 'salecityid': '2'}
    #r = requests.get("http://m.ctrip.com/webapp/tourvisa/visa_list", params=payload) 
    #print r.url
    
    #json处理
    #r = requests.get('https://github.com/timeline.json')
    #print r.json()
    
    #定制请求头
    #url = 'http://m.ctrip.com'
    #headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
    #r = requests.post(url, headers=headers)
    
    '''
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    '''
    
    #响应状态码
    #r = requests.get('http://httpbin.org/get')
    #print r.status_code
    
    #响应头
    #r = requests.get('http://m.ctrip.com')
    #print r.headers
    #print r.headers['Content-Type']
    #print r.headers.get('content-type')
    
    #Cookies
    #url = 'http://example.com/some/cookie/setting/url'
    #r = requests.get(url)
    #r.cookies['example_cookie_name']    读取cookies
    
    #url = 'http://httpbin.org/cookies'
    #cookies = dict(cookies_are='working')
    #r = requests.get(url, cookies=cookies) 发送cookies
    #print r.text    
    
    
    #复杂post请求
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
    payload = {'CountryName':'中国',
               'ProvinceName':'陕西省',
               'L1CityName':'汉中',
               'L2CityName':'城固',
               'TownName':'',
               'Longitude':'107.33393',
               'Latitude':'33.157131',
               'Language':'CN'
               }
    r = requests.post("http://ws.mobile.uat.qa.nt.ctripcorp.com/CityLocation/json/LBSLocateCity",headers=headers,data=payload)
    #r.encoding = 'utf-8'
    data=r.json()
    print r.text
    if r.status_code!=200:
        print "LBSLocateCity API Error " + str(r.status_code)
    print data['CityEntities'][0]['CityID']
    print data['ResponseStatus']['Ack']