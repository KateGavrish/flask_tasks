from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/list_prof/<list>')
def odd_even(list):
    a = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию']
    return render_template('index.html', a=a, list=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
