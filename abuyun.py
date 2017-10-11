#-*- encoding:utf-8 -*-
import requests
def abuyun(url):
    
# 代理服务器
    proxyHost = "proxy.abuyun.com"
    proxyPort = "9020"

# 代理隧道验证信息
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

# 要访问的目标页面
    print proxyMeta
    response = requests.get(url, proxies=proxies)
    print response.text


abuyun("http://test.abuyun.com/proxy.php")
