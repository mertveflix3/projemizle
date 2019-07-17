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
    print ("Baslatiliyor")
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options,executable_path="./geckodriver")
    driver.get(link)
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "movie_player")))
    dakikaelement= WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ytp-time-duration")))
    sure = dakikaelement.get_attribute('innerHTML')
    kacsaniye = suretosn(sure)
    print kacsaniye


    simdizamanelement = driver.find_element_by_class_name("ytp-time-current")


    time.sleep(10)
    simdizaman = simdizamanelement.get_attribute('innerHTML')
    
    if(simdizaman=="0:00"):
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            element.click()
        except:
            driver.execute_script('document.getElementById("movie_player").click()')
        
    print kacsaniye," Saniye Bekleniyor"
    time.sleep(kacsaniye)


    driver.save_screenshot('screen2.png')
    print("Screen Shot Alindi")
    driver.close()

