import os 
from tkinter import *
from functools import partial


tkWindow = Tk()
tkWindow.geometry('300x200')


insta_login_label = Label(tkWindow, text="Логин от instagram").grid(row=0, column=0)
insta_login = StringVar()
insta_login_entry = Entry(tkWindow, textvariable=insta_login).grid(row=0, column=1)


insta_password_label = Label(tkWindow, text="Пароль от instagram").grid(row=1, column=0)
insta_password = StringVar()
insta_password_entry = Entry(tkWindow, show='*', textvariable=insta_password).grid(row=1, column=1)


air_login_label = Label(tkWindow, text="Логин от airtable").grid(row=2, column=0)
air_login = StringVar()
air_login_entry = Entry(tkWindow, textvariable=air_login).grid(row=2, column=1)


air_password_label = Label(tkWindow, text="Пароль от airtable").grid(row=3, column=0)
air_password = StringVar()
air_password_entry = Entry(tkWindow, show='*' , textvariable=air_password).grid(row=3, column=1)


air_id_label = Label(tkWindow, text="ID Базы airtable").grid(row=4, column=0)
air_id = StringVar()
air_id_entry = Entry(tkWindow, textvariable=air_id).grid(row=4, column=1)


air_token_label = Label(tkWindow, text="Личный токен airtable").grid(row=5, column=0)
air_token = StringVar()
air_token_entry = Entry(tkWindow, textvariable=air_token).grid(row=5, column=1)

def write(insta_login, insta_password, air_login, air_password, air_id, air_token):
    with open('data\data.txt', 'wt') as f:
        f.write(f'{insta_login.get()}\n')
        f.write(f'{insta_password.get()}\n')
        f.write(f'{air_login.get()}\n')
        f.write(f'{air_password.get()}\n')
        f.write(f'{air_id.get()}\n')
        f.write(f'{air_token.get()}')
    tkWindow.destroy()

write = partial(write, insta_login, insta_password, air_login, air_password, air_id, air_token)

login_button = Button(tkWindow, text="Установить", command=write).grid(row=6, column=1)  

tkWindow.title('Airtable > Instagram | Установка')

tkWindow.mainloop()
