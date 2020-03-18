from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/distribution')
def answ():
    params = dict()
    params['title'] = 'Title'
    params['name'] = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('room.html', params=params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
