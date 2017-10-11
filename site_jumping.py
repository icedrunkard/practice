#-*- coding: UTF-8 -*-


from urllib2 import urlopen
from bs4 import BeautifulSoup
from lxml import etree
import requests


import xmol_login
cookies=xmol_login.get_cookie_from_network()



#html = requests.get('http://www.x-mol.com/university/china',cookies=cookies)#安徽大学~中科院页面
#html.cookies

s=requests.Session()
print s.get('http://www.x-mol.com/university/faculty/8510',cookies=cookies).text
print s.get('http://www.x-mol.com/university/faculty/31452',cookies=cookies).text


