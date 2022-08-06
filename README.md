# test-canal-service


## Выполненные пункты
### 1-3 пункты (решены полностью)

### 4a, 4b - полностью, 4с - решен без react на flask


## Инструкция по запуску 

### С помощью Docker
Основные команды:
```sh
# клонируем репозиторий
git clone https://github.com/dmsgavrilov/test-canal-service.git
cd test-canal-service

# выполняем билд проекта
docker-compose -f docker-compose.yml build

# запускаем проект
docker-compose -f docker-compose.local.yml up -d

# просматриваем логи
docker-compose -f docker-compose.local.yml down --remove-orphans

# останавливаем проект
docker-compose -f docker-compose.local.yml down --remove-orphans
```


### Без Docker

### Создание виртуального окружения

`virtualenv -p python3.9  venv`

### Запуск БД 

`docker run -d --name postgres -e POSTGRES_HOST_AUTH_METHOD=trust -p 5432:5432 -v {ABSOLUTE_PATH_TO_APP}/test-canal-service/DataBase:/docker-entrypoint-initdb.d  postgres:12-alpine
` *- запускаем постргю локально на 5432*

### Запуск основного скрипта
```
pip install -r UpdateScript/requirements.txt
python3 UpdateScript/main.py
```

### Запуск веб-приложения
```
pip install -r Web/requirements.txt
python3 Web/main.py
```


### Все необходимые данные есть в репозитории (для удобной проверки, разумеется)

Ссылка на копию таблицы - https://docs.google.com/spreadsheets/u/0/d/1NKughm4IIRRMi5Di57CUNgKccxIcFk5c958rfwL5TCQ/htmlview \
Ссылка на канал для получения уведомлений в Telegram - https://t.me/not1fy_test_channel 
