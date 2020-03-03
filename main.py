import time
from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

def runny():
    driver=webdriver.Chrome()
    driver.get('http://fast.com/')
    time.sleep(10)
    #resp = driver.find_element_by_xpath('//div[@class="speed-results-container succeeded"]/div').text
    #print(resp)
    filename = (strftime("%Y-%m-%d %H%M%S", gmtime()))
    element=driver.find_element_by_id('speed-value')
    print(element.text, filename)
    speed=[]
    speed.append(element.text)
    #df=pd.DataFrame({'Network speed is' :[speed[0]],'Time' :[filename]})
    df=pd.DataFrame({'Network speed is' :[speed[0]],'Time' :[filename]})
    df.to_csv('hourly_speed.csv', index=False, encoding='utf-8')
    with open('hourly_speed.csv', 'a+') as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write('\n')
            file_object.write(speed[0])
            file_object.write(',')
            file_object.write(filename)
           # df=pd.DataFrame({'Network speed is' :[speed[0]],'Time' :[filename]})
            
            #file_object.write({'Network speed is' :[speed[0]],'Time' :[filename]})


    
    driver.close()

if __name__ == "__main__":
    runny()