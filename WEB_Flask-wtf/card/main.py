from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)


@app.route('/member')
def answ():
    with open("templates/people.json", encoding="utf-8") as f:
        people_list = json.loads(f.read())
    return render_template('card.html', s=people_list['people'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
