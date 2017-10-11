#coding:utf-8

import requests

from bs4 import BeautifulSoup as BS





url='http://www.chemeng.tsinghua.edu.cn/podcast.do?method=staff&cid=3'
r=requests.get(url)
soup=BS(r.text,'lxml')



title=[]
i=0

for link in soup.select('td[id*="top"]',limit=7):
    title.append(link.get_text(strip=True))

for link in soup.select('table[class*="teachName"]',limit=7):#当limit=6,退休老师除外

    #print link
    print '\n',title[i],u'如下\n'
    i+=1
    soup=BS(unicode(link),'lxml')

    for link in soup.select('a[href*="podcast.do?method=content&id="]'):

        print link.get_text(strip=True),'http://www.chemeng.tsinghua.edu.cn/%s' %link.attrs['href']


