# Library Management System

## Микросервисное приложение для управления библиотекой книг. Включает 4 основных сервиса:

### Сервис авторизации и регистрации пользователей
### Сервис управления книгами
### Сервис управления заказами книг
### Сервис поиска пользователей
### Приложение также использует базу данных PostgreSQL и Redis для кэширования.

## Шаги для клонирования и запуска проекта
### 1. Клонирование репозитория
### Чтобы клонировать репозиторий на свой компьютер, выполните следующую команду:
```sh
$ git clone https://gitlab.com/Eganik/library_restapi_mq.git
$ cd LibraryManagmentDRF
```

### Запуск проекта 
```sh
$ docker-compose up --build
```

### Миграции базы данных
```sh
$ docker-compose exec auth-service bash -c "cd auth_service && python manage.py makemigrations && python manage.py migrate"
$ docker-compose exec book-service bash -c "cd book_service && python manage.py makemigrations && python manage.py migrate"
$ docker-compose exec order-service bash -c "cd order_service && python manage.py makemigrations && python manage.py migrate"
$ docker-compose exec user-search-service bash -c "cd user_search_service && python manage.py makemigrations && python manage.py migrate"
```

### Создание суперпользователя (опционально)
```sh
$ docker-compose exec <service-name> <service_name> python manage.py createsuperuser
```