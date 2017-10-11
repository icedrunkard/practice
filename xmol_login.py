# -*- coding=UTF-8 -*-
from selenium import webdriver
import pickle
import requests
def get_cookie_from_network():
    
    url_login = 'http://www.x-mol.com/login/' 
    driver = webdriver.PhantomJS(executable_path='C:/Python27/phantomjs-2.1.1-windows/phantomjs')
    driver.get(url_login)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('happy-267@163.com') # 改成你的微博账号
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('6times9is54') # 改成你的微博密码

    driver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/div/input').click() # 点击登录
    print driver.current_url
    # 获得 cookie信息
    cookie_list = driver.get_cookies()
    #print cookie_list

    cookie_dict = {}
    for cookie in cookie_list:
        #写入文件
        f = open(cookie['name']+'.xmol','w')
        pickle.dump(cookie, f)
        f.close()

        if cookie.has_key('name') and cookie.has_key('value'):
            cookie_dict[cookie['name']] = cookie['value']

    return cookie_dict

get_cookie_from_network()
