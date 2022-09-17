# API_Yatube
## Описание проекта 
Реализация API [Yatube](https://github.com/Alexander28-31/hw05_final), созданной в рамках учебного курса Яндекс.Практикум
Поддерживает методы GET, POST, PUT, PATCH, DELETE
Аутентификация по JWT-токену
## Как запустить проект
```
python -m venv env  
```
```
source env/bin/activate  
```
#### Установить зависимость от файла requirements.txt: 
```
python -m pip install --upgrade pip 
``` 
```
pip install -r requirements.txt  
```
#### Создание суперпользователся
```
python manage.py createsuperuser
```
#### Выполнить выборку:
```
python manage.py migrate  
```
#### Запустить сервер
```
python manage.py runserver
```
## Аутентификация


## Примеры. Некоторые примеры файлов к API. <img src ="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

POST-запрос получения токена http://127.0.0.1:8000/api/v1/api-token-auth/ передав поля имя пользователя и пароль.

```
{
    "username":"xxxxxx",
    "password":"xxxxxx"
}

```
Вернёт:
```
{
    "token": "6a48cec33c2888564344119c59c50ded9bb89492"
}
```

POST-запрос добавления нового поста. http://127.0.0.1:8000/api/v1/posts/  с передачей tokena
```
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится."
} 
```
Вернёт:
```
{
    "id": 4,
    "author": "alex",
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "pub_date": "2022-09-17T16:28:10.414247Z",
    "image": null,
    "group": null
}
```
