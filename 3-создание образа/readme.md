Одной из особенностей изучения в этом уроке(этого не было в курсе)
является обработка сигнала SIGTERM. Docker образ должен быть создан/запущен таким
образом, чтобы он обрабатывал корректно этот сигнал, т.е. выполнял graceful shutdown.
Признаком того, что контейнер завершился с graceful shutdown является 0 в результате завершения контейнера.
```shell
docker inspect task_3_container --format='{{.State.ExitCode}}'
```
Если это не так, то будет 137 (SIGKILL), 143 (SIGTERM+timeout)

Для демонстрации смотреть(разница в exec):
- [graceful-shutdown-bad.sh](graceful-shutdown/graceful-shutdown-bad.sh)
- [graceful-shutdown-good.sh](graceful-shutdown/graceful-shutdown-good.sh)

```shell
docker logs api | tail -5  # Ищем "graceful" логи
docker inspect api --format='{{.State.ExitCode}}'  # 0 = OK
```


```shell
# Создаем образ
docker build -t task_3:1.0 .
```

```shell
docker run -d \
  --name task_3_container \
  task_3:1.0 "asda" "sdsa"
```

Посмотреть логи контейнера
```shell
docker logs task_3_container
```
