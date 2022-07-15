import random
import time
from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.service import Service
serv = Service("C:\chromedriver_win32\chromedriver.exe")
# serv = Service("C:\msedgedriver.exe")


driver = webdriver.Chrome(service=serv)

def login(username_, password_):
    driver.get('https://www.instagram.com/')
    driver.implicitly_wait(4)

    # cookies = driver.find_element(by=By.XPATH, value='//button[text()="Allow essential and optional cookies"]')
    # cookies.click

    username = driver.find_element(by=By.NAME, value='username')
    password = driver.find_element(by=By.NAME, value='password')

    username.click()
    username.send_keys(username_)
    time.sleep(1)

    password.click()
    password.send_keys(password_)
    time.sleep(1)


    Log_in = driver.find_element(by=By.XPATH, value='//div[text()="Log In"]')
    Log_in.click()
    time.sleep(1)


    Not_now_credentials = driver.find_element(by=By.XPATH, value = "//button[text()='Not Now']")
    Not_now_credentials.click()
    time.sleep(1)


    Not_now_notif = driver.find_element(by=By.XPATH, value = "//button[text()='Not Now']")
    Not_now_notif.click()
    time.sleep(1)
    # Search_box.send_keys("sahil.uwu")

    # follow_like_comment()

def follow_like_comment(number):
    profiles_list=['sahil.uwu', 'ctfu_.radhe']
    comments=["You're amazing!", 'you are great!', "I love your content", "Stay happy King", "Amazing", "Niceeeeeeee"]

    for i in range(len(profiles_list)): 

        Search_box = driver.find_element(by=By.XPATH, value='//span[text()="Search"]')
        Search_box.click()
        Search_post_click = driver.find_element(by=By.XPATH, value='//input[@placeholder="Search"]')
        Search_post_click.send_keys(profiles_list[i])
        time.sleep(2)

        prof = driver.find_element(by=By.XPATH, value='//div[text()="sahil.uwu"]')
        prof.click()
        time.sleep(3)

        #follow
        follow = driver.find_element(by=By.XPATH, value='//div[text()="Follow"]')
        follow.click()
        time.sleep(1)

        #post
        post = driver.find_element(by=By.XPATH, value='//div[@class="_aagw"]')
        post.click()
        time.sleep(1)


        for j in range(number):

            #like
            like = driver.find_element(by=By.XPATH, value= '(//*[local-name()="svg"][@aria-label="Like"][@height="24"])[2]')
            like.click()
            time.sleep(1)

            #comment
            Comment_box = driver.find_element(by=By.XPATH, value='//textarea[@placeholder="Add a comment…"]')
            Comment_box.click()
            time.sleep(3)
            Comment_box = driver.find_element(by=By.XPATH, value='//textarea[@placeholder="Add a comment…"]')
            Comment_box.send_keys(random.choice(comments))
            time.sleep(1)

            Send_cmmt = driver.find_element(by=By.XPATH, value='//div[text()="Post"]')
            Send_cmmt.click()
            time.sleep(1)

            #next
            Next_button = driver.find_element(by=By.XPATH, value='//*[local-name()="svg"][@aria-label="Next"]')
            Next_button.click()
            time.sleep(1)

        Close_post = driver.find_element(by=By.XPATH, value='//*[local-name()="svg"][@aria-label="Close"]')
        Close_post.click()
        time.sleep(1)

        Direct_message('You are the best coder in the world!')

def Direct_message(Msg_text):
    DM_button = driver.find_element(by=By.XPATH, value='//div[text()="Message"]')
    DM_button.click()
    time.sleep(1)

    Msg_box= driver.find_element(by=By.XPATH, value='//textarea[@placeholder="Message..."]')
    Msg_box.send_keys(Msg_text)
    time.sleep(1)


    sendkey = driver.find_element(by=By.XPATH, value='//button[text()="Send"]')
    sendkey.click()
    time.sleep(1)



#function_call
login("bot_chand69", "Bot_chand6969")
follow_like_comment(2)

# bot_chand69
# Bot_chand6969

# brogrammer_bot69
# Brogrammer_bot6969