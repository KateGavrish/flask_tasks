from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/auto_answer')
@app.route('/answer')
def answ():
    params = dict()
    params['title'] = 'Анкета'
    params['surname'] = 'Watny'
    params['name'] = 'Mark'
    params['education'] = 'выше среднего'
    params['profession'] = 'штурман марсохода'
    params['sex'] = 'male'
    params['motivation'] = 'Всегда мечтал застрять на Марсе!'
    params['ready'] = 'True'
    return render_template('auto_answer.html', params=params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
