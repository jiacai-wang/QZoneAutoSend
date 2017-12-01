# -*- coding: utf-8 -*-

#This is a Python program that automatically get the weather infomation and publish it to your QZone,
#With the great help of Selenium and PhantomJS.
#It works on my RaspberryPi.

#Coded by WC.
#I know nothing about LICENSE.Just do whatever you'd like to.
#But better not come to me for help. I know it works. I don't know why.

import time
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("started")
browser=webdriver.PhantomJS()
#change the "lat" and "lon" to your city.
#just visit m.weather.com.cn to see where you are.
browser.get('http://m.weather.com.cn/d/town/index?lat=xx.xxxxxx&lon=xxx.xxxxxx')
print("weather_page_now got")
city=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/a').get_attribute('innerHTML')
updatetime=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/time').get_attribute('innerHTML')
temp_now=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/h1/i').get_attribute('innerHTML')
weather_now=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/h2').get_attribute('innerHTML')
head0=city+" ("+updatetime+"):"
head1=u"当前天气:"+temp_now+u"° "+weather_now

browser.get('http://m.weather.com.cn/d/town/future?lat=xx.xxxxxx&lon=xxx.xxxxxx')
print("weather_page_future got")

day0=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[1]/div[1]/time').get_attribute('innerHTML')
temp0H=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[1]/div[2]/div[1]/div[1]').get_attribute('innerHTML')
temp0L=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[1]/div[2]/div[1]/div[3]').get_attribute('innerHTML').strip()
weather0=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[1]/div[2]/div[2]/span[2]').get_attribute('innerHTML').strip()
wind0=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[1]/div[2]/div[3]/span[2]').get_attribute('innerHTML').strip()
day1=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[2]/div[1]/time').get_attribute('innerHTML')
temp1H=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[2]/div[2]/div[1]/div[1]').get_attribute('innerHTML')
temp1L=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[2]/div[2]/div[1]/div[3]').get_attribute('innerHTML').strip()
weather1=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[2]/div[2]/div[2]/span[2]').get_attribute('innerHTML').strip()
wind1=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[2]/div[2]/div[3]/span[2]').get_attribute('innerHTML').strip()
day2=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[3]/div[1]/time').get_attribute('innerHTML')
temp2H=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[3]/div[2]/div[1]/div[1]').get_attribute('innerHTML')
temp2L=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[3]/div[2]/div[1]/div[3]').get_attribute('innerHTML').strip()
weather2=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[3]/div[2]/div[2]/span[2]').get_attribute('innerHTML').strip()
wind2=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[3]/div[2]/div[3]/span[2]').get_attribute('innerHTML').strip()
day3=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[4]/div[1]/time').get_attribute('innerHTML')
temp3H=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[4]/div[2]/div[1]/div[1]').get_attribute('innerHTML')
temp3L=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[4]/div[2]/div[1]/div[3]').get_attribute('innerHTML').strip()
weather3=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[4]/div[2]/div[2]/span[2]').get_attribute('innerHTML').strip()
wind3=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[4]/div[2]/div[3]/span[2]').get_attribute('innerHTML').strip()
day4=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[5]/div[1]/time').get_attribute('innerHTML')
temp4H=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[5]/div[2]/div[1]/div[1]').get_attribute('innerHTML')
temp4L=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[5]/div[2]/div[1]/div[3]').get_attribute('innerHTML').strip()
weather4=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[5]/div[2]/div[2]/span[2]').get_attribute('innerHTML').strip()
wind4=browser.find_element_by_xpath('//*[@id="container"]/article/ul/li[5]/div[2]/div[3]/span[2]').get_attribute('innerHTML').strip()

info0=(day0.ljust(10)+temp0H.rjust(4)+temp0L.replace(' ','').ljust(6)+weather0+" "+wind0).replace('&lt','').replace(';','')
info1=(day1.ljust(10)+temp1H.rjust(4)+temp1L.replace(' ','').ljust(6)+weather1+" "+wind1).replace('&lt','').replace(';','')
info2=(day2.ljust(10)+temp2H.rjust(4)+temp2L.replace(' ','').ljust(6)+weather2+" "+wind2).replace('&lt','').replace(';','')
info3=(day3.ljust(10)+temp3H.rjust(4)+temp3L.replace(' ','').ljust(6)+weather3+" "+wind3).replace('&lt','').replace(';','')
info4=(day4.ljust(10)+temp4H.rjust(4)+temp4L.replace(' ','').ljust(6)+weather4+" "+wind4).replace('&lt','').replace(';','')

