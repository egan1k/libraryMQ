
# Library Management System

Микросервисное приложение для управления библиотекой книг. Включает 4 основных сервиса:

- **Сервис авторизации и регистрации пользователей**
- **Сервис управления книгами**
- **Сервис управления заказами книг**
- **Сервис поиска пользователей**

Приложение также использует базу данных PostgreSQL и Redis для кэширования.

## Шаги для клонирования и запуска проекта

### 1. Клонирование репозитория

Чтобы клонировать репозиторий на свой компьютер, выполните следующую команду:

```bash
git clone https://gitlab.com/Eganik/library_restapi_mq.git
cd LibraryManagmentDRF
```

### 2. Запуск проекта

Выполните следующую команду для запуска всех сервисов:

```bash
docker-compose up --build
```

### 3. Миграции базы данных

После запуска контейнеров, выполните миграции для каждого сервиса:

- **Auth Service**:
  ```bash
  docker-compose exec auth-service bash -c "cd auth_service && python manage.py makemigrations && python manage.py migrate"
  ```

- **Book Service**:
  ```bash
  docker-compose exec book-service bash -c "cd book_service && python manage.py makemigrations && python manage.py migrate"
  ```

- **Order Service**:
  ```bash
  docker-compose exec order-service bash -c "cd order_service && python manage.py makemigrations && python manage.py migrate"
  ```

- **User Search Service**:
  ```bash
  docker-compose exec user-search-service bash -c "cd user_search_service && python manage.py makemigrations && python manage.py migrate"
  ```

### 4. Создание суперпользователя (опционально)

Чтобы создать суперпользователя для администрирования:

- **Auth Service**:
  ```bash
  docker-compose exec auth-service bash -c "cd auth_service && python manage.py createsuperuser"
  ```

- **Book Service**:
  ```bash
  docker-compose exec book-service bash -c "cd book_service && python manage.py createsuperuser"
  ```

- **Order Service**:
  ```bash
  docker-compose exec order-service bash -c "cd order_service && python manage.py createsuperuser"
  ```

- **User Search Service**:
  ```bash
  docker-compose exec user-search-service bash -c "cd user_search && python manage.py createsuperuser"
  ```
