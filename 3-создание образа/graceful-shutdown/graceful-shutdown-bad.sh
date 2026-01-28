#!/bin/bash
# graceful-shutdown-bad.sh — тест BAD сценария

# ❌ Создаём образ с bash = PID 1 (без exec)
cat > Dockerfile << 'EOF'
FROM nginx:alpine
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
EOF

cat > entrypoint.sh << 'EOF'
#!/bin/sh
echo "=== BAD: bash/shell = PID 1 (shell-форма без exec) ==="
nginx -g "daemon off;"  # ❌ НЕ exec — shell остается PID 1
EOF

docker build -t bad-pid1 .
docker rm -f test
docker run -d --name test -p 8080:80 bad-pid1

sleep 2

# Длинный запрос
curl -v -N http://localhost:8080/ &
REQ_PID=$!
echo "Запрос запущен (PID $REQ_PID)"

# Остановка
docker stop -t 5 test

# ❌ КЛЮЧ: TIMEOUT + kill curl
if timeout 3s wait $REQ_PID 2>/dev/null; then # 0 в bash это true
  echo "✓ Завершился нормально (graceful)"
else
  # $? это exit-код(код возврата) последней выполненной команды
  echo "✗ ОБОРВАН (violent ✓)  exit=$?"
#  kill $REQ_PID 2>/dev/null  # Принудительно убиваем зависший curl
fi

docker logs test | tail -5   # Резкий обрыв
docker inspect test --format='{{.State.ExitCode}}'  # 137/143
