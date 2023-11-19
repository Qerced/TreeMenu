# TreeMenu
<details>
  <summary>Оглавление</summary>
  <ul>
    <li><a href="#описание">Описание</a></li>
    <li><a href="#настройка">Настройка</a></li>
    <li><a href="#запуск">Запуск</a></li>
    <li><a href="#админ-панель">Доступ к админ-панели</a></li>
  </ul>
</details>

## [Описание](#описание)

Django app, который реализует древовидное меню.

## [Настройка](#настройка)

Шаблон заполнения `.env`(должен находится в корне проекта):

```
SECRET_KEY=
DEBUG=false
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

## [Запуск](#запуск)

1. Запустите django app, БД и web сервер командой:

```
docker-compose -f infra/docker-compose.yml up
```

2. После запуска контейнера, перейдите по этой [ссылке](http://localhost):

```
http://localhost
```

## [Доступ к админ-панели](#админ-панель)

```
admin
admin_password
```
