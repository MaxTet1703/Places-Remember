# Places Remeber
## Описание: веб-прилоежние с авторизацией через ВКонтакте и возможностью создавать отзывы о местах, отмечая их на карте
### Запуск приложения
Примечание: Для полноценной работы приложения следует использовать docker и docker compose

Сборка приложения
```
docker-compose build
```
Миграция моеделей в PostreSQl
```
docker-compose run --rm backend python manage.py migrate
```
Тестирование приложения
```
docker-compose run --rm backend python manage.py test app
```
Запуск линтера
```
docker-compose run --rm backend flake8 --config config.cfg
```
Запуск приложения
```
docker-compose up
```
Примечание: Заходить на сайт стоит с хоста localhost:8000