browser.get('http://www.air-level.com/air/changchun/')
time.sleep(2)
aqi=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/span[1]').get_attribute('innerHTML')
aqi_time=browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div/span[2]').get_attribute('innerHTML')
head2=u"aqi指数："+aqi+"  "+aqi_time.split(' ')[1]

print head0
print head1
print head2
print info0
print info1
print info2
print info3
print info4

#following is to login and send weather info

browser.get('https://qzone.qq.com')
browser.switch_to_frame('login_frame')
browser.find_element_by_id('switcher_plogin').click()
browser.find_element_by_id('u').clear()
#replace QQ with your "QQnumber"
browser.find_element_by_id('u').send_keys(QQ)
browser.find_element_by_id('p').clear()
#replace Passwd as well
browser.find_element_by_id('p').send_keys(Passwd)
browser.find_element_by_id('login_button').click()
print("Login button clicked")
time.sleep(5)
browser.find_element_by_id('aIcenter').click()
time.sleep(5)
print("we are in "+ browser.title)
print("wait 10s to complete loading page")
time.sleep(10)

#for some reason if there are already some texts in the $1_content_content, which holds texts you'll send,
#then the $1_substitutor_content will be invisible and you can just modify your texts;
#but if not, which is usually the case, the $1_content_content will be invisible
#and you have to click on the $1_substitutor_content
#to make $1_content_content interactable so as to modify it

if(browser.find_element_by_id('$1_content_content').get_attribute('innerHTML')==""):
  browser.find_element_by_id('$1_substitutor_content').click()
  print("Now substitutor_content not displayed and content_content displayed")
  time.sleep(3)
else:
  print("content is previously set. trying to click it")
  browser.find_element_by_id('$1_content_content').click()
  time.sleep(2)
  browser.find_element_by_id('$1_content_content').clear()
  print("and now it is cleared")
  time.sleep(2)
browser.find_element_by_id('$1_content_content').click()
print("content clicked")
time.sleep(2)
print("trying to modify content")
browser.find_element_by_id('$1_content_content').send_keys(head0)
browser.find_element_by_id('$1_content_content').send_keys(Keys.ENTER)
browser.find_element_by_id('$1_content_content').send_keys(Keys.ENTER)
browser.find_element_by_id('$1_content_content').send_keys(head1)
browser.find_element_by_id('$1_content_content').send_keys(Keys.ENTER)
browser.find_element_by_id('$1_content_content').send_keys(head2)
browser.find_element_by_id('$1_content_content').send_keys(Keys.ENTER)
browser.find_element_by_id('$1_content_content').send_keys(info0)
browser.find_element_by_id('$1_content_content').send_keys(Keys.ENTER)
browser.find_element_by_id('$1_content_content').send_keys(info1)
browser.find_element_by_id('$1_content_content').send_keys(Keys.ENTER)
browser.find_element_by_id('$1_content_content').send_keys(info2)
browser.find_element_by_id('$1_content_content').send_keys(Keys.ENTER)
browser.find_element_by_id('$1_content_content').send_keys(info3)
browser.find_element_by_id('$1_content_content').send_keys(Keys.ENTER)
browser.find_element_by_id('$1_content_content').send_keys(info4)
browser.find_element_by_id('$1_content_content').send_keys(Keys.ENTER)
browser.find_element_by_id('$1_content_content').send_keys(Keys.ENTER)

browser.find_element_by_id('$1_content_content').send_keys('auto-sent from selenium on RaspberryPi')
browser.find_element_by_id('$1_content_content').send_keys(Keys.ENTER)
browser.find_element_by_id('$1_content_content').send_keys('--Coded by WC')
time.sleep(3)
print("content is now --* "+browser.find_element_by_id('$1_content_content').get_attribute('innerHTML')+" *--")
time.sleep(3)
print("trying to CTRL+Enter to send")
browser.find_element_by_id('$1_content_content').send_keys(Keys.CONTROL,Keys.ENTER)
print("it should have been sent")
time.sleep(3)

print("Done!!!")
browser.quit()
