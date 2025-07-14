from app import app
'''
    Web-приложение на Flask, которое взаимодействует с БД PostgreSQL.
    У обоих приложений должна быть одна сеть.
    docker run --rm -d --name kc_6_back -p 8080:8080 -e HOST=postgres17_5 --net kc_6_net kc_6_back:latest
'''
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
#    app.run()
