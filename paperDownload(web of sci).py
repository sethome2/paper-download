
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
targetWeb = "http://apps.webofknowledge.com/summary.do?locale=zh_CN&errorKey=&viewType=summary&product=WOS&search_mode=GeneralSearch&qid=1&SID=6EMbPCCNbKabQj64xiQ"

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
  for num in range (1,10):#tyr to open each paper information site,and get key information
    
    #get the title
    paperInfo.write(row,0,selectXpathAndReturnElementName("/html/body/div[1]/div[26]/div[2]/div/div/div/div[2]/div[3]/div[5]/form[2]/div/div[1]/div/span/div[2]/div[" + str(num) + "]/div[3]/div/div[1]/div/a/value"))
    #get the 
    paperInfo.write(row,2,selectXpathAndReturnElementName("/html/body/div[1]/div[26]/div[2]/div/div/div/div[2]/div[3]/div[5]/form[2]/div/div[1]/div/span/div[2]/div[" + str(num) + "]/div[3]/div/div[3]/span[2]/a/span/value"))
    
    paperList.save('paperList.xls')#save flie
    row = row + 1
  #click next page
  selectXpathAndClick("/html/body/div[1]/div[26]/div[2]/div/div/div/div[2]/div[4]/div/div/div[3]/div/form/nav/table/tbody/tr/td[3]/a")
  time.sleep(3)

browser.close()
browser.quit() 