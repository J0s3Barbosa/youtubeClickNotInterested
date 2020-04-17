from selenium import webdriver
from time import sleep    
import os
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pdb
from dotenv import load_dotenv


dirpath = os.getcwd()
load_dotenv()
# pdb.set_trace()0

driver = webdriver.Chrome(
    executable_path=r"{}\chromedriver.exe".format(dirpath))
driver.close()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("disable-infobars")
options.add_argument("--allow-file-access-from-files")
options.add_argument("--allow-file-access")
options.add_argument("--allow-cross-origin-auth-prompt")
options.add_argument("--disable-web-security")

driver = webdriver.Chrome(options=options)
url = os.getenv("URL")
driver.maximize_window()
driver.get(str(url))
wait = WebDriverWait(driver, 10)
main_window = driver.current_window_handle

driver.switch_to.window(main_window)

def username():
    while True:
        try:
            WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements_by_xpath("//*[@id='identifierId']")) > 0)
            bet_fa = driver.find_element_by_id("identifierId")
            GOOGLE_USERNAME = os.getenv("GOOGLE_USERNAME")
            bet_fa.send_keys(GOOGLE_USERNAME)
            bet_fa.send_keys(u'\ue007')
            break
        except Exception as ex:
            print(ex)


def password():
    while True:
        try:
            WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")) > 0)
            input_pass = driver.find_element_by_name("password")
            PASSWORD = os.getenv("PASSWORD")
            input_pass.send_keys(PASSWORD)
            input_pass.send_keys(u'\ue007')
            break
        except Exception as ex:
            print(ex)


def click_menu():
    while True:
        try:
            to_be_searched = "//*[@id='button']/yt-icon"
            menu_actions = "//button[@aria-label='Menu de ações']"
            WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements_by_xpath(to_be_searched)) > 0)
            input_pass = driver.find_element_by_xpath(menu_actions)
            input_pass.click()
            break
        except Exception as ex:
            print(ex)
  

            # input_not_interest = driver.find_element_by_xpath("//*[@id='items']/ytd-menu-service-item-renderer[3]/paper-item/yt-formatted-string")
            # input_not_interest.click()


def click_not_intereted():
    while True:
        try:
            to_be_searched = "//*[@id='items']/ytd-menu-service-item-renderer[3]/paper-item/yt-formatted-string"
            WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements_by_xpath(to_be_searched)) > 0)
            input_not_interest = driver.find_element_by_xpath(to_be_searched)
            input_not_interest.click()
            break
        except Exception as ex:
            print(ex)

def scroll():
    try:
    #    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        body = driver.find_element_by_css_selector('body')
        body.send_keys(Keys.PAGE_DOWN)
    except Exception as ex:
        print(ex)

def scrolling():
    try:
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    except Exception as ex:
        print(ex)

def all_videos_click_not_intereted():
    while True:
        try:
            count = 0
            list_actions = get_menus_not_interested()
            list_video = list_video_info()
            for action in list_actions:
                for playlist_title in list_video:
                    # title
                    title = playlist_title.get_attribute("title")
                    print(title)
                    #Nanatsu no Taizai Temporada 3 Capítulo 6 Sub Español HD720p Meliodas há 2 dias 20 minutos 2.005.588 visualizações
                    description = playlist_title.get_attribute("aria-label")
                    print(description)
                    # '2 mi de visualizações'
                    views = playlist_title.find_element_by_xpath('//*[@id="metadata-line"]/span[1]').text
                    print(views)
                   #'há 2 dias 47 minutes ago'
                    days_vid_out = playlist_title.find_element_by_xpath('//*[@id="metadata-line"]/span[2]').text
                    print(days_vid_out)
                   # 'Meliodas' name of the chanel
                    channel_name = playlist_title.find_element_by_xpath('//*[@id="text"]/a').text
                    print(channel_name)
                   # link
                   #  https://www.youtube.com/watch?v=uCEHNiofWjk
                    link = playlist_title.get_attribute("href")
                    print(link)
                    print()
                    # pdb.set_trace()
                    try:
                        action.click()
                        click_not_intereted()
                        count += 1
                    except Exception as ex:
                        print(ex)
                    
                    # sleep(2)
                    if count == len(list_actions):
                        scroll()
                        list_actions = get_menus_not_interested()
                        update_page()
                        count = 0 
                        # pdb.set_trace()
                    list_video.pop(0)
                    
                    break

        except Exception as ex:
            print(ex)
            update_page()

def update_page():
    driver.refresh()
            # pdb.set_trace()

def get_menus_not_interested():
    try:
        menu_actions = "//button[@aria-label='Menu de ações']"
        WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements_by_xpath(menu_actions)) > 0)
        
        #if vedeo that i dont like mark
        #set queries on a json file for machine learning
        
        list_actions = driver.find_elements_by_xpath("//button[@aria-label='Menu de ações']")
        print('list_actions = ' + str(len(list_actions)))
        return list_actions
    except Exception as ex:
        print(ex)

def list_video_info():
    try:
        playlist_titles = driver.find_elements_by_xpath("//a[@id='video-title']")
        print('playlist_titles = ' + str(len(playlist_titles)))

        return playlist_titles
    except Exception as ex:
        print(ex)


try:
    username()
    sleep(2)
    password()
    sleep(2)
    all_videos_click_not_intereted()
    # pdb.set_trace()

except Exception as ex:
    print(ex)
    driver.quit()

# finally:






