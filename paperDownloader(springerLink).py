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
targetWeb = "https://link.springer.com/search?query=Activated+sludge+treatment"

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

def selectCsspathAndReturnElementName(Csspath):
  element = browser.find_element_by_css_selector(Csspath)
  return element.text

def selectCsspathAndReturnIncludeLink(Csspath):
  element = browser.find_element_by_css_selector(Csspath)
  return element.get_attribute("href")

def getPaperInformation_printToXls(writeRow):
  #get title 
  paperInfo.write(writeRow,0,selectCsspathAndReturnElementName(".c-article-title"))
  #get summary
  paperInfo.write(writeRow,1,selectCsspathAndReturnElementName(".c-article-info-details > a:nth-child(1) > i:nth-child(1)"))
  #get journal
  paperInfo.write(writeRow,2,selectCsspathAndReturnElementName("#Abs1-content > p:nth-child(1)"))
  #get downloadLink
  try:
    paperInfo.write(writeRow,3,selectCsspathAndReturnIncludeLink("#sidebar > aside:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)"))
  except:
    print("can't get download link")
  paperList.save('paperList.xls')

#the program start
row = 0
selectCsspathAndCLick("#results-only-access-checkbox")
selectCsspathAndCLick("#onetrust-accept-btn-handler")
for i in range (0,5):#get 5 page of the sreach site
  for num in range (1,20):#tyr to open each paper information site,and get key information
    try:
      time.sleep(5)
      selectCsspathAndCLick("#results-list > li:nth-child(" + str(num) + ") > h2:nth-child(3) > a:nth-child(1)")
      getPaperInformation_printToXls(row)
      browser.back()
    except:
      print("open page err!")
    row = row + 1
  #click next page
  selectNameAndCLick("next")
  time.sleep(5)

browser.close()
browser.quit() 