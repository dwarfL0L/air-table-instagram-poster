# Airtable instagram poster

## Как им пользоваться?

Чтобы воспользоваться программой нужно для начала её скачать. Для этого переходим в папку для загрузки через `cd` в коммандной строке и вбиваем:
 `git clone https://github.com/dwarfL0L/air-table-instagram-poster.git`
Для этого способа загрузки понадобится установленный на ПК git.
 
Если у вас не установлен git, то можно просто скачать zip архив с этого сайта нажав на кнопку "clone" и после этого нажав на кнопку "download zip".

### Что сейчас?
Сейчас вам нужно скачать пакеты для работы программы. Для этого в терминале направляемся в папку с содержимым и после этого пишем:
`pip isntall -r requirements.txt`

После этого можно смело запускать установщик, а после и саму программу.

Запускаем `installer.py` и вводим данные аккаунтов и базы airtable с постами instagram. 
*после этого программа установлена и можно ей пользоваться*

## Как обустроить таблицу?

![Table Example](/img/table.png)
Для того чтобы программа работала правильно нужно чтобы в рабочей таблице было три колонки: 
1. text
2. date
3. attachments

тип первой колонки - long text
тип второй колонки - date
тип третьей колонки - Attachment

*настройка колонки date*
>![Date Description](/img/date.png)

**Важно** _чтобы сама таблиица_ (не путать с базой) _называлась "Table 1"._

## Всё готово!
Теперь вы можете запустить `app.py` и программа начнёт работу.
___
## Todo
Всё же хочется добавить, что я не вижу программу как полноценно доделанный софт. Поэтому мне нужно над ней активно работать.

Вот всё что мне нужно доделать:
 - [ ] перевести программу на GUI
- [ ] полиш программы
- [ ] добавление сториз
---
#### Над программой работали 
@dwarf_L0L и @bulatcute
#### Контакты
telegram:

- @idk_idk1
- @abclxyz
