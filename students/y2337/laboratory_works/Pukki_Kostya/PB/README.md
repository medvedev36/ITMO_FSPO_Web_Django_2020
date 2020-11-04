# The-Planning-Board
Итоговая работа Django + React

## Развертывание:

#### Создание виртуальной среды:
```
python -m venv venv
```
---
#### Активация виртуальной среды:
```
venv\Scripts\activate.bat
```
---
#### Установка зависимостей:
```
pip install -r req.txt
```
---
#### Миграции
```
python manage.py makemigrations
python manage.py migrate
```
---
#### Развертывание клиента
```
cd client
npm i
npm run build
```
---
#### Запуск
```
python manage.py runserver
```
