
import re
from bs4 import BeautifulSoup
import requests
import xmol_login


#cookies=xmol_login.get_cookie_from_network()
#x=requests.get('http://www.x-mol.com/university/faculty/31452',cookies=cookies)
x=requests.get('http://www.amorbond.com')
soup1=x.text
soup2=x.content
p=BeautifulSoup(soup1,'lxml')

print type(p),type(soup1),type(soup2)
print p.encoding

#for q in p.select('li[title*="@"]')
   # print q.get_text(strip=True)
