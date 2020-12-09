#author:sethome
#Email:sethomebyset@foxmail.com
#Start_time: 2020/11/19

Keyword = "life"

#excel operate module
import xlrd,xlwt
from xlutils.copy import copy
#browser auto operate module
import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
#warning:different environment need difference setup 
browser = webdriver.Chrome()

#pleace enter your search paper web,now only support springer
targetWeb = "https://kns.cnki.net/kns8/defaultresult/index"

#openTheXls
paperList = xlwt.Workbook(encoding = 'utf-8')
paperInfo = paperList.add_sheet("paperList")
print("OK")

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

def selectXpathAndInput(Xpath,text):
  element = browser.find_element_by_xpath(Xpath)
  element.send_keys(text)
  return

selectXpathAndInput("/html/body/div[4]/div/div[2]/div[1]/input[1]",Keyword)
selectXpathAndClick("/html/body/div[4]/div/div[2]/div[1]/input[2]")
#the program start
row = 0
for i in range (0,10):#get 10 page of the sreach site
  for num in range (1,20):#tyr to open each paper information site,and get key information
    try:
      #get the title
      paperInfo.write(row,0,selectCsspathAndReturnElementName("#gridTable > table > tbody > tr:nth-child(" + str(num) + ") > td.name > a"))
      #get the summary
      
      #get the jounal
      paperInfo.write(row,2,selectCsspathAndReturnElementName("#gridTable > table > tbody > tr:nth-child(" + str(num) + ") > td.source > a"))
      #get the time
      paperInfo.write(row,3,selectCsspathAndReturnElementName("#gridTable > table > tbody > tr:nth-child(" + str(num) + ") > td.date"))
      
      paperList.save('paperList.xls')#save flie
    except:
      print("open page err!")

    row = row + 1
  #click next page
  selectCsspathAndCLick("#PageNext")
  time.sleep(2)

browser.close()
browser.quit() 