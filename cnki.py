# -*- coding=UTF-8 -*-

import requests
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from lxml import etree

import time
from selenium import webdriver
import pickle
import requests

from bs4 import BeautifulSoup
import urllib2
    
url_login = 'http://www.cnki.net' 
driver = webdriver.PhantomJS(executable_path='C:/Python27/phantomjs-2.1.1-windows/phantomjs')

driver.get(url_login)


    
driver.find_element_by_xpath('//*[@id="txt_1_value1"]').send_keys('qinghua')



driver.find_element_by_xpath('//*[@id="btnSearch"]').click()

driver.implicitly_wait(30)

urlnow=driver.current_url

driver.switch_to_frame('iframeResult')
print '1',urlnow

print driver.find_elements_by_xpath('//*[@id="ctl00"]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/a')


######   get   cookies   ########
cookie_list = driver.get_cookies()

cookie_dict = {}
for cookie in cookie_list:
        
    if cookie.has_key('name') and cookie.has_key('value'):
            cookie_dict[cookie['name']] = cookie['value']



#response=requests.get(urlnow,)#cookies=cookie_dict)
#print response.url
#soup = BeautifulSoup(response.text,'lxml')

#iframexx = soup.find_all('iframe')
#for iframe in iframexx:
    #if 'src' in iframe.attrs:
        #print '2',iframe.attrs['src']






driver.quit()    








