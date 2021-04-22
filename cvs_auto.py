# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:55:38 2021

@author: 14052
"""

#Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


#birthday = input("Enter your birthday -- Example: 02231996 -- : ")
zipc = "73071"
age = '27'
fname = "Chris"
lname = "Ezzard"
url = 'https://www.cvs.com/immunizations/covid-19-vaccine?icid=cvs-home-hero1-link2-coronavirus-vaccinehttps://www.cvs.com/immunizations/covid-19-vaccine?icid=cvs-home-hero1-link2-coronavirus-vaccine'

driver = webdriver.Chrome("C:/Users/14052/Desktop/Chrome_Driver/chromedriver.exe")
driver.get(url)

driver.maximize_window()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="California"]'))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="vaccineinfo-CA"]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[3]/div/p[2]/a'))).click()

question1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="questionnaire"]/fieldset/section/div[3]/fieldset/div[2]/div[2]/label'
))).click()

question2 =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="questionnaire"]/fieldset/section/div[4]/fieldset/div[2]/div[2]/label'
))).click()

question3 =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="questionnaire"]/fieldset/section/div[5]/fieldset/div[2]/div[2]/label'
))).click()

submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[3]/button')))
submit.click()
# handle popup
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="acsMainInvite"]/div/a[1]'))).click()
except:
    TimeoutError
finally:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="generic"]/section/div[2]/div/div/div[1]/label'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div[3]/button'))).click()
#drop down menus
drpDwn =WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="jurisdiction"]')))
sel = Select(drpDwn)
sel.select_by_visible_text("California")

#fill form
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div[3]/button'))).click()
age_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="q1_0"]')))
age_in.clear()
age_in.send_keys(age)
#handle pop up
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="acsMainInvite"]/div/a[1]'))).click()
except:
    TimeoutError
finally:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="generic"]/fieldset/section/div[3]/div/div/div[2]/label'))).click()
    checkbox = driver.find_element_by_xpath('//*[@type = "checkbox"]')
    checkbox.click()
#submit
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div[3]/button'))).click()
#start schedule
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div[3]/button'))).click()

zip_code = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="address"]')))
zip_code.send_keys(zipc)




#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,''))).click()
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,''))).click()

#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ''))).click()
