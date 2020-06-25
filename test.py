from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

op = Options()
op.add_argument("--mute-audio")
f = open("data\data.txt", "r")
data_list = f.read().split("\n")
insta_login = data_list[0]
insta_password = data_list[1]
air_login = data_list[2]
air_password = data_list[3]
air_id = data_list[4]
air_token = data_list[5]

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=op)
driver.set_window_size(1230, 927)
driver.get("https://business.facebook.com/creatorstudio/")
driver.find_element_by_xpath(
    '//*[@id="media_manager_chrome_bar_instagram_icon"]'
).click()
driver.find_element_by_xpath(
    '//*[@id="u_0_0"]/div[2]/div/div/div[1]/div[2]/button'
).click()

while True:
    try:
        driver.switch_to_window(driver.window_handles[1]) # я какао делать пошел
        break
    except Exception:
        pass

while True:
    try:
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div/div/form/div[2]/div/label/input'
        ).send_keys(insta_login)
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div/div/form/div[3]/div/label/input'
        ).send_keys(insta_password)
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div/div/form/div[4]/button'
        ).click()
        break
    except Exception:
        try:
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div/div/form/div[2]/div/label/input'
            ).send_keys(insta_login)
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div/div/form/div[3]/div/label/input'
            ).send_keys(insta_password)
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div/div/form/div[4]/button'
            ).click()
            break
        except Exception:
            pass

while True:
    try:
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/section/div/button'
        ).click()
        break
    except Exception:
        pass

driver.switch_to_window(driver.window_handles[0])

while True:
    try:
        driver.find_element_by_xpath(
            '//*[@id="mediaManagerLeftNavigation"]/div[1]/div'
        ).click()
        break
    except Exception:
        pass

while True:
    try:
        driver.find_element_by_xpath(
            '//*[@id="globalContainer"]/div[2]/div/div/div/div/div/ul/li[1]/div/div/div'
        ).click()
        break
    except Exception:
        pass

while True:
    try:
        driver.find_element_by_id("creator_studio_sliding_tray_root")
        break
    except Exception:
        pass

while True:
    try:
        input = driver.find_element_by_css_selector('input[accept="video/*, image/*"]')
        break
    except:
        pass

img_list = ["\\image.jpeg", "\\Su24.jpg"]

for path in img_list:
    input.send_keys(path)
