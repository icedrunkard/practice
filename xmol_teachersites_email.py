#-*- coding: UTF-8 -*-


from urllib2 import urlopen
from bs4 import BeautifulSoup

from lxml import etree
import requests


import xmol_login
cookies=xmol_login.get_cookie_from_network()

html = urlopen('http://www.x-mol.com/university/china')          #安徽大学~中科院页面
xmol = BeautifulSoup(html, "lxml")                               #beautifulsoup解析成源码，赋值给过渡容器xmol
 

i=0
j=0
k=1
urls=[]                                                          #定义存储      各大学链接  的列表
htmls=[]                                                         #定义能存储   各大学老师页面源码  的列表
teachers=[]
teachersites=[]

filename1='chinateachers.txt'
filename2='chinateacherslink.txt'


for link in xmol.select("body ul ul a"):                          
  if 'href' in link.attrs:
    url='http://www.x-mol.com'+link.attrs['href']+'?all=1'        #得到安徽大学所有老师页面网址
    urls.append(url)                                              #安徽大学所有老师页面网址容器
    htmls.append(BeautifulSoup(urlopen(urls[i]),'lxml'))          #安徽大学所有老师页面  解析后的容器
    ii=i+1
    for link2 in htmls[i].select("body ul ul a"):                 
          if 'href' in link2.attrs:
            teacher=link2.attrs['href']                           
            teachersite='http://www.x-mol.com'+teacher            #得到安徽大学单个老师的页面
            teachers.append(teachersite)                          #安徽大学单个老师的页面网址的容器
            teachersites.append(BeautifulSoup(requests.get(teachers[j],cookies=cookies).text,'lxml'))#安徽大学单个老师的页面网址的容器
           
            for link3 in teachersites[j].select('li[title*="@"]'):
                l='['+str(k)+']'+'['+str(ii)+']'+link.get_text(strip=True)+'--'+link2.get_text(strip=True)+'--'+teachersite+'--'+link3.get_text(strip=True)+'\n'#unicode
                with open(filename1,'a') as file_object:
                    file_object.write(l.encode('utf-8'))            #unicode--->utf-8
                k+=1
            j+=1  
    i+=1
    print link.get_text(strip=True)

print k    
