import os
import requests

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
r = requests.get(url, headers=headers)

print(r.json())

while True:
    input('введите что-либо чтобы начать работу программы >>')
    r = requests.get(url, headers=headers)
    count_rec = len(r.json()['records'])
    records = r.json()['records']
    if len(r.json()['records']) != 0:
        print(f'найдено {count_rec} новых записей')
        for rec in records:
            text = rec['fields']['text']
            date = rec['fields']['date']
            year = date.split('-')[0]
            month = date.split('-')[1]
            day = date.split('T')[0].split('-')[-1]
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
            
            #post(text=text, day=day, month=month, year=year, hour=hour, minute=minute)

            for del_image in img_list:
                os.remove(os.getcwd() + '\\img\\' + del_image)
    else:
        print('не найдено новых записей')
