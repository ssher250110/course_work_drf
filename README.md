# DRF Habits

## Критерии

* Настроили CORS.
* Настроили интеграцию с Телеграмом.
* Реализовали пагинацию.
* Использовали переменные окружения.
* Все необходимые модели описаны или переопределены.
* Все необходимые эндпоинты реализовали.
* Настроили все необходимые валидаторы.
* Описанные права доступа заложены.
* Настроили отложенную задачу через Celery.
* Проект покрыли тестами как минимум на 80%.
* Код оформили в соответствии с лучшими практиками.
* Имеется список зависимостей.
* Результат проверки Flake8 равен 100%, при исключении миграций.
* Решение выложили на GitHub.

## Инструкция для запуска проекта

<details>
<summary>Инструкция</summary>
1. Клонируйте данный репозиторий к себе на локальную машину:

```bash
    git clone https://github.com/ssher250110/course_work_drf.git
```

2. Настройте виртуальное окружение poetry и установите библиотеки и их зависимости.

```bash
poetry env use python3.12
poetry shell
poetry install
```

3. В файле /.env_example подставьте свои переменные окружения и переименуйте файл в .env


4. Примените миграции

```bash
python manage.py migrate
```

6. Запустите сервер

```bash
python3 manage.py runserver
```

7. Команда для суперпользователя

```bash
python3 manage.py csu
```

8. Команды для запуска Celery и Celery Beat

```bash
celery -A config worker --loglevel=info
celery -A config beat --loglevel=info

```

</details>
