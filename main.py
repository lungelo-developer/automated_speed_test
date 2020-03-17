import time
import os
import datetime
from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

save_path = 'C:/speed/'
file_name = 'hourly_speed.csv'

complete_path = os.path.join(save_path, file_name)
def runny():
    driver=webdriver.Chrome()
    driver.get('http://fast.com/')
    time.sleep(20)
    now = datetime.datetime.now()
    current_date = str(now)
    element=driver.find_element_by_id('speed-value')
    units=driver.find_element_by_id('speed-units')
    print(element.text,units.text, current_date)
    speed=[]
    speed.append(element.text)
    unit=[]
    unit.append(units.text)
    
    with open(complete_path, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
            file_object.write(speed[0])
            file_object.write(',')
            file_object.write(unit[0])
            file_object.write(',')
            file_object.write(current_date)

        
    driver.close()

if __name__ == "__main__":
    runny()