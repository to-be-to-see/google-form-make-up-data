
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random


options = Options()
options.add_argument("--start-maximized")                       # Window maximized to load login btn in home page

driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
q1 = ['//*[@id="i6"]/div[3]/div', '//*[@id="i9"]/div[3]/div', '//*[@id="i12"]/div[3]/div']
q2 = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div']
q3 = ['//*[@id="i25"]/div[3]/div', '//*[@id="i28"]/div[3]/div']
q4 = ['//*[@id="i36"]/div[3]/div', '//*[@id="i39"]/div[3]/div']
q5 = ['//*[@id="i47"]/div[3]/div', '//*[@id="i50"]/div[3]/div']
q6 = ['//*[@id="i58"]/div[3]/div', '//*[@id="i61"]/div[3]/div']
q7 = ['//*[@id="i69"]/div[3]/div', '//*[@id="i72"]/div[3]/div']
q8 = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[3]/div/span/div/label[1]/div[2]/div/div/div[3]/div', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[3]/div/span/div/label[2]/div[2]/div/div/div[3]/div', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[3]/div/span/div/label[3]/div[2]/div/div/div[3]/div', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[3]/div/span/div/label[4]/div[2]/div/div/div[3]/div', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[3]/div/span/div/label[5]/div[2]/div/div/div[3]/div', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[3]/div/span/div/label[6]/div[2]/div/div/div[3]/div', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[3]/div/span/div/label[7]/div[2]/div/div/div[3]/div', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[3]/div/span/div/label[8]/div[2]/div/div/div[3]/div']


# set weighting of each choice

#q1a, q1b, q1c = 0,0,0
q2a, q2b, q2c, q2d = 1,2  ,3,4
q3a, q3b = 1,9
q4a, q4b = 1,9
q5a, q5b = 1,9
q6a, q6b = 1,9
q7a, q7b = 1,9
q8a, q8b, q8c, q8d, q8e, q8f, q8g = 1,2,3,4,  0,0,0


for count in range(100):
    q2_opt, q3_opt, q4_opt, q5_opt, q6_opt, q7_opt, q8_opt = 10,10,10,10,  10,10,10
    if q2a != 0:
        q2a -= 1
        q2_opt = 0
    elif q2b != 0:
        q2b -= 1
        q2_opt = 1
    elif q2c != 0:
        q2c -= 1
        q2_opt = 2
    elif q2d != 0:
        q2d -= 1
        q2_opt = 3


    if q3a != 0:
        q3a -= 1
        q3_opt = 0
    elif q3b != 0:
        q3b -= 1
        q3_opt = 1


    if q4a != 0:
        q4a -= 1
        q4_opt = 0
    elif q4b != 0:
        q4b -= 1
        q4_opt = 1


    if q5a != 0:
        q5a -= 1
        q5_opt = 0
    elif q5b != 0:
        q5b -= 1
        q5_opt = 1


    if q6a != 0:
        q6a -= 1
        q6_opt = 0
    elif q6b != 0:
        q6b -= 1
        q6_opt = 1


    if q7a != 0:
        q7a -= 1
        q7_opt = 0
    elif q7b != 0:
        q7b -= 1
        q7_opt = 1


    if q8a != 0:
        q8a -= 1
        q8_opt = 0
    elif q8b != 0:
        q8b -= 1
        q8_opt = 1
    elif q8c != 0:
        q8c -= 1
        q8_opt = 2
    elif q8d != 0:
        q8d -= 1
        q8_opt = 3
    elif q8e != 0:
        q8e -= 1
        q8_opt = 4
    elif q8f != 0:
        q8f -= 1
        q8_opt = 5
    elif q8g != 0:
        q8g -= 1
        q8_opt = 6

    print(q2_opt, q3_opt, q4_opt, q5_opt, q6_opt, q7_opt, q8_opt)

    driver.get('https://forms.gle/WgMg2kDnGkUvc7CP6')
    # Q1
    driver.find_element(By.XPATH, q1[int(random.randint(0,2))]).click()
    # Q2
    driver.find_element(By.XPATH, q2[int(q2_opt)]).click()
    # Q3
    driver.find_element(By.XPATH, q3[int(q3_opt)]).click()
    # Q4
    driver.find_element(By.XPATH, q4[int(q4_opt)]).click()
    # Q5
    driver.find_element(By.XPATH, q5[int(q5_opt)]).click()
    # Q6
    driver.find_element(By.XPATH, q6[int(q6_opt)]).click()
    # Q7
    driver.find_element(By.XPATH, q7[int(q7_opt)]).click()
    # Q8
    driver.find_element(By.XPATH, q8[int(q8_opt)]).click()

    # hand in btn
    #driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div').click()










