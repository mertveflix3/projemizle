import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import subprocess
import math
from threading import Thread

try:
    subprocess.call("chmod +x ./geckodriver", shell=True)
except:
    pass
    

def suretosn(sure):
    saniye=0
    lsure=list(sure)
    kharf=len(lsure)
    for i in range(1,kharf+1):
        if(i%3!=0):
            saniye+=int(lsure[kharf-(i)])*(math.pow(10,(i%3-1)))*(math.pow(60,(i/3)))
    return int(saniye)

def izlet(link):
    izletth = Thread(target=izlet2,args=(link,))
    izletth.start()

def izlet2(link):
    while True:
        print ("Baslatiliyor")
        options = Options()
        options.headless = True
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', 'en-US, en')
        driver = webdriver.Firefox(firefox_profile=profile,options=options,executable_path="./geckodriver")
        driver.get(link)
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "movie_player")))
        dakikaelement= WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ytp-time-duration")))
        sure = dakikaelement.get_attribute('innerHTML')
        kacsaniye = suretosn(sure)
        print kacsaniye


        simdizamanelement = driver.find_element_by_class_name("ytp-time-current")

        
        time.sleep(10)
        simdizaman = simdizamanelement.get_attribute('innerHTML')
        driver.save_screenshot('screen1.png')
        
        if(simdizaman=="0:00"):
            try:
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                element.click()
            except Exception as e:
                print(e)
                driver.quit()
                continue
            
        print kacsaniye," Saniye Bekleniyor"
        driver.save_screenshot('screen2.png')
        time.sleep(kacsaniye)


        driver.save_screenshot('screen3.png')
        print("Screen Shot Alindi")
        break
    driver.quit()

