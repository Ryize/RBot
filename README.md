# Rbot

NOC (альтернативное название Rbot) - New Orbit Cannon. Программа для стресс-тестирования собственных интернет ресурсов.

## Использованные технологии: 


![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
<br><br>

## Прежде всего:

> Установите Python (если он не установлен)<br>
> [Скачать Python3](https://www.python.org/downloads/)

<br>

Клонируйте репозиторий и перейдите в установленную папку:
```
git clone https://github.com/Ryize/RBot.git
cd RBot
```

Установите requirements:
```
pip3 install -r requirements.txt
```
<br>

Проект делится на две основные части:
<ul>
<li>Клиентскую, запускается на компьютерах с которых будет идти тестирование. Распологается в директории client/</li>
<li>Серверную, панель и БД задач для тестирования. Это весь остальной проект</li>
</ul>

Далее вам необходимо создать файл config.py и указать информацию для БД в формате:
```
DATABASE_URL = 'dialect+driver://username:password@host:port/database'
```

Тепепрь можно запустить проект командой:
```
python3 app.py
```

Теперь перейдите в клиентскую часть:
```
cd client
```
Откройте файл sys.pyw и добавьте свой домен/ip к которому привязана серверная часть.
Далее снова откройте файл system.py и добавьте свой домен/ip.

После вам надо открыть свою базу данных, и перейти в таблицу code.
Создайте новую запись, в строчку код (! важно) скопируйте весь код с отредактированного файла system.py
Если вы измените код в system.py, он автоматически обновится на всех подконтрольных устройствах. Для этого увеличьте цифру на первой строке файла (по умолчания: # 4).
Сохраните изменения в БД.

Теперь вы можете запустить файл sys.pyw на любом компьютере под Windows, на котором установлен Python. Скрипт сам поставит все библиотеки и перекопирует себя в автозапуск.
Устройство появится в панели через несколько секунд.

<hr>
Важные нюансы:
<ul>
  <li>Умная атака - атака которая запуск определённое кол-во потоков в зависимости от указанного % скорости. 15 потоков на 1мбит скорости</li>
  <li>Задержка - это время перед отправкой пакетов внутри потоков. Не влияет на скорость создания потоков</li>
  <li>Для перегрузки сайта без защиты требуется около 1500 потоков (+- 500 потоков)</li>
</ul>

> Этот проект создан ИСКЛЮЧИТЕЛЬНО для тестирования собственных ресурсов. При использовании в противозаконных действиях автор отвественность не несёт.
