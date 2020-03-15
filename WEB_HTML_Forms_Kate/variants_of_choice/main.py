from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/choice/<planet>')
def form_sample(planet):
    return f'''<!doctype html>
                    <html lang="en">
                        <head>
                        <meta charset="utf-8">
                        <meta name="viewport" static="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                        </head>
                        <body>
                            <h1>Мое предложение: {planet}</h1>
                            <h2>Эта планета близка к Земле</h2>
                            <div class="alert alert-warning" role="alert">
                                На ней много необходимых ресурсов;
                            </div>
                            <div class="alert alert-primary" role="alert">
                                На ней есть вода и атмосфера;
                            </div>
                            <div class="alert alert alert-secondary" role="alert">
                                На ней есть небольшщое магнитное поле;
                            </div>
                            <div class="alert alert-info" role="alert">
                                Наконец, она просто красива!
                            </div>
                        </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
