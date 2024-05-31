# 🌍Приложение Students grade book

Приложение предназначено для `учета учеников и оценок`.
Оно разработано с использованием `FastAPI и SQLAlchemy, базы данных PostgreSQL`.

## Начало работы

Эти инструкции помогут вам `запустить` копию проекта на вашей локальной машине 
для разработки и тестирования.

### Установка и запуск проекта

1. `Клонируйте` репозиторий на вашу локальную машину:

```
git clone https://github.com/ValentinKim531/Students_grade_book_API.git
```

2. Перейдите в директорию с приложением и создайте, активируйте `виртуальную среду`:

```
python -m venv .venv
```
```
source .venv/bin/activate  # для macOS и Linux
```
```
.\.venv\Scripts\activate  # для Windows
```

3. Установите `зависимости`

```
pip install -r requirements.txt
```


4. Настройте файл `.env`

Переименуйте файл ".env.example", находящийся в корне проекта, на ".env" и заполните его.

5. Создайте `базы данных и выполните миграции`:
Убедитесь, что PostgreSQL запущен и база данных создана. Затем выполните миграции:
```
alembic upgrade head
```

6. `Запустите` приложение
```
uvicorn main:app --reload --port 8000
```

7. Пройдите `по ссылке` в браузере
```
http://127.0.0.1:8000/docs
```



## API Эндпоинты:

### Создание нового студента
 - POST /students/

`Пример запроса:`

```{
  "first_name": "Valentin",
  "last_name": "Kim",
  "birthdate": "1992-01-20",
  "email": "valentink@yandex.ru"
}
```

`пример ответа:`

```{
  "id": 1,
  "first_name": "Valentin",
  "last_name": "Kim",
  "birthdate": "1992-01-20",
  "email": "valentink@yandex.ru",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00",
  "scores": []
}
```

### Получение списка всех студентов
GET /students/

`Пример ответа:`


```[
  {
    "id": 1,
    "first_name": "Valentin",
    "last_name": "Kim",
    "birthdate": "1982-01-20",
    "email": "valentink@yandex.ru",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00",
    "scores": []
  }
]
```

### Получение списка всех студентов с их оценками
GET /students/with-scores/

`Пример ответа:`

```
[
  {
    "id": 1,
    "first_name": "Valentin",
    "last_name": "Kim",
    "birthdate": "1982-01-20",
    "email": "valentink@yandex.ru",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00",
    "scores": [
      {
        "id": 1,
        "student_id": 1,
        "score": 5,
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00"
      }
    ]
  }
]
```


### Получение информации о конкретном студенте и его оценках 
GET /students/{student_id}/with-scores/
`
Пример ответа:`

```
{
  "id": 3,
  "first_name": "Rus",
  "last_name": "Ivanov",
  "birthdate": "1999-05-31",
  "email": "rrr@yandex.ru",
  "created_at": "2024-05-31T14:31:58.065656",
  "updated_at": "2024-05-31T14:31:58.065656",
  "scores": [
    {
      "id": 1,
      "student_id": 3,
      "score": 4,
      "created_at": "2024-05-31T14:34:29.193354",
      "updated_at": "2024-05-31T14:34:29.193354"
    },
    {
      "id": 2,
      "student_id": 3,
      "score": 6,
      "created_at": "2024-05-31T14:34:36.065662",
      "updated_at": "2024-05-31T14:34:36.065662"
    },
    {
      "id": 3,
      "student_id": 3,
      "score": 5,
      "created_at": "2024-05-31T14:34:44.344138",
      "updated_at": "2024-05-31T14:34:44.344138"
    }
  ]
}
```


### Получение информации о конкретном студенте
GET /students/{student_id}

`Пример ответа:`

```
{
  "id": 1,
  "first_name": "Valentin",
  "last_name": "Kim",
  "birthdate": "1982-01-20",
  "email": "valentink@yandex.ru",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00",
  "scores": []
}
```

### Обновление информации о конкретном студенте 
PATCH /students/{student_id}

`Пример запроса:`

```
{
  "first_name": "Valentin",
  "last_name": "Kim",
  "birthdate": "1982-01-20",
  "email": "valentink@example.com"
}
```


### Удаление студента
DELETE /students/{student_id}

`Пример ответа:`

```
{
  "id": 1,
  "first_name": "Valentin",
  "last_name": "Kim",
  "birthdate": "1982-01-20",
  "email": "valentink@yandex.ru",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00",
  "scores": []
}
```



## Оценки (Scores)


### Добавление оценки ученику
POST /scores/

`Пример запроса:`

```
{
  "student_id": 1,
  "score": 5
}
```

`Пример ответа:`

```
{
  "id": 1,
  "student_id": 1,
  "score": 5,
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```


### Получение информации о конкретной оценке

GET /scores/{score_id}

`Пример ответа:`

```
{
  "id": 1,
  "student_id": 1,
  "score": 5,
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

### Обновление информации о конкретной оценке

PATCH /scores/{score_id}

`Пример запроса:`

```
{
  "student_id": 0,
  "score": 0
}
```

`Пример ответа:`

```
{
  "id": 1,
  "student_id": 1,
  "score": 4,
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

### Удаление оценки

DELETE /scores/{score_id}

`Пример ответа:`

```
{
  "id": 1,
  "student_id": 1,
  "score": 4,
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```
