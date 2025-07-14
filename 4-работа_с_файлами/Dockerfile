FROM python:3.12
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
#COPY ./todo_result ./todo_result
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY tg_bot.py ./tg_bot.py
ENTRYPOINT ["python3", "tg_bot.py"]