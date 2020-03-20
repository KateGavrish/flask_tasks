from flask import Flask, url_for, request, render_template
import datetime
import os

app = Flask(__name__)


@app.route('/galery', methods=['POST', 'GET'])
def Mars():
    a = os.listdir('static/img')
    if request.method == 'GET':
        return render_template('galery.html', a=a)
    elif request.method == 'POST':
        f = request.files['file']
        map_file = f"static/img/{datetime.datetime.now()}.png"
        with open(map_file, "wb") as file:
            file.write(f.stream.read())
        a = os.listdir('static/img')
        return render_template('galery.html', a=a)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
