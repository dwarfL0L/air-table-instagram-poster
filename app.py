import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")
f = open("data\data.txt", "r")
data_list = f.read().split("\n")
insta_login = data_list[0]
insta_password = data_list[1]
air_login = data_list[2]
air_password = data_list[3]
air_id = data_list[4]
air_token = data_list[5]

url = f'https://api.airtable.com/v0/{air_id}/Table%201'
headers = {
    "Authorization": f"Bearer {air_token}"
}
driver = webdriver.Chrome(
    executable_path=ChromeDriverManager().install(),
    options=chrome_options
)
driver.set_window_size(1230, 927)
driver.get("https://business.facebook.com/creatorstudio/")
driver.find_element_by_xpath(
    '//*[@id="media_manager_chrome_bar_instagram_icon"]'
).click()
driver.find_element_by_xpath(
    '//*[@id="u_0_0"]/div[2]/div/div/div[1]/div[2]/button'
).click()

actions = ActionChains(driver)

while True:
    try:
        driver.switch_to_window(driver.window_handles[1])
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

def post(text, img_list, day, month, year, hour, minute):
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


    for name in img_list:
        driver.execute_script('document.querySelector("._82ht > div").click()')

        while True:
            try:
                input = driver.find_element_by_css_selector('input[accept="video/*, image/*"]')
                break
            except:
                pass

        input.send_keys(os.getcwd() + '\\img\\' + name)
    
    driver.find_element_by_xpath('//*[@id="creator_studio_sliding_tray_root"]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div').click()
    actions = ActionChains(driver)
    actions.send_keys(text)
    actions.perform()

    driver.find_element_by_link_text('dropdownButton').click()

    while True:
        try:
            driver.find_element_by_link_text('Запланированная публикация').click()
            break
        except Exception:
            pass

    while True:
        try:
            driver.find_element_by_xpath('//input[@placeholder="дд.мм.гггг"]').send_keys(f'{day}.{month}.{year}')
            break
        except Exception:
            pass

while True:
    input('введите что-либо чтобы начать работу программы >>')
    r = requests.get(url, headers=headers)
    print(r.json())
    count_rec = len(r.json()['records'])
    records = r.json()['records']
    if len(r.json()['records']) != 0:
        print(f'найдено {count_rec} новых записей')
        for rec in records:
            text = rec['fields']['text']
            date = rec['fields']['date']
            year = date.split('-')[0]
            month = date.split('-')[1]
            
            if month.startswith('0'):
                month = list(month)[1]
            
            day = date.split('T')[0].split('-')[-1]
            
            if day.startswith('0'):
                day = list(day)[1]
            
            hour = date.split('T')[1].split(':')[0]
            minute = date.split('T')[1].split(':')[1]
            img_list = []

            for img in rec['fields']['attachments']:
                img_url = img['url']
                filename = img_url.split('/')[-1]
                img_list.append(filename)
                img_resp = requests.get(img_url)
                image = open(os.getcwd() + '\\img\\' + filename, 'wb')
                image.write(img_resp.content)
                image.close()
            
            post(text=text, img_list=img_list, day=day, month=month, year=year, hour=hour, minute=minute)

            for del_image in img_list:
                os.remove(os.getcwd() + '\\img\\' + del_image)
    else:
        print('не найдено новых записей')
