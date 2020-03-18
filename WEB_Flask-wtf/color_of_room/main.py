from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/table_param/<sex>/<int:age>')
def answ(sex, age):
    return render_template('color.html', sex=sex, age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
