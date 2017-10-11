import requests
import re
from bs4 import BeautifulSoup as bs
def get_ua():
    r=requests.get('http://www.useragentstring.com/pages/useragentstring.php?typ=Mobile%20Browser')
    soup=bs(r.text,'lxml')
    ua_list=[]
    for each in soup.find_all('a',href=re.compile("index"),limit=100):
        if 'href' in each.attrs:
            ua_list.append(each.get_text())
    return ua_list


print get_ua()
