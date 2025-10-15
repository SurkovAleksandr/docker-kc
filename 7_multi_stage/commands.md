# Команды для поднятия сайта локально

Чтобы команды сработали, нужно находиться в текущей папке (`lesson_7`).
Результатом команды ls должно быть что-то в таком роде:

```
backend  database  frontend  nginx  README.md  Сommands.md
```

## Создаем образы

```shell
docker build -t 7_back ./backend
```

```shell
docker build -t 7_database ./database
```

```shell
docker build -t 7_nginx ./frontend
```

## Создаем сеть и вольюм

```shell
docker volume create 7_db
```

```shell
docker network create 7_net
```

## Поднимаем базу данных

```shell
docker run --rm -d \
  --name database \
  --net=7_net \
  -v 7_db:/var/lib/postgresql/data \
  -e POSTGRES_DB=postgresql \
  -e POSTGRES_USER=postgresql \
  -e POSTGRES_PASSWORD=postgresql \
  -p 5432:5432 \
  7_database
```

## Поднимаем бекенд

```shell
docker run --rm -d \
  --name backend \
  --net=7_net \
  -e HOST=database \
  -e PORT=5432 \
  -e DB=postgresql \
  -e DB_USERNAME=postgresql \
  -e DB_PASSWORD=postgresql \
  7_back
```

## Поднимаем фронтедн

```shell
docker run --rm -d \
  --name frontend \
  --net=7_net \
  -p 80:80 \
  -v $(pwd)/nginx/nginx.conf:/etc/nginx/nginx.conf:ro \
  7_nginx
```

## Заходим на сайт [http://localhost](http://localhost)

