FROM python:3.12
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip && python -m pip install --no-cache-dir -r requirements.txt
COPY ./app.py ./app.py
COPY ./wsgi.py ./wsgi.py
EXPOSE 8080
CMD ["python", "wsgi.py"]