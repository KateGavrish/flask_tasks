from flask import Flask, render_template
from data import db_session
from data.u import User
from data.j import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    db_session.global_init("journal/db/blogs.sqlite")
    session = db_session.create_session()
    i = []
    for job in session.query(Jobs).all():
        i.append([job.id, job.job, job.team_leader, job.work_size, job.collaborators, job.is_finished])
    return render_template('job.html', i=i)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
