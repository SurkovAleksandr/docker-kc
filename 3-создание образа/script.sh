#!/bin/bash
set -e

for i in 1 2 3 4 5 6; do
  echo $i
done

all_args=$@
name=$1
len=${#name}
first_letter=${name::1}
rest_letters=${name:1:len}

echo $name
echo $len
echo $first_letter
echo $rest_letters
echo $all_args
echo $!
ps aux

if [ -z "$name" ]; then
    echo "Нужно ввести аргумент"
    exit 1
else
  echo "Hello, ${first_letter^}${rest_letters,,} :)"
fi

# Эмулируем долгую работу внутри контейнера
long_task() {
  while true ; do
    sleep 3
    CURRENT_TIME=$(date)
    echo $CURRENT_TIME
  done
}

long_task &

ps aux

# ловим SIGTERM и SIGINT, пересылаем дочернему процессу и ждём его
trap 'echo "SIGTERM/SIGINT received, forwarding to $child"; kill -TERM "$child" 2>/dev/null; wait "$child"; exit 0' TERM INT
CHILD=$!
wait $CHILD



