import time
import os
from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

save_path = 'C:/'
file_name = 'hourly_speed.csv'

complete_path = os.path.join(save_path, file_name)
def runny():
    driver=webdriver.Chrome()
    driver.get('http://fast.com/')
    time.sleep(10)
   
    datetime = (strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    element=driver.find_element_by_id('speed-value')
    print(element.text, datetime)
    speed=[]
    speed.append(element.text)
    
    with open(complete_path, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        file_object.write(speed[0])
        file_object.write(',')
        file_object.write(datetime)

    driver.close()

if __name__ == "__main__":
    runny()