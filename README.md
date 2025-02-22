# Описание
Микро-сервис для скачивания информации с ftp.zakupki.gov.ru, работающий на связке flask+uWSGI+NGINX.
1. Api для скачивания архивов с информацией по аукциону с ftp за заданный период

# Структура
* app/ - директория с flask приложением
* congigs/ - директория с настройками пакетов, приложения, api. Все настройки можно получить от ConfigDealer
* packages/ - директория со специальными пакетами необдодимые для работы контроллеров flask. Получить необходимый объект можно от PackageDealer
* wsgi.py - файл точки входа
* service.ini - файл настройками uWSGI сервиса
* ftpd.sock - файл сокет для соеденения сервера NGINX  с сервисом uWSGI
* setup.py - файл установки. Временно не работает
* .env - файл с переменными окружения, необходимые для работы сериса

# Предустановки
1. sudo apt update
2. sudo apt install nginx python3
3. sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-d$

# Установка
1. Скачать с репозитория
2. Созздать venv и установить в него требуемые пакеты из requirements.txt
3. Настроить файл .env
4. Настроить файл .service
5. Создать uWSGI сервис в ОС.
6. Создать связть uWSGI и NGINX через файл ftpd.sock

# Настройка Configs(.env) - файл переменных виртуального окружения
* APP_MODE - режим в котором включить приложение
* FTP_HOST - ссылка на удаленный Ftp
* FTP_LOGIN - логин от FTP
* FTP_PASSWORD - пароль от FTP
* FTP_ZIPS - директория загрузки
* API_AUTOFILLER - ссылка на API autofiller
