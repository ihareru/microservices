import datetime
from flask import Flask

app = Flask(__name__)

count = 0

@app.route('/hello')
def test_function():
    now = datetime.datetime.now().utcnow()
    return f'Это новая страничка, ответ сгенерирован в {now}'

@app.route('/hello/world')
def hello_world():
    return f'Привет мир!'

@app.route('/counter')
def counter():
    global count
    count += 1
    return f'Страница открывалась {count} раз.'
