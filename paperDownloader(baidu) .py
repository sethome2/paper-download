#author:sethome
#Email:sethomebyset@foxmail.com
#Start_time: 2020/11/19

#excel operate module
import xlrd,xlwt
from xlutils.copy import copy
#browser auto operate module
import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
#warning:different environment need difference setup 
browser = webdriver.Firefox()
browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver", log_path="geckodriver.log")

#pleace enter your search paper web,now only support springer
targetWeb = "https://xueshu.baidu.com/s?wd=life&tn=SE_baiduxueshu_c1gjeupa&cl=3&ie=utf-8&bs=fuck&f=8&rsv_bp=1&rsv_sug2=0&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&rsv_spt=3"

#openTheXls
paperList = xlwt.Workbook(encoding = 'utf-8')
paperInfo = paperList.add_sheet("paperList")

#browser.implicitly_wait(25) #wait for browser open the web
browser.get(targetWeb)

#operate funtion
def selectXpathAndClick(Xpath):
  element = browser.find_element_by_xpath(Xpath)
  element.click()
  return element

def selectCsspathAndCLick(Csspath):
  element = browser.find_element_by_css_selector(Csspath)
  element.click()
  return element

def selectNameAndCLick(Name):
  element = browser.find_element("title",Name)
  element.click()
  return element

def selectXpathAndReturnElementName(Xpath):
  element = browser.find_element_by_xpath(Xpath)
  return element.text

def selectCsspathAndReturnElementName(Csspath):
  element = browser.find_element_by_css_selector(Csspath)
  return element.text

def selectCsspathAndReturnIncludeLink(Csspath):
  element = browser.find_element_by_css_selector(Csspath)
  return element.get_attribute("href")

#the program start
row = 0
for i in range (0,10):#get 10 page of the sreach site
  for num in range (4,14):#tyr to open each paper information site,and get key information
    try:
      time.sleep(1)
    
      #get the title
      paperInfo.write(row,0,selectXpathAndReturnElementName("/html/body/div[1]/div[4]/div[3]/div[2]/div/div[" + str(num) + "]/div[1]/h3/a"))
      #get the summary
      paperInfo.write(row,1,selectXpathAndReturnElementName("/html/body/div[1]/div[4]/div[3]/div[2]/div/div[" + str(num) + "]/div[1]/div[1]"))
      #get the jounal
      paperInfo.write(row,2,selectXpathAndReturnElementName("/html/body/div[1]/div[4]/div[3]/div[2]/div/div[" + str(num) + "]/div[1]/div[2]/span[2]/a"))
      
      paperList.save('paperList.xls')#save flie
    except:
      print("open page err!")

    row = row + 1
  #click next page
  selectXpathAndClick("/html/body/div[1]/div[4]/div[3]/p/a[8]")
  time.sleep(5)

browser.close()
browser.quit() 