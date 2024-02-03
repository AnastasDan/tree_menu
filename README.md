# Древовидное меню

Небольшое веб-приложение на Django, которое реализовывает древовидное меню через template tag.

## Как запустить:

Клонируем себе репозиторий:

```
git clone git@github.com:AnastasDan/tree_menu.git
```

Переходим в директорию:

```
cd tree_menu
```

Cоздаем и активируем виртуальное окружение:

* Если у вас Linux/MacOS:

    ```
    python3 -m venv venv
    ```

    ```
    source venv/bin/activate
    ```

* Если у вас Windows:

    ```
    python -m venv venv
    ```

    ```
    source venv/Scripts/activate
    ```

Устанавливаем зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполняем миграции:

```
python manage.py migrate
```

Создаем суперпользователя:

```
python manage.py createsuperuser
```

Запускаем проект:

```
python manage.py runserver
```

## После запуска переходим по этой ссылке:

http://127.0.0.1:8000/tree_menu/
