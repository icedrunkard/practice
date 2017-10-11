import requests
import json


proxyHost = "proxy.abuyun.com"
proxyPort = "9020"


proxyUser = "H264P9E9M949159D"
proxyPass = "1C6AED9CB122390C"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }

proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }
proxy_s=set()
url='http://www.xdaili.cn/ipagent/greatRecharge/getGreatIp?spiderId=a35de4b72d544e0e83dde76484ed8868&orderno=YZ20174292746c5tj8U&returnType=2&count={page}'
for i in range(1,40):
    
    s=requests.Session()
    resp=s.get(url.format(page=1000),proxies=proxies)
    result=json.loads(resp.text)
    print result.get('RESULT')
    for item in result.get('RESULT'):
        print item
        print item['ip'],item['port']
        proxy='http://{ip}:{port}'.format(ip=item['ip'],port=item['port'])
        proxy_s.add(proxy)

    s.close()
with open('proxy.json','a') as f:
    json.dumps(proxy_s,f)
print len(proxy_s)
