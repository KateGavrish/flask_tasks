from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/answer')
def answ(list):
    return render_template('index.html', a=a, list=list)


@app.route('/answer')
def auto_answ(list):
    return render_template('index.html', a=a, list=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
