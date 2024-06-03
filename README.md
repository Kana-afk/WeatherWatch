# WeatherWatch API

WeatherWatch API - это платформа для мониторинга и управления данными о погодных условиях с различных датчиков.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/Kana-afk/weatherwatch.git
    cd weatherwatch
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для MacOS/Linux
    .\venv\Scripts\activate   # Для Windows
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Создайте суперпользователя:

    ```bash
    python manage.py createsuperuser
    ```

6. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

## API Эндпоинты

### Регистрация пользователя

- **URL:** `POST /api/register/`
- **Body (JSON):**

    ```json
    {
        "username": "newuser",
        "password": "ComplexPass123!",
        "email": "newuser@example.com",
        "first_name": "New",
        "last_name": "User"
    }
    ```

### Получение JWT токена

- **URL:** `POST /api/token/`
- **Body (JSON):**

    ```json
    {
        "username": "newuser",
        "password": "ComplexPass123!"
    }
    ```

### Обновление JWT токена

- **URL:** `POST /api/token/refresh/`
- **Body (JSON):**

    ```json
    {
        "refresh": "your_refresh_token"
    }
    ```

### Создание датчика

- **URL:** `POST /api/sensors/`
- **Headers:** `Authorization: Bearer <your_access_token>`
- **Body (JSON):**

    ```json
    {
        "type": "temperature",
        "model": "T1000",
        "installation_date": "2023-01-01",
        "status": "active"
    }
    ```

### Получение списка датчиков

- **URL:** `GET /api/sensors/`
- **Headers:** `Authorization: Bearer <your_access_token>`

### Обновление датчика

- **URL:** `PUT /api/sensors/{id}/`
- **Headers:** `Authorization: Bearer <your_access_token>`
- **Body (JSON):**

    ```json
    {
        "type": "humidity",
        "model": "H2000",
        "installation_date": "2023-01-01",
        "status": "inactive"
    }
    ```

### Удаление датчика

- **URL:** `DELETE /api/sensors/{id}/`
- **Headers:** `Authorization: Bearer <your_access_token>`

### Создание данных

- **URL:** `POST /api/data/`
- **Headers:** `Authorization: Bearer <your_access_token>`
- **Body (JSON):**

    ```json
    {
        "sensor": 1,
        "temperature": 23.5,
        "humidity": 60.0,
        "wind_speed": 5.0,
        "rain": 0.0
    }
    ```

### Получение списка данных

- **URL:** `GET /api/data/`
- **Headers:** `Authorization: Bearer <your_access_token>`

### Создание оповещения

- **URL:** `POST /api/alerts/`
- **Headers:** `Authorization: Bearer <your_access_token>`
- **Body (JSON):**

    ```json
    {
        "sensor": 1,
        "description": "High temperature detected"
    }
    ```

### Получение списка оповещений

- **URL:** `GET /api/alerts/`
- **Headers:** `Authorization: Bearer <your_access_token>`

## Документация API

Документация доступна по адресам `/swagger/` и `/redoc/`.
